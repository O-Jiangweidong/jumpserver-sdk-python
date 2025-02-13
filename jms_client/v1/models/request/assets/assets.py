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
