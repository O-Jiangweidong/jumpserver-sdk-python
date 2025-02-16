from .common import Instance


class OrganizationInstance(Instance):
    TYPE = 'Organization'

    def __init__(self,  **kwargs):
        """
        :attr name: 名称
        :attr id: ID
        :attr comment: 备注
        :attr internal: 是否为内置组织
        :attr is_default: 是否为默认组织
        :attr is_root: 是否为全局组织
        :attr created_by: 创建者
        :attr date_created: 创建时间
        :attr resource_statistics: 组织资源统计（只读）
        """
        self.id: str = ''
        self.name: str = ''
        self.comment: str = ''
        # readonly
        self.internal: bool = False
        self.is_default: bool = False
        self.is_root: bool = False
        self.created_by: str = ''
        self.date_created: str = ''
        self.resource_statistics: dict = {
            'asset_perms_amount': 0, 'assets_amount': 0,
            'domains_amount': 0, 'groups_amount': 0,
            'nodes_amount': 0, 'users_amount': 0,
        }
        super().__init__(**kwargs)
