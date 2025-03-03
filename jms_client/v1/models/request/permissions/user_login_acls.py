from typing import List

from jms_client.v1.models.instance.permissions import UserLoginACLInstance
from ..const import ACLAction
from ..common import Request
from ..params import UserManyFilterParam, PriorityParam, RuleParam
from ..mixins import (
    WithIDMixin, CreateMixin, DeleteMixin, UpdateMixin, ExtraRequestMixin
)


class BaseUserLoginACLRequest(Request):
    URL = 'acls/login-acls/'
    InstanceClass = UserLoginACLInstance


class DescribeUserLoginACLsRequest(ExtraRequestMixin, BaseUserLoginACLRequest):
    """ 查询用户登陆 ACL 列表 """

    def __init__(
            self,
            name: str = '',
            action: str = '',
            user: str = '',
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称
        :param name: 名称
        :param action: 动作，支持 reject、accept、review、notice
        :param user: 用户，支持用户 ID、用户名、名称
        :param kwargs: 其他参数
        """
        query_params = {}
        if name:
            query_params['name'] = name
        if action:
            query_params['action'] = action
        if user:
            query_params['users'] = user
        super().__init__(**query_params, **kwargs)


class DetailUserLoginACLRequest(WithIDMixin, BaseUserLoginACLRequest):
    """ 获取指定 ID 的用户登录 ACL 详情 """


class CreateUpdateUserLoginACLParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            comment: str = '',
            action: str = ACLAction.REJECT,
            is_active: bool = True,
            priority: int = 50,
            reviewers: List = None,
            rules: RuleParam = None,
            users: UserManyFilterParam = None,
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
        if not isinstance(rules, RuleParam):
            rules = RuleParam()
        if not isinstance(users, UserManyFilterParam):
            users = UserManyFilterParam()
        self._body['rules'] = rules.get_rule()
        self._body['users'] = users.get_result()


class CreateUserLoginACLRequest(
    CreateUpdateUserLoginACLParamsMixin, CreateMixin, BaseUserLoginACLRequest
):
    """ 创建用户登陆 ACL """


class UpdateUserLoginACLRequest(
    CreateUpdateUserLoginACLParamsMixin, UpdateMixin, BaseUserLoginACLRequest
):
    """ 更新指定 ID 的用户登录 ACL 属性 """


class DeleteUserLoginACLRequest(DeleteMixin, BaseUserLoginACLRequest):
    """ 删除指定 ID 的用户登录 ACL """
