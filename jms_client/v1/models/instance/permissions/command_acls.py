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


class CommandFilterInstance(Instance):
    TYPE = 'CommandFilter'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr name: 名称
        :attr comment: 备注
        :attr org_id: 组织 ID
        :attr org_name: 组织名称
        :attr priority: 优先级
        :attr accounts: 账号
        :attr action: 动作
        :attr assets: 资产
        :attr command_groups: 命令组
        :attr created_by: 创建者
        :attr date_created: 创建日期
        :attr date_updated: 更新日期
        :attr is_active: 是否激活
        :attr reviewers: 审核接受者
        :attr users: 控制的用户
        """
        self.id: str = ''
        self.name: str = ''
        self.comment: str = ''
        self.org_id: str = ''
        self.org_name: str = ''
        self.priority: int = 0
        self.accounts: list[str] = []
        self.action: dict = {}
        self.assets: dict = {}
        self.command_groups: list = []
        self.created_by: str = ''
        self.date_created: str = ''
        self.date_updated: str = ''
        self.is_active: bool = False
        self.reviewers: list = []
        self.users: dict = {}
        super().__init__(**kwargs)
