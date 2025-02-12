from jms_client.v1.models.instance.assets import (
    AssetInstance, HostInstance, DatabaseInstance, DeviceInstance,
    CloudInstance, WebInstance, GPTInstance, CustomInstance
)
from ..common import Request


class DescribeAssetsRequest(Request):
    URL = 'assets/assets/'
    InstanceClass = AssetInstance


class DeleteAssetRequest(Request):
    URL = 'assets/assets/'

    def get_url(self):
        if not self.instance or not getattr(self.instance, 'id', None):
            raise ValueError(
                'When performing delete action, the parameter [instance] is required'
            )
        return f'{self.url_prefix}{self.URL}{self.instance.id}/'

    def get_method(self):
        return 'delete'


class DescribeHostsRequest(Request):
    URL = 'assets/hosts/'
    InstanceClass = HostInstance


class DescribeDatabasesRequest(Request):
    URL = 'assets/databases/'
    InstanceClass = DatabaseInstance


class DescribeDevicesRequest(Request):
    URL = 'assets/devices/'
    InstanceClass = DeviceInstance


class DescribeCloudsRequest(Request):
    URL = 'assets/clouds/'
    InstanceClass = CloudInstance


class DescribeWebsRequest(Request):
    URL = 'assets/webs/'
    InstanceClass = WebInstance


class DescribeGPTsRequest(Request):
    URL = 'assets/gpts/'
    InstanceClass = GPTInstance


class DescribeCustomsRequest(Request):
    URL = 'assets/customs/'
    InstanceClass = CustomInstance
