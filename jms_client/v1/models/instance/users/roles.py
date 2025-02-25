from ..common import Instance


class RoleInstance(Instance):
    TYPE = 'Role'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr name: 名称
        :attr comment: 备注
        :attr builtin: 是否内置
        :attr created_by: 创建者
        :attr updated_by: 更新者
        :attr date_created: 创建时间
        :attr date_updated: 更新时间
        :attr display_name: 显示名称
        :attr scope: 角色类型
        :attr users_amount: 关联的用户数量
        """
        self.id: str = ''
        self.name: str = ''
        self.comment: str = ''
        self.builtin: bool = False
        self.created_by: str = ''
        self.updated_by: str = ''
        self.date_created: str = ''
        self.date_updated: str = ''
        self.display_name: str = ''
        self.scope: dict = {}
        self.users_amount: int = 0
        super().__init__(**kwargs)


class RoleUserInstance(Instance):
    TYPE = 'RoleRelationUser'

    def __init__(self, **kwargs):
        """
        :attr id: ID
        :attr org: 组织 ID
        :attr org_name: 组织名称
        :attr role: 角色 ID
        :attr scope: 角色类型
        :attr user: 用户信息
        """
        self.id: str = ''
        self.org: str = ''
        self.org_name: str = ''
        self.role: str = ''
        self.scope: str = ''
        self.user: dict = {}
        super().__init__(**kwargs)

    @property
    def display(self):
        return f'{self.user["name"]}'
