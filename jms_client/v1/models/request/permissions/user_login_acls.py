import re

from jms_client.v1.models.instance.permissions import UserLoginACLInstance
from ..const import ACLAction
from ..common import Request, UserParam
from ..mixins import (
    DetailMixin, CreateMixin, DeleteMixin, UpdateMixin, ExtraRequestMixin
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


class DetailUserLoginACLRequest(DetailMixin, BaseUserLoginACLRequest):
    """ 获取指定 ID 的用户登录 ACL 详情 """


class RuleParam(object):
    def __init__(self):
        self._time_pattern = re.compile(
            r'^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])~(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$'
        )
        self._time_period = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        self._rule = {'ip_group': ['*']}

    def get_rule(self):
        self._rule['time_period'] = [
            {'id': k, 'value': '、'.join(v)} for k, v in self._time_period.items()
        ]
        return self._rule

    def set_ip_group(self, ip_groups: list):
        self._rule['ip_group'] = ip_groups

    def set_time_period(self, weeks: list[int], time_periods: list):
        """
        :param weeks: 星期，取值范围 0-6、分别代表星期日至星期六
        :param time_periods: 时间段，元素格式为 00:00~00:00
        """
        for week in weeks:
            if week not in self._time_period.keys():
                raise ValueError('week must be in [0-6]')

        for time_period in time_periods:
            if not self._time_pattern.match(time_period):
                raise ValueError('time_period must be in format 00:00~00:00')
            for week in weeks:
                self._time_period[week].append(time_period)


class CreateUpdateUserLoginACLParamsMixin(object):
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
            users: UserParam = None,
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
            'name': name, 'is_active': is_active, 'priority': priority,
            'action': ACLAction(action),
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
        if not isinstance(users, UserParam):
            users = UserParam()
        self._body['rules'] = rules.get_rule()
        self._body['users'] = users.get_users()


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
