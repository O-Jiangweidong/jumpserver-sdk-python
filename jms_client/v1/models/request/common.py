from urllib.parse import urlencode


class Request(object):
    URL = ''
    InstanceClass = None

    def __init__(
            self, instance=None, **kwargs
    ):
        self.url_prefix = 'api/v1/'
        self.instance = instance

    @staticmethod
    def get_method():
        return 'get'

    @staticmethod
    def get_params():
        return {}

    def get_url(self):
        params = self.get_params()
        return f'{self.url_prefix}{self.URL}?{urlencode(params)}'

    @staticmethod
    def get_data():
        return {}

    @staticmethod
    def get_headers():
        return {}
