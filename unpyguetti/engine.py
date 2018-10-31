import ast
import pathlib2

from .loader import ModuleLoader


class Visitor(ast.NodeVisitor):
    VARIABLE_NAME = 'version'

    def __init__(self, definitions):
        self.definitions = definitions

    def visit_generic(self, node):
        for strategy in self.definitions:
            for matcher, execute_refactoring in strategy.matchers.items():
                if matcher.accepts(node):
                    node = execute_refactoring(node)


    def visit_FunctionDef(self, node):
        for strategy in self.definitions:
            for matcher, execute_refactoring in strategy.matchers.items():
                if matcher.accepts(node):
                    node = execute_refactoring(node)


class RefactoringSession(object):
    def __init__(self):
        self.load = ModuleLoader()

    def run(self, targets):
        finder = Visitor(self.load.definitions)

        for path in map(pathlib2.Path, targets):
            if not path.exists():
                raise RuntimeError(f'{path} does not exist')

            if not path.is_file():
                raise RuntimeError(f'{path} is not a valid file')

        finder.visit(ast.parse(path.open('r').read()))
