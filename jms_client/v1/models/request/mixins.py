from urllib.parse import urlencode

from .const import FIELDS_MINI, FIELDS_SMALL


class WithIDMixin(object):
    URL: str
    url_prefix: str
    instance: object = None
    get_params: callable

    def __init__(self, id_, *args, **kwargs):
        if not id_:
            raise ValueError('Param [id_] is required')

        self.id = id_
        self.other = kwargs
        super().__init__(*args, **kwargs)

    def get_url(self):
        self.other.update(self.get_params())
        if '{id}' in self.URL:
            url = self.URL.format(id=self.id)
        else:
            url = f'{self.URL}{self.id}/'
        return f'{self.url_prefix}{url}'


class DeleteMixin(WithIDMixin):
    @staticmethod
    def get_method():
        return 'delete'


class BulkDeleteMixin(object):
    URL: str
    url_prefix: str

    def __init__(self, spm: str, *args, **kwargs):
        """
        :param spm: 根据 CreateResourceCacheRequest 获取
        """
        self._spm = spm
        super().__init__(*args, **kwargs)

    def get_url(self):
        return f'{self.url_prefix}{self.URL}?spm={self._spm}'

    @staticmethod
    def get_method():
        return 'delete'


class UpdateMixin(WithIDMixin):
    @staticmethod
    def get_method():
        return 'put'


class ExtraRequestMixin(object):
    def __init__(
            self,
            limit=100,
            offset=0,
            fields_size='',
            search='',
            **kwargs
    ):
        other = {'limit': limit, 'offset': offset}
        if fields_size in (FIELDS_MINI, FIELDS_SMALL):
            other['fields_size'] = fields_size
        if search:
            other['search'] = search

        super().__init__(**other, **kwargs)


class CreateMixin(object):
    _body: dict

    def __init__(
            self,
            id_: str = '',
            **kwargs
    ):
        """
        :param id_: ID
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        if id_:
            self._body['id'] = id_

    @staticmethod
    def get_method():
        return 'post'
