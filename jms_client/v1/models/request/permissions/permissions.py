from jms_client.v1.models.instance.permissions import (
    PermissionInstance
)
from jms_client.v1.utils import handle_range_datetime
from ..common import Request, AccountParam, SimpleProtocolParam
from ..mixins import (
    WithIDMixin, CreateMixin, DeleteMixin,
    UpdateMixin, ExtraRequestMixin
)


__all__ = [
    'CreatePermissionRequest', 'UpdatePermissionRequest', 'DeletePermissionRequest',
    'DescribePermissionsRequest', 'DetailPermissionRequest',
    'DescribePermsForAssetAndUserRequest', 'DescribePermsForAssetAndUserGroupRequest',
    'AppendUsersToPermissionRequest', 'RemoveUserFromPermissionRequest',
    'AppendUserGroupsToPermissionRequest', 'RemoveUserGroupFromPermissionRequest',
    'AppendAssetsToPermissionRequest', 'RemoveAssetFromPermissionRequest',
    'AppendNodesToPermissionRequest', 'RemoveNodeFromPermissionRequest',
    'ActionParam', 'ProtocolParam',
]


class BasePermissionRequest(Request):
    URL = 'perms/asset-permissions/'
    InstanceClass = PermissionInstance


class DescribePermissionsRequest(ExtraRequestMixin, BasePermissionRequest):
    """ 查询授权列表 """

    def __init__(
            self,
            is_effective: bool = None,
            node_id: str = '',
            node_name: str = '',
            asset_id: str = '',
            asset_name: str = '',
            user_id: str = '',
            username: str = '',
            all_: bool = None,
            is_valid: bool = None,
            address: str = '',
            accounts: str = '',
            user_group_id: str = '',
            user_group: str = '',
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称
        :param is_effective: 全部属性是否都设置，如用户、用户组、资产、节点等配置项
        :param node_id: 根据节点 ID 过滤
        :param node_name: 根据节点名称过滤
        :param asset_id: 根据授权的资产 ID 过滤
        :param asset_name: 根据授权的资产名称过滤
        :param user_id: 根据授权的用户 ID 过滤
        :param username: 根据授权的用户名称过滤
        :param all_: 在 node_id、 node_name、asset_id、asset_name、address、user_id、username 配置的基础上，额外过滤功能。
                        当值为 True 时，搜索当前节点的授权，当值为 False 时，同时搜索当前节点和祖先节点的授权
        :param is_valid: 是否有效
        :param address: 根据授权的资产地址过滤
        :param accounts: 根据授权的账号进行过滤，多个账号间用逗号（,）隔开
        :param user_group_id: 根据授权的用户组 ID 过滤
        :param user_group: 根据授权的用户组名称过滤
        :param kwargs: 其他参数
        """
        query_params = {}
        if isinstance(is_effective, bool):
            query_params['is_effective'] = is_effective
        if node_id:
            query_params['node_id'] = node_id
        if node_name:
            query_params['node_name'] = node_name
        if asset_id:
            query_params['asset_id'] = asset_id
        if asset_name:
            query_params['asset_name'] = asset_name
        if user_id:
            query_params['user_id'] = user_id
        if username:
            query_params['username'] = username
        if isinstance(all_, bool):
            query_params['all'] = all_
        if isinstance(is_valid, bool):
            query_params['is_valid'] = is_valid
        if address:
            query_params['address'] = address
        if accounts:
            query_params['accounts'] = accounts
        if user_group_id:
            query_params['user_group_id'] = user_group_id
        if user_group:
            query_params['user_group'] = user_group
        super().__init__(**query_params, **kwargs)


class DetailPermissionRequest(WithIDMixin, BasePermissionRequest):
    """ 获取指定 ID 的授权详情 """


class ActionParam(object):
    CONNECT = 'connect'
    UPLOAD = 'upload'
    DOWNLOAD = 'download'
    COPY = 'copy'
    PASTE = 'paste'
    DELETE = 'delete'
    SHARE = 'share'

    def __init__(self):
        self._actions = []

    def get_actions(self):
        return self._actions

    def set_all(self):
        self._actions.extend([
            self.CONNECT, self.UPLOAD, self.DOWNLOAD, self.COPY,
            self.PASTE, self.DELETE, self.SHARE,
        ])

    def set_file_transfer(self):
        self._actions.extend([
            self.UPLOAD, self.DOWNLOAD, self.DELETE,
        ])

    def set_clipboard(self):
        self._actions.extend([self.COPY, self.PASTE])


class ProtocolParam(SimpleProtocolParam):
    def append_all(self):
        self._protocols = [{'name': 'all'}]


class CreateUpdatePermissionParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            date_start: str = '',  # 2025-02-17 02:01:57
            date_expired: str = '',  # 2025-02-17 02:01:57
            is_active: bool = True,
            users: list = None,
            assets: list = None,
            nodes: list = None,
            user_groups: list = None,
            accounts: AccountParam = None,
            actions: ActionParam = None,
            protocols: ProtocolParam = None,
            comment: str = '',
            **kwargs
    ):
        """
        :param name: 名称
        """
        super().__init__(**kwargs)
        date_start, date_expired = handle_range_datetime(date_start, date_expired)
        self._body.update({
            'name': name, 'is_active': is_active,
            'date_start': date_start, 'date_expired': date_expired,
        })
        if users is not None:
            self._body['users'] = users
        if assets is not None:
            self._body['assets'] = assets
        if nodes is not None:
            self._body['nodes'] = nodes
        if user_groups is not None:
            self._body['user_groups'] = user_groups
        if isinstance(accounts, AccountParam):
            self._body['accounts'] = accounts.get_accounts()
        if isinstance(actions, ActionParam):
            self._body['actions'] = actions.get_actions()
        if isinstance(protocols, ProtocolParam):
            self._body['protocols'] = protocols.get_protocols(only_name=True)
        if comment:
            self._body['comment'] = comment


class CreatePermissionRequest(
    CreateUpdatePermissionParamsMixin, CreateMixin, BasePermissionRequest
):
    """ 创建授权 """


class UpdatePermissionRequest(
    CreateUpdatePermissionParamsMixin, UpdateMixin, BasePermissionRequest
):
    """ 更新指定 ID 的授权属性 """


class DeletePermissionRequest(DeleteMixin, BasePermissionRequest):
    """ 删除指定 ID 的授权 """


class DescribePermsForAssetAndUserRequest(DescribePermissionsRequest):
    """ 获取指定资产及用户被授权的授权列表"""
    URL = 'assets/assets/{asset_id}/perm-users/{user_id}/permissions/'

    def __init__(
            self,
            asset_id: str,
            user_id: str,
            **kwargs
    ):
        """
        :param asset_id: 资产 ID
        :param user_id: 用户 ID
        :param kwargs: 其他参数
        """
        self.URL = self.URL.format(asset_id=asset_id, user_id=user_id)
        super().__init__(**kwargs)


class DescribePermsForAssetAndUserGroupRequest(DescribePermissionsRequest):
    """ 获取指定资产及用户组被授权的授权列表"""
    URL = 'assets/assets/{asset_id}/perm-user-groups/{user_group_id}/permissions/'

    def __init__(
            self,
            asset_id: str,
            user_group_id: str,
            **kwargs
    ):
        """
        :param asset_id: 资产 ID
        :param user_group_id: 用户组 ID
        :param kwargs: 其他参数
        """
        self.URL = self.URL.format(asset_id=asset_id, user_group_id=user_group_id)
        super().__init__(**kwargs)


class BaseUserRelationRequest(Request):
    URL = 'perms/asset-permissions-users-relations/'


class AppendUsersToPermissionRequest(BaseUserRelationRequest):
    """ 向指定授权批量添加用户 """
    def __init__(
            self,
            users: list,
            permission_id: str,
            **kwargs
    ):
        """
        :param users: 用户 ID，格式 ['user1_id', 'user2_id']
        :param permission_id: 授权 ID
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self._body = [{'user': u, 'assetpermission': permission_id} for u in users]

    @staticmethod
    def get_method():
        return 'post'


class RemoveUserFromPermissionRequest(BaseUserRelationRequest):
    """ 从授权移除用户 """
    def __init__(
            self,
            user_id: str,
            permission_id: str,
            **kwargs
    ):
        """
        :param user_id: 用户 ID
        :param permission_id: 授权 ID
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self.other.update({'user': user_id, 'assetpermission': permission_id})

    @staticmethod
    def get_method():
        return 'delete'


class BaseUserGroupRelationRequest(Request):
    URL = 'perms/asset-permissions-user-groups-relations/'


class AppendUserGroupsToPermissionRequest(BaseUserGroupRelationRequest):
    """ 向指定授权批量添加用户组 """
    def __init__(
            self,
            user_groups: list,
            permission_id: str,
            **kwargs
    ):
        """
        :param user_groups: 用户组 ID，格式 ['user_group1_id', 'user_group2_id']
        :param permission_id: 授权 ID
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self._body = [{'usergroup': ug, 'assetpermission': permission_id} for ug in user_groups]

    @staticmethod
    def get_method():
        return 'post'


class RemoveUserGroupFromPermissionRequest(BaseUserGroupRelationRequest):
    """ 从授权移除用户组 """
    def __init__(
            self,
            user_group_id: str,
            permission_id: str,
            **kwargs
    ):
        """
        :param user_group_id: 用户组 ID
        :param permission_id: 授权 ID
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self.other.update({'usergroup': user_group_id, 'assetpermission': permission_id})

    @staticmethod
    def get_method():
        return 'delete'


class BaseAssetRelationRequest(Request):
    URL = 'perms/asset-permissions-assets-relations/'


class AppendAssetsToPermissionRequest(BaseAssetRelationRequest):
    """ 向指定授权批量添加资产 """
    def __init__(
            self,
            assets: list,
            permission_id: str,
            **kwargs
    ):
        """
        :param assets: 资产 ID，格式 ['asset1_id', 'asset2_id']
        :param permission_id: 授权 ID
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self._body = [{'asset': a, 'assetpermission': permission_id} for a in assets]

    @staticmethod
    def get_method():
        return 'post'


class RemoveAssetFromPermissionRequest(BaseAssetRelationRequest):
    """ 从授权移除资产 """
    def __init__(
            self,
            asset_id: str,
            permission_id: str,
            **kwargs
    ):
        """
        :param asset_id: 资产 ID
        :param permission_id: 授权 ID
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self.other.update({'asset': asset_id, 'assetpermission': permission_id})

    @staticmethod
    def get_method():
        return 'delete'


class BaseNodeRelationRequest(Request):
    URL = 'perms/asset-permissions-nodes-relations/'


class AppendNodesToPermissionRequest(BaseNodeRelationRequest):
    """ 向指定授权批量添加节点 """
    def __init__(
            self,
            nodes: list,
            permission_id: str,
            **kwargs
    ):
        """
        :param nodes: 节点 ID，格式 ['node1_id', 'node2_id']
        :param permission_id: 授权 ID
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self._body = [{'node': n, 'assetpermission': permission_id} for n in nodes]

    @staticmethod
    def get_method():
        return 'post'


class RemoveNodeFromPermissionRequest(BaseNodeRelationRequest):
    """ 从授权移除节点 """
    def __init__(
            self,
            node_id: str,
            permission_id: str,
            **kwargs
    ):
        """
        :param node_id: 节点 ID
        :param permission_id: 授权 ID
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self.other.update({'node': node_id, 'assetpermission': permission_id})

    @staticmethod
    def get_method():
        return 'delete'
