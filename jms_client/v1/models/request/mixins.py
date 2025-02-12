

class GetInstanceMixin(object):
    URL: str
    url_prefix: str
    instance: object = None

    def get_instance_id(self):
        if not self.instance or not getattr(self.instance, 'id', None):
            raise ValueError(
                'When performing delete action, the parameter [instance] is required'
            )
        return self.instance.id

    def get_url(self):
        instance_id = self.get_instance_id()
        return f'{self.url_prefix}{self.URL}{instance_id}/'
