from jms_client.v1.models.instance.general import ResourceCacheInstance
from .common import Request


__all__ = [
    'CreateResourceCacheRequest',
]


class BaseResourceCacheRequest(Request):
    URL = 'common/resources/cache/'
    InstanceClass = ResourceCacheInstance


class CreateResourceCacheRequest(BaseResourceCacheRequest):
    """ 创建资源缓存 """
    _body: dict

    def __init__(
            self,
            resources: list,
            **kwargs
    ):
        """
        :param resources: 资源对象 ID 列表
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self._body['resources'] = resources

    @staticmethod
    def get_method():
        return 'post'
