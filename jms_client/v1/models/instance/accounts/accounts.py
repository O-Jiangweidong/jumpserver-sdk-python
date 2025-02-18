from ..common import Instance


class AccountsInstance(Instance):
    TYPE = 'Account'

    def __init__(self, **kwargs):
        """
        :attr name: 账号名称
        :attr username: 账号用户名
        :attr secret_type: 密文类型
        :attr id_: 账号 ID
        :attr source: 账号来源
        :attr comment: 备注
        :attr asset: 账号绑定的资产
        :attr privileged: 特权账号
        :attr is_active: 活跃性
        """
        self.id: str = ''
        self.asset: dict = {}
        self.username: str = ''
        self.name: str = ''
        self.secret_type: str = ''
        self.source: str = ''
        self.privileged: bool = False
        self.is_active: bool = True
        self.comment: str = ''
        # readonly
        self.connectivity = ''
        self.created_by = ''
        self.date_created = ''
        self.date_verified = ''
        self.org_id = ''
        self.org_name = ''
        self.has_secret = True
        super().__init__(**kwargs)

    def display(self):
        return f'{self.name}({self.username})'
