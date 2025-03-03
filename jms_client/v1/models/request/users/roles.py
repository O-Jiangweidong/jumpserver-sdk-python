from typing import List

from jms_client.v1.models.instance.users import RoleInstance, RoleUserInstance
from ..common import Request
from ..mixins import (
    ExtraRequestMixin, WithIDMixin, CreateMixin,
    DeleteMixin, UpdateMixin,
)


class BaseRoleRequest(Request):
    URL = 'rbac/roles/'
    InstanceClass = RoleInstance


class DescribeRolesRequest(ExtraRequestMixin, BaseRoleRequest):
    """ 获取角色列表 """
    def __init__(
            self,
            name: str = '',
            scope: str = '',
            builtin: bool = None,
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称
        :param name: 名称
        :param scope: 范围，取值 system/org
        :param builtin: 是否内置
        :param kwargs: 其他参数
        """
        query_params = {}
        if name:
            query_params['name'] = name
        if scope:
            query_params['scope'] = scope
        if builtin is not None:
            query_params['builtin'] = builtin
        super().__init__(**query_params, **kwargs)


class DetailRoleRequest(WithIDMixin, BaseRoleRequest):
    """ 获取角色详情 """


class CreateUpdateRoleParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            scope: str = 'system',
            comment: str = '',
            **kwargs
    ):
        """
        :param name: 名称
        :param scope: 范围，取值 system/org
        :param comment: 备注
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self._body.update({
            'name': name,  'comment': comment, 'scope': scope
        })


class CreateRoleRequest(
    CreateUpdateRoleParamsMixin, CreateMixin, BaseRoleRequest
):
    """ 创建 系统角色 """


class UpdateRoleRequest(
    CreateUpdateRoleParamsMixin, UpdateMixin, BaseRoleRequest
):
    """ 更新 角色 """


class DeleteRoleRequest(DeleteMixin, BaseRoleRequest):
    """ 删除指定 ID 的角色 """


class BaseRoleRelationRequest(Request):
    InstanceClass = RoleUserInstance

    def __init__(
            self,
            scope: str = '',
            **kwargs
    ):
        """
        :param scope: 范围，取值 system/org
        """
        self.URL = f'rbac/{scope}-role-bindings/'
        super().__init__(**kwargs)


class DescribeUsersWithRoleRequest(ExtraRequestMixin, BaseRoleRelationRequest):
    def __init__(
            self,
            role_id: str,
            **kwargs
    ):
        """
        :param role_id: 角色 ID
        :param kwargs: 其他参数
        """
        super().__init__(role=role_id, **kwargs)


class AppendUsersToRoleRequest(BaseRoleRelationRequest):
    """ 向指定角色批量添加用户 """
    def __init__(
            self,
            users: List,
            role_id: str,
            **kwargs
    ):
        """
        :param users: 用户 ID，格式 ['user1_id', 'user2_id']
        :param role_id: 用户角色 ID
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        scope = kwargs.get('scope')
        self._body = [{'user': u, 'role': role_id, 'scope': scope} for u in users]

    @staticmethod
    def get_method():
        return 'post'


class RemoveUserFromRoleRequest(DeleteMixin, BaseRoleRelationRequest):
    """ 从角色移除用户 """
    def __init__(
            self,
            relation_id: str,
            role_id: str,
            **kwargs
    ):
        """
        :param relation_id: 用户和角色的关联 ID
        :param role_id: 角色 ID
        :param kwargs: 其他参数
        """
        super().__init__(id_=relation_id, role=role_id, **kwargs)
