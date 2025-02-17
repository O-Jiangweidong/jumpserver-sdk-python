from .const import FIELDS_MINI, FIELDS_SMALL


class DetailMixin(object):
    URL: str
    url_prefix: str
    instance: object = None

    def __init__(self, id_, *args, **kwargs):
        if not id_:
            raise ValueError('Param [id_] is required')

        self.id = id_
        super().__init__(*args, **kwargs)

    def get_url(self):
        return f'{self.url_prefix}{self.URL}{self.id}/'


class DeleteMixin(DetailMixin):
    @staticmethod
    def get_method():
        return 'delete'


class UpdateMixin(DetailMixin):
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
        self._other = {'limit': limit, 'offset': offset}
        if fields_size in (FIELDS_MINI, FIELDS_SMALL):
            self._other['fields_size'] = fields_size
        if search:
            self._other['search'] = search

        super().__init__(**kwargs)

    def get_params(self):
        return self._other


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
