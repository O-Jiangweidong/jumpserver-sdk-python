from ..common import Instance


class CommandGroupInstance(Instance):
    TYPE = 'CommandGroup'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr name: 名称
        :attr comment: 备注
        :attr content: 内容
        :attr ignore_case: 是否忽略大小写
        :attr type: 类型
        :attr org_id: 组织 ID（只读）
        :attr org_name: 组织名称（只读）
        """
        self.id: str = ''
        self.name: str = ''
        self.comment: str = ''
        self.content: str = ''
        self.ignore_case: bool = True
        self.type: dict = {}
        self.org_id: str = ''
        self.org_name: str = ''
        super().__init__(**kwargs)
