import functools
from collections import OrderedDict



class Strategy(object):
    def __init__(self, description):
        self.description = description
        self.matchers = OrderedDict()

    def on(self, matcher):
        def decorator(func):
            self.matchers[matcher] = func
            return func

        return decorator

    def __repr__(self):
        return f'Strategy("{self.description}")'
