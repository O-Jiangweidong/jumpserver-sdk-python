class Instance(object):
    TYPE = 'Unknown'

    def __init__(self, *args, **other):
        self._bind_attrs(other)

    def _bind_attrs(self, attrs):
        for k, v in attrs.items():
            setattr(self, k, v)

    @property
    def display(self):
        return getattr(self, 'name', 'Unknown')

    def __str__(self):
        return f'<{self.TYPE}>: {self.display}'

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return vars(self)
