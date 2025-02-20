import re

from jms_client.v1.models.instance.permissions import UserLoginACLInstance
from ..const import UserLoginACLAction as LoginACLAction
from ..common import Request
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


class UserParam(object):
    def __init__(self):
        self._users = {}
        self.set_all_users()

    def get_users(self):
        return self._users

    def set_all_users(self):
        self._users = {'type': 'all', 'username_group': ''}

    def set_specify_users(self, users: list):
        """
        :param users: 指定用户，格式为 ['user1_id', 'user2_id']
        """
        self._users = {'type': 'ids', 'ids': users}

    def set_attr_users(self, attrs: list):
        """
        :param attrs: 指定用户属性，格式为 [{'name': '', 'match': '', 'value': ''}]
            以下为 'name' 为某个属性时，match 支持的内容 及 value 的内容格式
            name: 用户名称、value: 值、match：
                in：在...中
                exact：等于
                not：不等于
                contains：包含
                startswith：以...开头
                endswith：以...结尾
                regex：正则表达式
            username: 用户名、value: 值、match：同上方 name 的 match 取值
            email: 邮箱、value: 值、match：同上方 name 的 match 取值
            comment: 备注、value: 值、match：同上方 name 的 match 取值
            is_active: 是否激活、value: True/False、match：
                exact：等于
                not：不等于
            is_first_login: 是否首次登录、value: True/False、match：同上方 is_active 的 match 取值
            system_roles: 系统角色、value: ['id1', 'id2']、match：
                m2m: 任意包含
                m2m_all: 同时包含
            org_roles: 组织角色、value: ['id1', 'id2']、match：同上方 system_roles 的 match 取值
            groups: 组、value: ['id1', 'id2']、match：同上方 system_roles 的 match 取值
        """
        str_match = ('in', 'exact', 'not', 'contains', 'startswith', 'endswith', 'regex')
        bool_match = ('exact', 'not')
        m2m_match = ('m2m', 'm2m_all')
        attr_rule_map = {
            'name': {'match': str_match}, 'username': {'match': str_match},
            'email': {'match': str_match}, 'comment': {'match': str_match},
            'is_active': {'match': bool_match}, 'is_first_login': {'match': bool_match},
            'system_roles': {'match': m2m_match}, 'org_roles': {'match': m2m_match},
            'groups': {'match': m2m_match},
        }
        for attr in attrs:
            name = attr.get('name')
            if not name or name not in attr_rule_map.keys():
                raise ValueError(f'Param attrs item name must be in {attr_rule_map.keys()}')

            match_value = attr.get('match', '')
            match_rule = attr_rule_map[name]['match']
            if match_value not in match_rule:
                raise ValueError(f'Param attrs [{name}] match must be in {match_rule}')
        self._users = {'type': 'attrs', 'attrs': attrs}


class CreateUpdateUserLoginACLParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            comment: str = '',
            action: str = LoginACLAction.REJECT,
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
        :param reviewers: 审批人，支持用户 ID、用户名、名称
        :param rules: 规则（IP 组、时段限制）
        :param users: 通知人，格式为 ['user1_id', 'user2_id']
        """
        super().__init__(**kwargs)
        self._body.update({
            'name': name, 'is_active': is_active, 'priority': priority,
            'action': LoginACLAction(action),
        })
        if action in (LoginACLAction.REVIEW, LoginACLAction.NOTICE) and not reviewers:
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
