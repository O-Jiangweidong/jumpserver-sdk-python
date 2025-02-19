from jms_client.v1.models.instance.accounts import AccountInstance
from ..common import Request
from ..mixins import (DetailMixin, ExtraRequestMixin)


class BaseAccountRequest(Request):
    URL = 'accounts/accounts/'
    InstanceClass = AccountInstance


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
            has_secret: bool = None,
            secret_type: str = '',
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称、备注、用户名、资产名称、资产地址
        :param asset: 资产 ID
        :param source_id: 创建该账号所使用的模板 ID
        :param username: 账号名称精确匹配
        :param address: 资产地址
        :param node_id: 节点 ID
        :param platform: 资产平台过滤，支持按照平台 ID 查询
        :param category: 资产平台类别
        :param type_: 资产平台类型
        :param secret_type: 密钥类型
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
        if isinstance(has_secret, bool):
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
