from jms_client.v1.models.instance.users import RoleInstance
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
