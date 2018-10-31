import ast
import imp
import inspect
import hashlib
import importlib

import pathlib2

from unpyguetti.refactoring import Strategy


class LoadingError(Exception):
    pass

class IOLoadingError(LoadingError):
    pass


class ImportLoadingError(LoadingError):
    pass


class ModuleLoader(object):
    def __init__(self):
        self.modules = []
        self.definitions = []

    def from_source(self, path):
        path = pathlib2.Path(path)

        if not path.is_file():
            raise IOLoadingError(f'source file does not exist {path}')

        name = 'module_{}'.format(path)

        module = imp.load_source(name, str(path), path.open('r'))
        self.register_module(module, name, path)


    def from_module(self, name):
        try:
            module = importlib.import_module(name)
        except (SyntaxError, ImportError) as error:
            raise ImportLoadingError(f'{error}')

        self.register_module(module, name)

    def register_module(self, module, name, path=None):
        if path is None:
            path = module.__file__

        members =  inspect.getmembers(module)
        info = (module, name, members, path)
        self.modules.append(info)

        for name, member in members:
            if isinstance(member, Strategy):
                self.definitions.append(member)

        return info
