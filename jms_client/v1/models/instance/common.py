class Instance(object):
    def __init__(self, *args, **other):
        self._bind_attrs(other)

    def _bind_attrs(self, attrs):
        for k, v in attrs.items():
            setattr(self, k, v)
