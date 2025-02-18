from ..common import Instance


class ChangePasswordLogInstance(Instance):
    TYPE = 'ChangePasswordLog'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr remote_addr: 操作者远端地址
        :attr datetime: 操作日期
        :attr change_by: 修改人
        :attr user: 用户名标识
        """
        self.id: str = ''
        self.remote_addr: str = ''
        self.datetime: str = ''
        self.change_by: str = ''
        self.user: str = ''
        super().__init__(**kwargs)

    @property
    def display(self):
        return self.user
