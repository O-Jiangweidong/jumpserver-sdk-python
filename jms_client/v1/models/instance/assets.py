from .common import Instance


class AssetInstance(Instance):
    TYPE = 'Asset'

    def __init__(self, **kwargs):
        """
        :attr name: 资产名称
        :attr address: 资产地址
        :attr nodes: 节点
        :attr platform: 平台
        :attr id_: 资产 ID
        :attr auto_config: 自动化配置
        :attr comment: 备注
        :attr domain: 网域
        :attr is_active: 激活状态
        :attr labels: 标签
        :attr protocols: 协议
        :attr category: 资产类别
        :attr connectivity: 连通性
        :attr created_by: 创建人
        :attr date_created: 创建时间
        :attr date_verified: 验证时间
        """
        self.id: str = ''
        self.address: str = ''
        self.name: str = ''
        self.auto_config: dict = {}
        self.comment: str = ''
        self.domain: dict = {}
        self.is_active: bool = False
        self.labels: list = []
        self.nodes: list = []
        self.platform: dict = {}
        self.protocols: list = []
        # readonly
        self.category = ''
        self.connectivity = ''
        self.created_by = ''
        self.date_created = ''
        self.date_verified = ''
        super().__init__(**kwargs)

    def __str__(self):
        return f'<{self.TYPE}>: {self.name}({self.address})'

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return vars(self)


class HostInstance(AssetInstance):
    TYPE = 'Host'

    def __init__(self, **kwargs):
        # readonly
        self.gathered_info = ''
        self.nodes_display = []
        self.org_id = ''
        self.org_name = ''
        self.spec_info = ''
        self.type = ''
        super().__init__(**kwargs)


class DatabaseInstance(AssetInstance):
    TYPE = 'Database'

    def __init__(self, **kwargs):
        """
        :attr allow_invalid_cert: 是否忽略证书检查
        :attr use_ssl: 是否使用 SSL/TLS
        :attr ca_cert: CA 证书
        :attr client_cert: 客户端证书
        :attr client_key: 客户端密钥
        :attr db_name: 数据库名
        """
        self.use_ssl: bool = False
        self.allow_invalid_cert: bool = False
        self.ca_cert: str = ''
        self.client_cert: str = ''
        self.client_key: str = ''
        self.db_name: str = ''
        super().__init__(**kwargs)


class DeviceInstance(AssetInstance):
    TYPE = 'Device'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class CloudInstance(AssetInstance):
    TYPE = 'Cloud'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class WebInstance(AssetInstance):
    TYPE = 'Web'

    def __init__(self, **kwargs):
        """
        :attr autofill: 自动填充
        :attr username_selector: 用户名选择器
        :attr password_selector: 密码选择器
        :attr submit_selector: 提交选择器
        :attr script: 脚本内容
        """
        self.autofill: bool = False
        self.username_selector: str = ''
        self.password_selector: str = ''
        self.submit_selector: str = ''
        self.script: list = []
        super().__init__(**kwargs)


class GPTInstance(AssetInstance):
    TYPE = 'GTP'

    def __init__(self, **kwargs):
        """
        :attr proxy: HTTP(s) 代理地址
        """
        self.proxy: str = ''
        super().__init__(**kwargs)


class CustomInstance(AssetInstance):
    TYPE = 'Custom'

    def __init__(self, **kwargs):
        """
        :attr custom_info: 自定义字段信息
        """
        self.custom_info: dict = {}
        super().__init__(**kwargs)
