from ..common import Instance


class PermissionInstance(Instance):
    TYPE = 'Permission'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr name: 名称
        :attr comment: 备注
        :attr is_active: 是否激活
        :attr labels: 标签
        :attr accounts: 授权的账号
        :attr actions: 授权的动作
        :attr protocols: 授权的协议
        :attr created_by: 创建者
        :attr date_created: 创建时间
        :attr date_start: 开始时间
        :attr date_expired: 过期时间
        :attr is_valid: 是否有效（只读）
        :attr is_expired: 是否过期（只读）
        :attr org_id: 组织 ID（只读）
        :attr org_name: 组织名称（只读）
        :attr from_ticket: 是否工单创建（只读）
        :attr assets_amount: 授权的资产数量（只读）
        :attr nodes_amount: 授权的节点数量（只读）
        :attr user_groups_amount: 授权的用户组数量（只读）
        """
        self.id: str = ''
        self.name: str = ''
        self.comment: str = ''
        self.is_active: bool = True
        self.labels: list = []
        self.accounts: list = []
        self.actions: list = []
        self.protocols: list = []
        self.date_start: str = ''
        self.date_expired: str = ''
        # readonly
        self.is_valid: bool = True
        self.is_expired: bool = False
        self.org_id: str = ''
        self.org_name: str = ''
        self.created_by: str = ''
        self.date_created: str = ''
        self.from_ticket: bool = False
        self.assets_amount: int = 0
        self.nodes_amount: int = 0
        self.user_groups_amount: int = 0
        super().__init__(**kwargs)
