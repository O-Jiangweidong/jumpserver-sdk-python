class Instance(object):
    def __init__(self, *args, **kwargs):
        pass


class GenerateDeleteInstance(Instance):
    def __init__(self, id, *args, **kwargs):
        """
        :param id: 对象 ID
        :param args: 其他参数
        :type kwargs: 其他参数
        """
        self.id = id
        super().__init__(*args, **kwargs)
