

class Request(object):
    URL = ''
    InstanceClass = None

    def __init__(
            self, instance=None, **kwargs
    ):
        self.url_prefix = 'api/v1/'
        self.instance = instance
        self.other = kwargs
        self._body = {}

    @staticmethod
    def get_method():
        return 'get'

    def get_params(self):
        return self.other

    def get_url(self):
        return f'{self.url_prefix}{self.URL}'

    def get_data(self):
        return self._body

    @staticmethod
    def get_headers():
        return {}
