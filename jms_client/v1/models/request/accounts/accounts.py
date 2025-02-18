from jms_client.v1.models.instance.accounts import AccountsInstance
from ..common import Request
from ..mixins import (DetailMixin, ExtraRequestMixin)


class BaseAccountRequest(Request):
    URL = 'accounts/accounts/'
    InstanceClass = AccountsInstance


class DescribeAccountsRequest(ExtraRequestMixin, BaseAccountRequest):

    def __init__(
            self,
            asset: str = '',
            source_id: str = '',
            username: str = '',
            address: str = '',
            node_id: str = '',
            platform: str = '',
            category: str = '',
            type_: str = '',
            has_secret: str = '',
            secret_type: str = '',
            **kwargs
    ):
        """
        :param asset: 资产 ID 精确匹配
        :param source_id: 账号来源 ID
        :param username: 账号名称精确匹配
        :param address: 账号绑定的资产 IP 精确匹配
        :param node_id: 节点 ID 精确匹配
        :param platform: 账号绑定的资产平台过滤，支持按照 `平台名称` 或者 `平台 ID` 精确匹配
        :param category: 账号绑定的资产平台类别精确匹配
        :param type_: 账号绑定的资产平台类型精确匹配
        :param secret_type: 密钥类型精确匹配
        :param has_secret: 是否托管密码
        :param kwargs: 其他参数
        """

        query_params = {}
        if asset:
            query_params['asset'] = asset
        if source_id:
            query_params['source_id'] = source_id
        if username:
            query_params['username'] = username
        if address:
            query_params['address'] = address
        if node_id:
            query_params['node_id'] = node_id
        if has_secret:
            query_params['has_secret'] = has_secret
        if platform:
            query_params['platform'] = platform
        if category:
            query_params['category'] = category
        if type_:
            query_params['type'] = type_
        if secret_type:
            query_params['secret_type'] = secret_type
        super().__init__(**query_params, **kwargs)


class DetailAccountRequest(DetailMixin, BaseAccountRequest):
    """ 获取指定 ID 的账号详情 """
