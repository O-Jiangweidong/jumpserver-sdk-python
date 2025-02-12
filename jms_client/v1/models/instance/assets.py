from .common import Instance


class AssetInstance(Instance):
    TYPE = 'Asset'

    def __init__(
            self,
            name,
            address,
            id=None,
            auto_config=None,
            comment='',
            domain=None,
            is_active=True,
            labels=None,
            nodes=None,
            platform=None,
            protocols=None,
            **kwargs
    ):
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
        self.autofill = autofill
        self.username_selector = username_selector
        self.password_selector = password_selector
        self.submit_selector = submit_selector
        self.script = script
        super().__init__(**kwargs)


class GPTInstance(AssetInstance):
    TYPE = 'GTP'

    def __init__(self, proxy='', **kwargs):
        self.proxy = proxy
        super().__init__(**kwargs)


class CustomInstance(AssetInstance):
    TYPE = 'Custom'

    def __init__(self, custom_info=None, **kwargs):
        self.custom_info = custom_info
        super().__init__(**kwargs)
