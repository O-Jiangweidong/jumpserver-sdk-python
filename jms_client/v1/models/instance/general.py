from .common import Instance


__all__ = [
    'ResourceCacheInstance',
]


class ResourceCacheInstance(Instance):
    TYPE = 'Spm'

    def __init__(self,  **kwargs):
        """
        :attr spm: 缓存 ID
        """
        self.spm: str = ''
        super().__init__(**kwargs)
