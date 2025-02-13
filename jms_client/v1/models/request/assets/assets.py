from jms_client.v1.models.instance.assets import (
    AssetInstance, HostInstance, DatabaseInstance, DeviceInstance,
    CloudInstance, WebInstance, GPTInstance, CustomInstance
)
from ..common import Request
from ..mixins import DetailMixin


class DescribeAssetsRequest(Request):
    """
    此方法获取的资产是通用类型，顾返回的资产只包含通用类型的字段
    如数据库中的 dbname 则不存在，若想获取不同类型独特的字段，则需要更改请求模型
    如数据库的则为 DescribeDatabasesRequest
    """
    URL = 'assets/assets/'
    InstanceClass = AssetInstance

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
        father_kwargs = {}
        if search:
            father_kwargs['search'] = search
        if platform:
            father_kwargs['platform'] = platform
        if exclude_platform:
            father_kwargs['exclude_platform'] = exclude_platform
        if domain:
            father_kwargs['domain'] = domain
        if type_:
            father_kwargs['type'] = type_
        if category:
            father_kwargs['category'] = category
        if protocols:
            father_kwargs['protocols'] = protocols
        if isinstance(domain_enabled, bool):
            father_kwargs['domain_enabled'] = domain_enabled
        if isinstance(ping_enabled, bool):
            father_kwargs['ping_enabled'] = ping_enabled
        if isinstance(gather_facts_enabled, bool):
            father_kwargs['gather_facts_enabled'] = gather_facts_enabled
        if isinstance(change_secret_enabled, bool):
            father_kwargs['change_secret_enabled'] = change_secret_enabled
        if isinstance(push_account_enabled, bool):
            father_kwargs['push_account_enabled'] = push_account_enabled
        if isinstance(verify_account_enabled, bool):
            father_kwargs['verify_account_enabled'] = verify_account_enabled
        if isinstance(gather_accounts_enabled, bool):
            father_kwargs['gather_accounts_enabled'] = gather_accounts_enabled
        super().__init__(**father_kwargs, **kwargs)


class DetailAssetRequest(DetailMixin, DescribeAssetsRequest):
    """
    此方法获取的资产是通用类型，顾返回的资产只包含通用类型的字段
    如数据库中的 dbname 则不存在，若想获取不同类型独特的字段，则需要更改请求模型
    如数据库的则为 DetailDatabaseRequest
    """


class DeleteAssetRequest(DetailMixin, Request):
    """
    删除指定 ID 的资产
    """
    URL = 'assets/assets/'

    def get_method(self):
        return 'delete'


class DescribeHostsRequest(DescribeAssetsRequest):
    """
    查询资产类型为 主机 的列表
    """
    URL = 'assets/hosts/'
    InstanceClass = HostInstance


class DetailHostRequest(DetailMixin, DescribeHostsRequest):
    """
    查询资产类型为 主机 的详情
    """


class DescribeDatabasesRequest(DescribeAssetsRequest):
    """
    查询资产类型为 数据库 的列表
    """
    URL = 'assets/databases/'
    InstanceClass = DatabaseInstance


class DetailDatabaseRequest(DetailMixin, DescribeDatabasesRequest):
    """
    查询资产类型为 数据库 的详情
    """


class DescribeDevicesRequest(DescribeAssetsRequest):
    """
    查询资产类型为 网络设备 的列表
    """
    URL = 'assets/devices/'
    InstanceClass = DeviceInstance


class DetailDeviceRequest(DetailMixin, DescribeDevicesRequest):
    """
    查询资产类型为 网络设备 的详情
    """


class DescribeCloudsRequest(DescribeAssetsRequest):
    """
    查询资产类型为 云服务 的列表
    """
    URL = 'assets/clouds/'
    InstanceClass = CloudInstance


class DetailCloudRequest(DetailMixin, DescribeCloudsRequest):
    """
    查询资产类型为 云服务 的详情
    """


class DescribeWebsRequest(DescribeAssetsRequest):
    """
    查询资产类型为 Web 的列表
    """
    URL = 'assets/webs/'
    InstanceClass = WebInstance


class DetailWebRequest(DetailMixin, DescribeWebsRequest):
    """
    查询资产类型为 Web 的详情
    """


class DescribeGPTsRequest(DescribeAssetsRequest):
    """
    查询资产类型为 GPT 的列表
    """
    URL = 'assets/gpts/'
    InstanceClass = GPTInstance


class DetailGPTRequest(DetailMixin, DescribeGPTsRequest):
    """
    查询资产类型为 GPT 的详情
    """


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
