from ..common import Instance


class OperateLogInstance(Instance):
    TYPE = 'OperateLog'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr remote_addr: 操作者远端地址
        :attr datetime: 操作日期
        :attr org_id: 组织 ID
        :attr org_name: 组织名称
        :attr resource: 被操作对象
        :attr resource_type: 被操作对象类型
        :attr username: 用户名标识
        :attr action: 操作动作
        """
        self.id: str = ''
        self.remote_addr: str = ''
        self.datetime: str = ''
        self.org_id: str = ''
        self.org_name: str = ''
        self.resource: str = ''
        self.resource_type: str = ''
        self.username: str = ''
        self.action: dict = {}
        super().__init__(**kwargs)

    @property
    def display(self):
        return f'{self.resource}({self.resource_type})'
