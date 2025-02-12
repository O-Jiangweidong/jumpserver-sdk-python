from functools import partial
from types import MethodType

from jms_client.exceptions import JMSException


class Version(object):
    def __init__(self, version, sep='.'):
        self.version = self.corrected_version(version)
        self.major, self.minor = self.get_version_list(sep)

    @staticmethod
    def corrected_version(version):
        version = str(version)
        version_flag_index = str(version).rfind('v')
        if version_flag_index != -1:
            version = version[version_flag_index+1:]
        return version

    def get_version_list(self, sep):
        version_list = self.version.split(sep)
        if len(version_list) < 2 or not (all(map(lambda x: x.isdigit(), version_list))):
            raise JMSException(f'错误的版本信息: {self.version}。JumpServer 版本信息不对.(例：3.10)')
        return [int(i) for i in version_list[:2]]

    def find_best_match(self, versions):
        """
        versions 是按照从大到小的版本排序的
        版本查找方式是按照最近最小版本原则
        """
        for v in versions:
            if not isinstance(v, Version):
                v_instance = Version(v, sep='_')
            else:
                v_instance = v

            if self >= v_instance:
                return True, v
        return False, None

    def __ge__(self, other):
        if not isinstance(other, Version):
            return False
        if self.major > other.major:
            return True
        if self.major == other.major:
            return self.minor >= other.minor
        return False


def get_instance_like_methods(instance, prefix=''):
    """
    根据指定前缀获取某个对象的类似方法
    :param instance:
    :param like:
    :return:
    """
    all_attributes = dir(instance)
    methods = []
    for attr in all_attributes:
        method = getattr(instance, attr)
        if not attr.startswith('__') \
                and attr.startswith(prefix) \
                and isinstance(method, MethodType):
            methods.append(attr)
    methods.sort(reverse=True)
    return methods


def version_routing(func):
    """
    这是一个版本路由转发的类装饰器，必须装饰在类方法上
    :param func:
    :return:
    """
    def inner(self, *args, **kwargs):
        prefix = func.__name__
        methods = get_instance_like_methods(self, prefix=prefix)
        jms_version = self.client.api_version

        exist, version = Version(jms_version).find_best_match(methods[:-1])
        if exist:
            new_func = getattr(self, version)
        else:
            new_func = partial(func, self)
        return new_func(*args, **kwargs)
    return inner
