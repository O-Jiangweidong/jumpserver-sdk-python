import sys
import time

from importlib import import_module


def cached_import(module_path, class_name):
    module = sys.modules.get(module_path)
    spec = getattr(module, "__spec__", None)
    if not (module and spec and getattr(spec, "_initializing", False)):
        module = import_module(module_path)
    return getattr(module, class_name)


def import_string(dotted_path):
    try:
        module_path, class_name = dotted_path.rsplit(".", 1)
    except ValueError as err:
        raise ImportError("%s doesn't look like a module path" % dotted_path) from err

    try:
        return cached_import(module_path, class_name)
    except AttributeError as err:
        exc_info = f'Module "{module_path}" does not define a "{class_name}" attribute/class'
        raise ImportError(exc_info) from err


def record_time(func):
    def inner(self, *args, **kwargs):
        start = time.time()
        resp = func(self, *args, **kwargs)
        self.timer += time.time() - start
        return resp
    return inner
