from .common import Instance


class OrganizationInstance(Instance):
    TYPE = 'Organization'

    def __init__(
            self,
            name: str,
            id_: str = None,
            comment: str = '',
            **kwargs
    ):
        """
        :param name: 组织名称
        :param id: 组织 ID（可选）
        :param comment: 备注（可选）
        :param kwargs: 其他参数
        """
        self.id = id_
        self.name = name
        self.comment = comment
        # readonly
        self.internal = False
        self.is_default = False
        self.is_root = False
        self.created_by = ''
        self.date_created = ''
        self.resource_statistics = {
            'asset_perms_amount': 0, 'assets_amount': 0,
            'domains_amount': 0, 'groups_amount': 0,
            'nodes_amount': 0, 'users_amount': 0,
        }
        super().__init__(**kwargs)

    def __str__(self):
        return f'<{self.TYPE}>: {self.name}'

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return vars(self)
