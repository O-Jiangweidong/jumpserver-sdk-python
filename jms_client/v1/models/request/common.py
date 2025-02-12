from urllib.parse import urlencode

from .const import FIELDS_MINI, FIELDS_SMALL


class Request(object):
    URL = ''
    InstanceClass = None

    def __init__(
            self, limit=100, offset=0, fields_size='', instance=None, **kwargs
    ):
        self.url_prefix = 'api/v1/'
        self.limit = limit
        self.offset = offset
        self.fields_size = fields_size
        self.instance = instance
        self.other = kwargs

    @staticmethod
    def get_method():
        return 'get'

    def get_url(self):
        params = self.other.copy()
        if self.fields_size in (FIELDS_MINI, FIELDS_SMALL):
            params['fields_size'] = self.fields_size
        params.update({'limit': self.limit, 'offset': self.offset})
        return f'{self.url_prefix}{self.URL}?{urlencode(params)}'

    @staticmethod
    def get_data():
        return {}

    @staticmethod
    def get_headers():
        return {}
