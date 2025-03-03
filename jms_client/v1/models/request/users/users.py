from typing import List

from jms_client.const import USER, ORG_USER
from jms_client.v1.models.instance.users import (
    UserInstance, UserProfileInstance, PermUserInstance,
)
from ..const import Source, MFALevel
from ..common import Request
from ..mixins import (
    ExtraRequestMixin, WithIDMixin, CreateMixin,
    DeleteMixin, UpdateMixin,
)


__all__ = [
    'CreateUserRequest', 'UpdateUserRequest', 'DeleteUserRequest',
    'DescribeUsersRequest', 'DetailUserRequest', 'UserProfileRequest',
    'DescribeAuthorizedUsersForAssetRequest', 'RemoveUserRequest',
    'DescribeUsersForPermissionRequest',
    'InviteUserRequest',
    'AuthStrategyParam',
]


class BaseUserRequest(Request):
    URL = 'users/users/'
    InstanceClass = UserInstance


class DescribeUsersRequest(ExtraRequestMixin, BaseUserRequest):
    """ 获取用户列表 """
    def __init__(
            self,
            id_: str = '',
            name: str = '',
            username: str = '',
            email: str = '',
            group_id: str = '',
            groups: str = '',
            exclude_group_id: str = '',
            source: str = '',
            org_roles: str = '',
            system_roles: str = '',
            is_active: bool = None,
            **kwargs
    ):
        """
        :param search: 条件搜索，支持用户名、邮箱、名称
        :param id: ID
        :param name: 名称
        :param username: 用户名
        :param email: 邮箱
        :param group_id: 用户组 ID
        :param groups: 用户组名称
        :param exclude_group_id: 排除此用户组 ID 的其他用户
        :param source: 来源
        :param org_roles: 组织角色 ID/名称
        :param system_roles: 系统角色 ID/名称
        :param is_active: 是否激活
        :param kwargs: 其他参数
        """
        query_params = {}
        if id_:
            query_params['id'] = id_
        if name:
            query_params['name'] = name
        if username:
            query_params['username'] = username
        if email:
            query_params['email'] = email
        if group_id:
            query_params['group_id'] = group_id
        if groups:
            query_params['groups'] = groups
        if exclude_group_id:
            query_params['exclude_group_id'] = exclude_group_id
        if source:
            query_params['source'] = source
        if org_roles:
            query_params['org_roles'] = org_roles
        if system_roles:
            query_params['system_roles'] = system_roles
        if is_active is not None:
            query_params['is_active'] = is_active
        super().__init__(**query_params, **kwargs)


class DetailUserRequest(WithIDMixin, BaseUserRequest):
    """ 获取用户详情 """


class AuthStrategyParam(object):
    def __init__(self):
        self._result = {}
        self.set_reset_email()

    def get_strategy(self):
        return self._result

    def set_reset_email(self):
        self._result['password_strategy'] = 'email'

    def set_password(self, password, need_update=False):
        self._result.update({
            'password_strategy': 'custom', 'password': password,
            'need_update_password': need_update
        })


class CreateUpdateUserParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            username: str,
            email: str,
            comment: str = '',
            groups: List = None,
            mfa_level: str = None,
            source: str = None,
            is_active: bool = True,
            system_roles: List = None,
            org_roles: List = None,
            date_expired: str = None,
            phone: str = None,
            wechat: str = None,
            auth_strategy: AuthStrategyParam = None,
            **kwargs
    ):
        """
        :param name: 名称
        :param username: 用户名
        :param email: 邮箱
        :param comment: 备注
        :param groups: 用户组 ID
        :param mfa_level: MFA
        :param source: 来源
        :param is_active: 是否激活
        :param system_roles: 系统角色 ID
        :param org_roles: 组织角色 ID
        :param date_expired: 过期时间
        :param phone: 手机号
        :param wechat: 微信
        :param auth_strategy: 认证策略
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self._body.update({
            'name': name, 'username': username, 'email': email, 'comment': comment,
        })
        if date_expired:
            self._body['date_expired'] = date_expired
        if phone:
            self._body['phone'] = phone
        if wechat:
            self._body['wechat'] = wechat
        if isinstance(groups, list):
            self._body['groups'] = groups
        if isinstance(is_active, bool):
            self._body['is_active'] = is_active
        if isinstance(system_roles, list):
            self._body['system_roles'] = system_roles
        else:
            self._body['system_roles'] = [USER]
        if isinstance(org_roles, list):
            self._body['org_roles'] = org_roles
        else:
            self._body['org_roles'] = [ORG_USER]

        self._body['mfa_level'] = mfa_level or MFALevel.DISABLED
        self._body['source'] = source or Source.LOCAL
        if not isinstance(auth_strategy, AuthStrategyParam):
            auth_strategy = AuthStrategyParam()
        self._body.update(auth_strategy.get_strategy())


class CreateUserRequest(
    CreateUpdateUserParamsMixin, CreateMixin, BaseUserRequest
):
    """ 创建 用户 """


class UpdateUserRequest(
    CreateUpdateUserParamsMixin, UpdateMixin, BaseUserRequest
):
    """ 更新 用户 """
    def __init__(
            self,
            public_key: str = '',
            **kwargs
    ):
        super().__init__(**kwargs)
        if public_key:
            self._body['set_public_key'] = True
            self._body['public_key'] = public_key


class DeleteUserRequest(DeleteMixin, BaseUserRequest):
    """ 删除指定 ID 的用户 """


class UserProfileRequest(Request):
    URL = 'users/profile/'
    InstanceClass = UserProfileInstance


class InviteUserRequest(CreateMixin, Request):
    URL = 'users/users/invite/'

    def __init__(
            self,
            org_roles: List,
            users: List,
            **kwargs
    ):
        """
        :param org_roles: 组织角色列表，格式为 ['role1_id', 'role2_id']
        :param users: 用户列表，格式为 ['user1_id', 'user2_id']
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self._body.update({
            'org_roles': org_roles, 'users': users
        })

    def get_method(self):
        return 'post'


class RemoveUserRequest(WithIDMixin, Request):
    """ 从某个组中中移除用户【非删除】 """
    URL = 'users/users/{id}/remove/'
    
    @staticmethod
    def get_method():
        return 'post'


class DescribeAuthorizedUsersForAssetRequest(ExtraRequestMixin, WithIDMixin, BaseUserRequest):
    """ 获取指定资产被授权的用户列表"""
    URL = 'assets/assets/{id}/perm-users/'

    def __init__(
            self,
            asset_id: str,
            **kwargs
    ):
        """
        :param asset_id: 资产 ID
        :param kwargs: 其他参数
        """
        super().__init__(id_=asset_id, **kwargs)


class DescribeUsersForPermissionRequest(WithIDMixin, Request):
    """ 获取指定授权下的用户 """
    URL = 'perms/asset-permissions/{id}/users/all/'
    InstanceClass = PermUserInstance
