from ..common import Instance


class ConnectMethodACLInstance(Instance):
    TYPE = 'ConnectMethodACL'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr name: 名称
        :attr comment: 备注
        :attr priority: 优先级
        :attr is_active: 是否激活
        :attr created_by: 创建者
        :attr date_created: 创建日期
        :attr date_updated: 更新日期
        :attr org_id: 组织 ID（只读）
        :attr actions: 授权的动作
        :attr connect_methods: 允许的协议
        :attr reviewers: 接收人，无用
        :attr users: 受控制的用户
        """
        self.id: str = ''
        self.name: str = ''
        self.comment: str = ''
        self.priority: int = 50
        self.is_active: bool = True
        self.date_created: str = ''
        self.date_update: str = ''
        self.org_id: str = ''
        self.actions: dict = {}
        self.reviewers: list = []
        self.users: list = []
        super().__init__(**kwargs)
