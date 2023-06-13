import os
import pkgutil
import importlib


def recursive_import(path_: str, module_name: str):
    for module_path, name, is_pkg in pkgutil.iter_modules([path_]):
        if is_pkg:
            recursive_import(f"{module_path.path}/{name}", module_name + f'.{name}')
        else:
            importlib.import_module(module_name + f'.{name}')


path = os.path.dirname(__file__)


def init():
    recursive_import(path, __name__)
