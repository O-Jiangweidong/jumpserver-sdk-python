from .common import Instance


class DomainInstance(Instance):
    TYPE = 'Domain'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr name: 名称
        :attr comment: 备注
        :attr org_id: 组织 ID
        :attr org_name: 组织名称
        :attr date_created: 创建时间
        :attr gateways: 网关资产
        :attr assets_amount: 资产关联数量
        """
        self.id: str = ''
        self.name: str = ''
        self.comment: str = ''
        self.org_id: str = ''
        self.org_name: str = ''
        self.date_created: str = ''
        self.gateways: dict = {}
        self.assets_amount: int = 0
        super().__init__(**kwargs)

    def __str__(self):
        return f'<{self.TYPE}>: {self.name}'

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return vars(self)
