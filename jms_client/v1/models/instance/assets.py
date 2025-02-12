from .common import Instance


class AssetInstance(Instance):
    TYPE = 'Asset'

    def __init__(
            self,
            name,
            address,
            nodes,
            platform,
            id=None,
            auto_config=None,
            comment='',
            domain=None,
            is_active=True,
            labels=None,
            protocols=None,
            **kwargs
    ):
        """
        :param name: 资产名称
        :param address: 资产地址
        :param nodes: 节点
        :param platform: 平台
        :param id: 资产ID（可选）
        :param auto_config: 自动化配置（可选）
        :param comment: 备注（可选）
        :param domain: 网域（可选）
        :param is_active: 激活状态（可选）
        :param labels: 标签（可选）
        :param protocols: 协议（可选）
        :param kwargs: 其他参数
        """
        self.id = id
        self.address = address
        self.name = name
        self.auto_config = auto_config
        self.comment = comment
        self.domain = domain
        self.is_active = is_active
        self.labels = labels
        self.nodes = nodes
        self.platform = platform
        self.protocols = protocols
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

    def __init__(
            self,
            allow_invalid_cert=False,
            use_ssl=False,
            ca_cert='',
            client_cert='',
            client_key='',
            db_name='',
            **kwargs
    ):
        """
        :param allow_invalid_cert: 是否忽略证书检查（可选）
        :param use_ssl: 是否使用 SSL/TLS（可选）
        :param ca_cert: CA 证书（可选）
        :param client_cert: 客户端证书（可选）
        :param client_key: 客户端密钥（可选）
        :param db_name: 数据库名（可选）
        :param kwargs: 其他参数
        """
        self.use_ssl = use_ssl
        self.allow_invalid_cert = allow_invalid_cert
        self.ca_cert = ca_cert
        self.client_cert = client_cert
        self.client_key = client_key
        self.db_name = db_name
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

    def __init__(
            self,
            autofill='no',
            username_selector='name=username',
            password_selector='name=password',
            submit_selector='id=login_button',
            script=None,
            **kwargs
    ):
        """
        :param autofill: 自动填充（可选）
        :param username_selector: 用户名选择器（可选）
        :param password_selector: 密码选择器（可选）
        :param submit_selector: 提交选择器（可选）
        :param script: 脚本内容（可选）
        :param kwargs: 其他参数
        """
        self.autofill = autofill
        self.username_selector = username_selector
        self.password_selector = password_selector
        self.submit_selector = submit_selector
        self.script = script
        super().__init__(**kwargs)


class GPTInstance(AssetInstance):
    TYPE = 'GTP'

    def __init__(self, proxy='', **kwargs):
        """
        :param proxy: HTTP(s) 代理（可选）
        :param kwargs: 其他参数
        """
        self.proxy = proxy
        super().__init__(**kwargs)


class CustomInstance(AssetInstance):
    TYPE = 'Custom'

    def __init__(self, custom_info=None, **kwargs):
        self.custom_info = custom_info
        super().__init__(**kwargs)
