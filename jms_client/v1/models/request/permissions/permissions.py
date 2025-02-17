from datetime import datetime, timedelta

from jms_client.v1.models.instance.permissions import (
    PermissionInstance
)
from ..common import Request, ProtocolParam as BaseProtocolParam
from ..mixins import (
    DetailMixin, CreateMixin, DeleteMixin,
    UpdateMixin, ExtraRequestMixin
)


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


class DetailPermissionRequest(DetailMixin, BasePermissionRequest):
    """ 获取指定 ID 的授权详情 """


class AccountParam(object):
    ALL = '@ALL'
    INPUT = '@INPUT'
    SPEC = '@SPEC'
    ANON = '@ANON'
    USER = '@USER'

    def __init__(self):
        self._accounts = []

    def get_accounts(self):
        if {self.ALL, self.SPEC}.issubset(set(self._accounts)):
            raise ValueError('AccountParam 中不能同时包含 所有账号 和 指定账号')
        return self._accounts

    def set_all(self):
        self._accounts.append(self.ALL)

    def set_input(self):
        """ 设置手动账号 """
        self._accounts.append(self.INPUT)

    def set_user(self):
        """ 设置同名账号 """
        self._accounts.append(self.USER)

    def set_spec(self, username: list):
        """ 设置指定账号
        :param username:
        """
        self._accounts.extend([self.SPEC, *username])

    def set_anon(self):
        """ 设置匿名账号 """
        self._accounts.append(self.ANON)


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


class ProtocolParam(BaseProtocolParam):
    def __init__(self):
        super().__init__(type_=None)
        self._pre_check = False

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
        date_start, date_expired = self.handle_datetime(date_start, date_expired)
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

    @staticmethod
    def handle_datetime(start, expired, formater='%Y-%m-%d %H:%M:%S'):
        try:
            start_time = datetime.strptime(start, formater)
        except ValueError:
            start_time = datetime.now()

        try:
            expired_time = datetime.strptime(expired, formater)
        except ValueError:
            expired_time = start_time + timedelta(days=70 * 365)
        start_time = start_time.strftime(formater)
        expired_time = expired_time.strftime(formater)
        return start_time, expired_time


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
