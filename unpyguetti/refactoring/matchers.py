import _ast
import fnmatch


class Matcher(object):
    """base matcher"""
    node_type = None

    def __init__(self, named=None, **kw):
        self.meta = {
            'named': named,
        }

        self.initialize(**kw)

    def initialize(self, **kw):
        return kw

    def __repr__(self):
        classname = self.__class__.__name__
        return f'{classname}({self.meta})'
    def accepts(self, node):
        if self.node_type is None:
            return False

        if not isinstance(node, self.node_type):
            return False

        if not self.meta['named'].matches(node.name):
            return False

        return True


class Name(object):
    def __init__(self, value):
        self.value = value

    def matches(self, value):
        return self.value == value


class Glob(Name):
    """Glob matcher
    """

    def matches(self, value):
        return fnmatch.fnmatch(value, self.value)


class Function(Matcher):
    """matches function definitions, works for both methods, functions or lambdas
    """
    node_type = _ast.FunctionDef

    def initialize(self, with_params=None, **kw):
        self.meta['with_params'] = with_params or []

    def with_param(self, **kw):

        self.meta['with_params'].append(Argument(**kw))
        return self

    def within_class(self, **kw):
        self.meta['within_class'] = Class(**kw)
        return self

    def accepts(self, node):
        ok = super(Function, self).accepts(node)
        if not ok:
            return False

        matched_args = []
        argument_matchers = self.meta['with_params']
        for arg in node.args.args:
            for matcher in argument_matchers:
                if matcher.accepts(arg.arg):
                    matched_args = (matcher, arg.arg)
                    break


        if len(matched_args) < len(argument_matchers):
            return False

        import ipdb;ipdb.set_trace()

class Argument(Matcher):
    """matches arguments of functions, methods and lambdas
    """
    def accepts(self, arg):
        return self.meta['named'].matches(arg)

class Class(Matcher):
    """matches classes
    """
    node_type = _ast.ClassDef

    def with_param(self, named=None):
        self.meta['with_params'].append(Argument(**kw))
        return self


    def within_class(self, **kw):
        self.meta['within_class'] = Class(**kw)
        return self

    def accepts(self, node):
        ok = super(Function, self).accepts(node)
        if not ok:
            return False

        import ipdb;ipdb.set_trace()


anything = Glob('*')
