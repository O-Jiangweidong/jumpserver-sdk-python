from jms_client.v1.models.instance.accounts import AccountTemplateInstance
from ..common import Request
from ..params import SimpleProtocolParam as ProtocolParam, PushParam
from ..mixins import (
    WithIDMixin, ExtraRequestMixin,
    CreateMixin, UpdateMixin, DeleteMixin
)


class BaseAccountTemplateRequest(Request):
    URL = 'accounts/account-templates/'
    InstanceClass = AccountTemplateInstance


class DescribeAccountTemplatesRequest(ExtraRequestMixin, BaseAccountTemplateRequest):
    """ 获取账号模板列表 """

    def __init__(
            self,
            name: str = '',
            username: str = '',
            protocols: ProtocolParam = None,
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称、用户名
        :param name: 名称
        :param username: 用户名
        :param protocols: 协议，根据协议的 secret_type 匹配账号模板的 secret_type 一致的数据
        :param kwargs: 其他参数
        """

        query_params = {}
        if name:
            query_params['name'] = name
        if username:
            query_params['username'] = username
        if isinstance(protocols, ProtocolParam):
            query_params['protocols'] = ','.join(protocols.get_protocols(only_name=True))
        super().__init__(**query_params, **kwargs)


class DetailAccountTemplateRequest(WithIDMixin, BaseAccountTemplateRequest):
    """ 获取指定 ID 的账号详情 """


class SecretParam(object):
    def __init__(self):
        self._result = {
            'secret': '',
            'password_rules': {
                'digit': True, 'symbol': True, 'lowercase': True,
                'uppercase': True, 'length': 16, 'exclude_symbols': ''
            }
        }

    def get_result(self):
        return self._result

    def set_specific_secret(self, secret: str):
        self._result['secret'] = secret
        self._result['secret_strategy'] = 'specific'

    def random_gen_secret(
            self,
            length: int = 16,
            digit: bool = True,
            symbol: bool = True,
            lowercase: bool = True,
            uppercase: bool = True,
            exclude_symbols: str = ''
    ):
        self._result['secret_strategy'] = 'random'
        self._result['password_rules'].update({
            'length': length, 'digit': digit, 'symbol': symbol, 'lowercase': lowercase,
            'uppercase': uppercase, 'exclude_symbols': exclude_symbols
        })


class CreateUpdateAccountTemplateParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            username: str = '',
            privileged: bool = False,
            su_from: str = '',
            secret: SecretParam = None,
            auto_push: bool = False,
            platforms: list = None,
            push_params: PushParam = None,
            comment: str = '',
            **kwargs
    ):
        """
        :param name: 名称
        :param username: 用户名
        :param privileged: 特权账号
        :param su_from: 切换自（从其他账号切换到该账号下），这里写的是其他的账号模板 ID
        :param secret: 密码及策略
        :param auto_push: 是否自动推送
        :param platforms: 平台 ID，只有开启自动推送才有效
        :param push_params: 推送参数
        :param comment: 备注
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self._body.update({
            'name': name, 'username': username, 'privileged': privileged,
        })
        if su_from:
            self._body['su_from'] = su_from
        if isinstance(auto_push, bool):
            self._body['auto_push'] = auto_push
            if isinstance(platforms, list):
                self._body['platforms'] = platforms
        if comment:
            self._body['comment'] = comment
        if isinstance(push_params, PushParams) and auto_push:
            self._body['push_params'] = push_params.get_result()
        if not isinstance(secret, SecretParam):
            secret = SecretParam()
        self._body.update(secret.get_result())


class CreateAccountTemplateRequest(
    CreateUpdateAccountTemplateParamsMixin,  CreateMixin, BaseAccountTemplateRequest
):
    """ 创建账号模板 """


class UpdateAccountTemplateRequest(
    CreateUpdateAccountTemplateParamsMixin, UpdateMixin, BaseAccountTemplateRequest
):
    """ 更新指定 ID 的账号模板信息 """


class DeleteAccountTemplateRequest(DeleteMixin, BaseAccountTemplateRequest):
    """ 删除指定 ID 的账号模板 """


class SyncAccountTemplateInfoRequest(WithIDMixin, Request):
    """ 同步账号模板信息到关联账号 """
    URL = 'accounts/account-templates/{id}/sync-related-accounts/'

    @staticmethod
    def get_method():
        return 'patch'
