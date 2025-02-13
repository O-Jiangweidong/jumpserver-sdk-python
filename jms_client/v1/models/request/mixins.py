

class DetailMixin(object):
    URL: str
    url_prefix: str
    instance: object = None

    def __init__(self, id, *args, **kwargs):
        self.id = id
        super().__init__(*args, **kwargs)

    def get_url(self):
        return f'{self.url_prefix}{self.URL}{self.id}/'
