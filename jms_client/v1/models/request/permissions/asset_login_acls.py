import re

from jms_client.v1.models.instance.permissions import AssetLoginACLInstance
from ..const import ACLAction
from ..common import (
    Request, PriorityParam, AccountParam, RuleParam,
    UserManyFilterParam, AssetManyFilterParam,
)
from ..mixins import (
    WithIDMixin, CreateMixin, DeleteMixin, UpdateMixin, ExtraRequestMixin
)


class BaseAssetLoginACLRequest(Request):
    URL = 'acls/login-asset-acls/'
    InstanceClass = AssetLoginACLInstance


class DescribeAssetLoginACLsRequest(ExtraRequestMixin, BaseAssetLoginACLRequest):
    """ 查询资产登陆 ACL 列表 """

    def __init__(
            self,
            name: str = '',
            users: str = '',
            assets: str = '',
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称
        :param name: 名称
        :param users: 用户，支持用户 ID、用户名、名称
        :param assets: 资产，支持资产 ID、名称、地址
        :param kwargs: 其他参数
        """
        query_params = {}
        if name:
            query_params['name'] = name
        if users:
            query_params['users'] = users
        if assets:
            query_params['assets'] = assets
        super().__init__(**query_params, **kwargs)


class DetailAssetLoginACLRequest(WithIDMixin, BaseAssetLoginACLRequest):
    """ 获取指定 ID 的资产登录 ACL 详情 """


class CreateUpdateAssetLoginACLParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            comment: str = '',
            action: str = ACLAction.REJECT,
            is_active: bool = True,
            priority: int = 50,
            reviewers: list = None,
            rules: RuleParam = None,
            accounts: AccountParam = None,
            users: UserManyFilterParam = None,
            assets: AssetManyFilterParam = None,
            **kwargs
    ):
        """
        :param name: 名称
        :param comment: 备注
        :param action: 动作，支持 reject、accept、review、notice
        :param is_active: 是否激活
        :param priority: 优先级, 1-100
        :param reviewers: 审批人
        :param rules: 规则（IP 组、时段限制）
        :param accounts: 受控制的账号
        :param assets: 受控制的资产
        :param users: 受控制的人
        """
        super().__init__(**kwargs)
        self._body.update({
            'name': name, 'is_active': is_active, 'action': ACLAction(action),
            'priority': PriorityParam(priority),
        })
        if action in (ACLAction.REVIEW, ACLAction.NOTICE) and not reviewers:
            raise ValueError('reviewers can not be empty')
        if int(priority) < 0 or int(priority) > 100:
            raise ValueError('priority must be in [0-100]')
        if comment:
            self._body['comment'] = comment
        if isinstance(reviewers, list):
            self._body['reviewers'] = reviewers
        if isinstance(accounts, AccountParam):
            self._body['accounts'] = accounts.get_accounts()
        if not isinstance(assets, AssetManyFilterParam):
            assets = AssetManyFilterParam()
        if not isinstance(rules, RuleParam):
            rules = RuleParam()
        if not isinstance(users, UserManyFilterParam):
            users = UserManyFilterParam()
        self._body['assets'] = assets.get_result()
        self._body['rules'] = rules.get_rule()
        self._body['users'] = users.get_result()


class CreateAssetLoginACLRequest(
    CreateUpdateAssetLoginACLParamsMixin, CreateMixin, BaseAssetLoginACLRequest
):
    """ 创建资产登陆 ACL """


class UpdateAssetLoginACLRequest(
    CreateUpdateAssetLoginACLParamsMixin, UpdateMixin, BaseAssetLoginACLRequest
):
    """ 更新指定 ID 的资产登录 ACL 属性 """


class DeleteAssetLoginACLRequest(DeleteMixin, BaseAssetLoginACLRequest):
    """ 删除指定 ID 的资产登录 ACL """
