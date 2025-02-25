from jms_client.v1.models.instance.users import UserGroupInstance
from ..common import Request
from ..mixins import (
    ExtraRequestMixin, WithIDMixin, CreateMixin,
    DeleteMixin, UpdateMixin,
)

__all__ = [
    'DescribeUserGroupsRequest', 'DetailUserGroupRequest',
    'CreateUserGroupRequest', 'UpdateUserGroupRequest',
    'DeleteUserGroupRequest', 'AppendUserToGroupRequest',
    'RemoveUserFromGroupRequest', 'AppendAllUserToGroupRequest'
]


class BaseUserGroupRequest(Request):
    URL = 'users/groups/'
    InstanceClass = UserGroupInstance


class DescribeUserGroupsRequest(ExtraRequestMixin, BaseUserGroupRequest):
    """ 获取用户组列表 """
    def __init__(
            self,
            name: str = '',
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称
        :param name: 名称
        :param kwargs: 其他参数
        """
        query_params = {}
        if name:
            query_params['name'] = name
        super().__init__(**query_params, **kwargs)


class DetailUserGroupRequest(WithIDMixin, BaseUserGroupRequest):
    """ 获取用户组详情 """


class CreateUpdateUserGroupParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            users: list = None,
            comment: str = '',
            **kwargs
    ):
        """
        :param name: 名称
        :param users: 用户列表，格式为 ['user1_id', 'user2_id']
        :param comment: 备注
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self._body.update({
            'name': name,  'comment': comment,
        })
        if users is not None:
            self._body['users'] = users


class CreateUserGroupRequest(
    CreateUpdateUserGroupParamsMixin, CreateMixin, BaseUserGroupRequest
):
    """ 创建 用户组 """


class UpdateUserGroupRequest(
    CreateUpdateUserGroupParamsMixin, UpdateMixin, BaseUserGroupRequest
):
    """ 更新 用户组 """


class DeleteUserGroupRequest(DeleteMixin, BaseUserGroupRequest):
    """ 删除指定 ID 的用户组 """


class BaseRelationRequest(Request):
    URL = 'users/users-groups-relations/'


class AppendUserToGroupRequest(BaseRelationRequest):
    """ 向指定用户组批量添加用户 """
    def __init__(
            self,
            users: list,
            group_id: str,
            **kwargs
    ):
        """
        :param users: 用户 ID，格式 ['user1_id', 'user2_id']
        :param group_id: 用户组 ID
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self._body = [{'user': u, 'usergroup': group_id} for u in users]

    @staticmethod
    def get_method():
        return 'post'


class RemoveUserFromGroupRequest(BaseRelationRequest):
    """ 从用户组移除用户 """
    def __init__(
            self,
            user_id: str,
            group_id: str,
            **kwargs
    ):
        """
        :param user_id: 用户 ID
        :param group_id: 用户组 ID
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self.other.update({'user': user_id, 'usergroup': group_id})

    @staticmethod
    def get_method():
        return 'delete'


class AppendAllUserToGroupRequest(WithIDMixin, Request):
    """ 向指定用户组添加所有用户（当前组织下的用户） """
    URL = 'users/groups/{id}/add-all-users/'

    def __init__(
            self,
            group_id: str,
            **kwargs
    ):
        """
        :param group_id: 用户组 ID
        :param kwargs: 其他参数
        """
        super().__init__(id_=group_id, **kwargs)

    @staticmethod
    def get_method():
        return 'post'
