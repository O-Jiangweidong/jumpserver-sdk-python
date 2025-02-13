from .const import FIELDS_MINI, FIELDS_SMALL


class DetailMixin(object):
    URL: str
    url_prefix: str
    instance: object = None

    def __init__(self, id_, *args, **kwargs):
        if not id_:
            raise ValueError('id_ is required')

        self.id = id_
        super().__init__(*args, **kwargs)

    def get_url(self):
        return f'{self.url_prefix}{self.URL}{self.id}/'


class ExtraRequestMixin(object):
    def __init__(self, limit=100, offset=0, fields_size='', **kwargs):
        self.limit = limit
        self.offset = offset
        self._other = {'limit': limit, 'offset': offset,}
        if fields_size in (FIELDS_MINI, FIELDS_SMALL):
            self._other['fields_size'] = fields_size

        super().__init__(**kwargs)

    def get_params(self):
        return self._other
