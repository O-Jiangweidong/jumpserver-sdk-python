from jms_client.v1.models.instance.accounts import (
    AccountInstance, WithTemplateAccountInstance
)
from ..const.account import SecretType, OnInvalidType
from ..common import Request
from ..params import PushParam
from ..mixins import (
    WithIDMixin, ExtraRequestMixin,
    CreateMixin, UpdateMixin, DeleteMixin
)


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
        :param source_id: 账号模板 ID
        :param username: 账号名称
        :param address: 资产地址
        :param node_id: 节点 ID
        :param platform: 资产平台 ID
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


class DetailAccountRequest(WithIDMixin, BaseAccountRequest):
    """ 获取指定 ID 的账号详情 """


class CreateUpdateAccountParamsMixin(object):
    _body: dict

    def __init__(
            self,
            username: str,
            asset: str,
            name: str,
            secret_type: str = SecretType.PASSWORD,
            secret: str = '',
            comment: str = '',
            su_from: str = '',
            is_active: bool = True,
            push_now: bool = False,
            privileged: bool = False,
            push_params: PushParam = None,
            **kwargs
    ):
        """
        :param username: 用户名
        :param asset: 资产 ID
        :param name: 名称
        :param secret_type: 密文类型，支持 password、ssh_key、access_key、token、api_key
        :param secret: 密码
        :param comment: 备注
        :param su_from: 切换自 ID
        :param is_active: 是否激活
        :param privileged: 特权账号
        :param push_params: 推送参数
        :param push_now: 是否推送账号至资产
        """
        super().__init__(**kwargs)
        self._body.update({
            'is_active': is_active, 'username': username, 'name': name,
            'secret_type': SecretType(secret_type), 'asset': asset,
        })
        if isinstance(privileged, bool):
            self._body['privileged'] = privileged
        if isinstance(push_now, bool):
            self._body['push_now'] = push_now
        if isinstance(push_params, PushParam) and push_now:
            self._body['params'] = push_params.get_result()
        if secret:
            self._body['secret'] = secret
        if comment:
            self._body['comment'] = comment
        if su_from:
            self._body['su_from'] = su_from


class CreateAccountRequest(
    CreateUpdateAccountParamsMixin, CreateMixin, BaseAccountRequest
):
    """ 创建账号 """


class UpdateAccountRequest(
    CreateUpdateAccountParamsMixin, UpdateMixin, BaseAccountRequest
):
    """ 更新指定 ID 的账号信息 """


class DeleteAccountRequest(DeleteMixin, BaseAccountRequest):
    """ 删除指定 ID 的账号 """


class ClearAccountSecretRequest(Request):
    """ 清除指定 ID 的账号密码 """
    URL = 'accounts/accounts/clear-secret/'

    def __init__(
            self,
            accounts: list,  # 格式为  ['asset1_id', 'asset2_id']
            **kwargs
    ):
        super().__init__(**kwargs)
        self._body['account_ids'] = accounts

    @staticmethod
    def get_method():
        return 'patch'


class WithTemplateCreateAccountRequest(Request):
    """ 使用账号模板创建账号 """
    URL = 'accounts/accounts/bulk/'
    InstanceClass = WithTemplateAccountInstance

    def __init__(
            self,
            assets: list,  # 格式为 ['asset1_id', 'asset2_id']
            template_id: str,
            is_active: bool = True,
            privileged: bool = False,
            push_now: bool = False,
            secret_type: str = SecretType.PASSWORD,
            on_invalid: str = OnInvalidType.ERROR,
            **kwargs,
    ):
        super().__init__(**kwargs)
        self._body.update({
            'assets': assets, 'template': template_id,
            'secret_type': SecretType(secret_type),
            'on_invalid': OnInvalidType(on_invalid),
        })
        if isinstance(privileged, bool):
            self._body['privileged'] = privileged
        if isinstance(is_active, bool):
            self._body['is_active'] = is_active
        if isinstance(push_now, bool):
            self._body['push_now'] = push_now

    @staticmethod
    def get_method():
        return 'post'
