from ..common import Instance


class AccountInstance(Instance):
    TYPE = 'Account'

    def __init__(self, **kwargs):
        """
        :attr name: 账号名称
        :attr username: 账号用户名
        :attr secret_type: 密码类型
        :attr id_: 账号 ID
        :attr source: 账号来源
        :attr comment: 备注
        :attr asset: 资产信息
        :attr privileged: 特权账号
        :attr is_active: 活跃性
        :attr connectivity: 可连接性
        :attr created_by: 创建者
        :attr date_created: 创建日期
        :attr data_updated: 更新日期
        :attr org_id: 组织 ID
        :attr org_name: 组织名称
        :attr has_secret: 是否托管密码
        :attr labels: 标签
        :attr source_id: 创建该账号所使用的模板 ID
        :attr su_from: 切换自（该账号切换到其他账号下）
        :attr version: 账号版本号（初始值为1，修改一次加1）
        """
        self.id: str = ''
        self.asset: dict = {}
        self.username: str = ''
        self.name: str = ''
        self.secret_type: dict = {}
        self.source: dict = {}
        self.privileged: bool = False
        self.is_active: bool = True
        self.comment: str = ''
        self.labels: list = []
        self.source_id: str = ''
        self.su_from: dict = {}
        self.connectivity: dict = {}
        self.created_by = ''
        self.date_created = ''
        self.data_updated = ''
        self.org_id = ''
        self.org_name = ''
        self.has_secret = True
        self.version: int = 0
        super().__init__(**kwargs)

    def display(self):
        return f'{self.name}({self.username})'
