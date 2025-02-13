from jms_client.v1.models.instance.assets import (
    AssetInstance, HostInstance, DatabaseInstance, DeviceInstance,
    CloudInstance, WebInstance, GPTInstance, CustomInstance
)
from ..common import Request
from ..mixins import DetailMixin, ExtraRequestMixin


class BaseAssetRequest(Request):
    URL = 'assets/assets/'
    InstanceClass = AssetInstance


class DescribeAssetsRequest(ExtraRequestMixin, BaseAssetRequest):
    """
    此方法获取的资产是通用类型，顾返回的资产只包含通用类型的字段
    如数据库中的 dbname 则不存在，若想获取不同类型独特的字段，则需要更改请求模型
    如数据库的则为 DescribeDatabasesRequest
    """

    def __init__(
            self,
            search: str = '',
            platform: str = '',
            exclude_platform: str = '',
            domain: str = '',
            type_: str = '',
            category: str = '',
            protocols: str = '',
            domain_enabled: bool = None,
            ping_enabled: bool = None,
            gather_facts_enabled: bool = None,
            change_secret_enabled: bool = None,
            push_account_enabled: bool = None,
            verify_account_enabled: bool = None,
            gather_accounts_enabled: bool = None,
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称、地址、备注
        :param platform: 平台过滤，支持按照 `平台名称` 或者 `平台 ID` 精确匹配
        :param exclude_platform: 平台过滤，不包含的平台名称模糊匹配
        :param domain: 网域过滤，支持按照 `网域名称` 模糊匹配，或者 `网域 ID` 精确匹配
        :param type_: 平台类型精确匹配
        :param category: 平台类别精确匹配
        :param protocols: 协议名称精确匹配，多个协议用逗号(,)隔开
        :param domain_enabled: 资产平台中的网域是否启用
        :param ping_enabled: 资产平台中的自动化 - 资产探活是否启用
        :param gather_facts_enabled: 资产平台中的自动化 - 收集资产信息是否启用
        :param change_secret_enabled: 资产平台中的自动化 - 改密是否启用
        :param push_account_enabled: 资产平台中的自动化 - 账号推送是否启用
        :param verify_account_enabled: 资产平台中的自动化 - 账号验证是否启用
        :param gather_accounts_enabled: 资产平台中的自动化 - 账号收集是否启用
        :param kwargs: 其他参数
        """
        query_params = {}
        if search:
            query_params['search'] = search
        if platform:
            query_params['platform'] = platform
        if exclude_platform:
            query_params['exclude_platform'] = exclude_platform
        if domain:
            query_params['domain'] = domain
        if type_:
            query_params['type'] = type_
        if category:
            query_params['category'] = category
        if protocols:
            query_params['protocols'] = protocols
        if isinstance(domain_enabled, bool):
            query_params['domain_enabled'] = domain_enabled
        if isinstance(ping_enabled, bool):
            query_params['ping_enabled'] = ping_enabled
        if isinstance(gather_facts_enabled, bool):
            query_params['gather_facts_enabled'] = gather_facts_enabled
        if isinstance(change_secret_enabled, bool):
            query_params['change_secret_enabled'] = change_secret_enabled
        if isinstance(push_account_enabled, bool):
            query_params['push_account_enabled'] = push_account_enabled
        if isinstance(verify_account_enabled, bool):
            query_params['verify_account_enabled'] = verify_account_enabled
        if isinstance(gather_accounts_enabled, bool):
            query_params['gather_accounts_enabled'] = gather_accounts_enabled
        super().__init__(**query_params, **kwargs)


class DetailAssetRequest(DetailMixin, BaseAssetRequest):
    """
    此方法获取的资产是通用类型，顾返回的资产只包含通用类型的字段
    如数据库中的 dbname 则不存在，若想获取不同类型独特的字段，则需要更改请求模型
    如数据库的则为 DetailDatabaseRequest
    """


class DeleteAssetRequest(DetailMixin, BaseAssetRequest):
    """
    删除指定 ID 的资产
    """

    def get_method(self):
        return 'delete'


class CreateMixin(object):
    _body: dict

    def __init__(
            self,
            id_: str = '',
            **kwargs
    ):
        """
        :param id_: ID
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        if id_:
            self._body['id'] = id_

    def get_url(self):
        url = super().get_url()
        sep = '?' if '?' not in url else '&'
        return f'{url}{sep}platform={self._body.get("platform", "1")}'

    @staticmethod
    def get_method():
        return 'post'


class CreateUpdateAssetParamsMixin(object):
    # TODO 后边搞完账号模型后，再来补充账号相关的内容
    """
        "accounts":[
        {
            "privileged": False,
            "secret_type": "password",
            "push_now": True,
            "on_invalid": "error",
            "is_active": True,
            "name": "hello",
            "username": "hello",
            "params": {
                "push_account_posix": {
                    "modify_sudo": True,
                    "sudo": "/bin/whoami",
                    "shell": "/bin/bash",
                    "home": "/home",
                    "groups": "usergroup"
                }
            },
            "secret": "secret"
            }
        ]
    """

    def __init__(
            self,
            name: str,
            address: str,
            domain: str = '',
            platform: str = '',
            nodes: list = None,
            protocols: list = None,
            labels: list = None,
            is_active: bool = True,
            comment: str = '',
            **kwargs
    ):
        """
        :param name: 名称
        :param address: 地址
        :param domain: 网域 ID
        :param platform: 平台 ID
                :param nodes: 节点 ID 列表, eg: ["node1_id", "node2_id"]
        :param protocols: 协议列表, eg: [{'name': 'ssh', 'port': '22'}]
        :param labels: 标签列表, eg: ["name1:key1", "name2:key2"]
        :param is_active: 是否激活
        :param comment: 备注
        :param kwargs: 其他参数
        """
        self._body = {
            'name': name,
            'address': address,
            'platform': platform,
            'is_active': is_active,
            'comment': comment,
        }
        if domain:
            self._body['domain'] = domain
        if nodes is not None:
            self._body['nodes'] = nodes
        if protocols is not None:
            self._body['protocols'] = protocols
        if labels is not None:
            self._body['labels'] = labels
        super().__init__(**kwargs)

    def get_data(self):
        return self._body


class BaseHostRequest(Request):
    URL = 'assets/hosts/'
    InstanceClass = HostInstance


class DescribeHostsRequest(BaseHostRequest, DescribeAssetsRequest):
    """
    查询资产类型为 主机 的列表
    """


class DetailHostRequest(DetailMixin, BaseHostRequest):
    """
    查询资产类型为 主机 的详情
    """


class CreateHostRequest(
    CreateUpdateAssetParamsMixin, CreateMixin, BaseHostRequest
):
    """ 创建主机 """


class UpdateHostRequest(
    CreateUpdateAssetParamsMixin, DetailMixin, BaseHostRequest
):
    """ 更新主机 """
    def get_method(self):
        return 'put'


class BaseDatabaseRequest(Request):
    URL = 'assets/databases/'
    InstanceClass = DatabaseInstance


class DescribeDatabasesRequest(BaseDatabaseRequest, DescribeAssetsRequest):
    """
    查询资产类型为 数据库 的列表
    """


class DetailDatabaseRequest(DetailMixin, BaseDatabaseRequest):
    """
    查询资产类型为 数据库 的详情
    """


class CreateUpdateDatabaseParamsMixin(CreateUpdateAssetParamsMixin):
    def __init__(
            self,
            db_name: str,
            **kwargs
    ):
        """
            :param db_name: 数据库名称
        """
        super().__init__(**kwargs)
        self._body['db_name'] = db_name


class CreateDatabaseRequest(
    CreateUpdateDatabaseParamsMixin, CreateMixin, BaseDatabaseRequest
):
    """ 创建数据库 """


class UpdateDatabaseRequest(
    CreateUpdateDatabaseParamsMixin, DetailMixin, BaseDatabaseRequest
):
    """ 更新数据库 """
    def get_method(self):
        return 'put'


class BaseDeviceRequest(Request):
    URL = 'assets/devices/'
    InstanceClass = DeviceInstance


class DescribeDevicesRequest(BaseDeviceRequest, DescribeAssetsRequest):
    """
    查询资产类型为 网络设备 的列表
    """


class DetailDeviceRequest(DetailMixin, BaseDeviceRequest):
    """
    查询资产类型为 网络设备 的详情
    """


class CreateDeviceRequest(
    CreateUpdateAssetParamsMixin, CreateMixin, BaseDeviceRequest
):
    """ 创建网络设备 """


class UpdateDeviceRequest(
    CreateUpdateAssetParamsMixin, DetailMixin, BaseDeviceRequest
):
    """ 更新网络设备 """
    def get_method(self):
        return 'put'


class BaseCloudRequest(Request):
    URL = 'assets/clouds/'
    InstanceClass = CloudInstance


class DescribeCloudsRequest(BaseCloudRequest, DescribeAssetsRequest):
    """
    查询资产类型为 云服务 的列表
    """


class DetailCloudRequest(DetailMixin, BaseCloudRequest):
    """
    查询资产类型为 云服务 的详情
    """


class CreateCloudRequest(
    CreateUpdateAssetParamsMixin, CreateMixin, BaseCloudRequest
):
    """ 创建云服务 """


class UpdateCloudRequest(
    CreateUpdateAssetParamsMixin, DetailMixin, BaseCloudRequest
):
    """ 更新云服务 """
    def get_method(self):
        return 'put'


class BaseWebRequest(Request):
    URL = 'assets/webs/'
    InstanceClass = WebInstance


class DescribeWebsRequest(BaseWebRequest, DescribeAssetsRequest):
    """
    查询资产类型为 Web 的列表
    """


class DetailWebRequest(DetailMixin, BaseWebRequest):
    """
    查询资产类型为 Web 的详情
    """


class Script(object):
    def __init__(self):
        self._current_step = 1
        self._script = []

    def add_script(self, value, target, command):
        self._script.append({
            'value': value, 'target': target,
            'command': command, 'step': self._current_step
        })
        self._current_step += 1

    def get_script(self):
        return self._script


class CreateUpdateWebParamsMixin(CreateUpdateAssetParamsMixin):
    def __init__(
            self,
            autofill: str = 'basic',  # 支持 no(禁用代填)、basic(根据选择器代填)、scrit(根据脚本代填)
            username_selector: str = 'name=username',
            password_selector: str = 'name=password',
            submit_selector: str = 'id=login_button',
            script: Script = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self._body.update({
            'autofill': autofill,
            'username_selector': username_selector,
            'password_selector': password_selector,
            'submit_selector': submit_selector,
        })
        if isinstance(script, Script):
            self._body['script'] = script.get_script()


class CreateWebRequest(
    CreateUpdateWebParamsMixin, CreateMixin, BaseWebRequest
):
    """
    创建 Web
    注意：
        Web 类型的资产，协议会根据指定平台自动设置，传递无效
        但是参数必须携带，传递 [{'name': 'http', 'port': '80'}] 即可
    """


class UpdateWebRequest(
    CreateUpdateWebParamsMixin, DetailMixin, BaseWebRequest
):
    """
    更新 Web
    注意：
        Web 类型的资产，协议会根据指定平台自动设置，传递无效，
        但是参数必须携带，传递 [{'name': 'http', 'port': '80'}] 即可
    """
    def get_method(self):
        return 'put'


class BaseGPTRequest(Request):
    URL = 'assets/gpts/'
    InstanceClass = GPTInstance


class DescribeGPTsRequest(BaseGPTRequest, DescribeAssetsRequest):
    """
    查询资产类型为 GPT 的列表
    """


class DetailGPTRequest(DetailMixin, BaseGPTRequest):
    """
    查询资产类型为 GPT 的详情
    """


class CreateUpdateGPTParamsMixin(CreateUpdateAssetParamsMixin):
    def __init__(
            self,
            proxy: str = '',
            **kwargs
    ):
        """
            :param proxy: HTTP(s) 代理
        """
        super().__init__(**kwargs)
        self._body['proxy'] = proxy


class CreateGPTRequest(
    CreateUpdateGPTParamsMixin, CreateMixin, BaseGPTRequest
):
    """ 创建 GPT """


class UpdateGPTRequest(
    CreateUpdateGPTParamsMixin, DetailMixin, BaseGPTRequest
):
    """ 更新 GPT """
    def get_method(self):
        return 'put'


class DescribeCustomsRequest(DescribeAssetsRequest):
    """
    查询资产类型为 自定义资产 的列表
    """
    URL = 'assets/customs/'
    InstanceClass = CustomInstance


class DetailCustomRequest(DetailMixin, DescribeCustomsRequest):
    """
    查询资产类型为 自定义资产 的详情
    """
