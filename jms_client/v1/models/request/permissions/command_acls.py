from jms_client.v1.models.instance.permissions import (
    CommandGroupInstance, CommandFilterInstance,
)
from ..common import Request
from ..params import (
    AccountParam, PriorityParam,
    UserManyFilterParam, AssetManyFilterParam
)
from ..const import CommandGroupType, ACLAction
from ..mixins import (
    WithIDMixin, CreateMixin, DeleteMixin,
    UpdateMixin, ExtraRequestMixin
)


class BaseCommandGroupRequest(Request):
    URL = 'acls/command-groups/'
    InstanceClass = CommandGroupInstance


class DescribeCommandGroupsRequest(ExtraRequestMixin, BaseCommandGroupRequest):
    """ 查询命令过滤-命令组列表 """
    def __init__(
            self,
            name: str = '',
            command_filters: str = '',
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称
        :param command_filters: 命令过滤的 ID
        :param kwargs: 其他参数
        """
        query_params = {}
        if name:
            query_params['name'] = name
        if command_filters:
            query_params['command_filters'] = command_filters
        super().__init__(**query_params, **kwargs)


class DetailCommandGroupRequest(WithIDMixin, BaseCommandGroupRequest):
    """ 获取指定 ID 的命令过滤命令组详情 """


class CreateUpdateCommandGroupParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            content: str,
            ignore_case: bool = True,
            type_: str = CommandGroupType.COMMAND,
            comment: str = '',
            **kwargs
    ):
        """
        :param name: 名称
        """
        super().__init__(**kwargs)
        self._body.update({
            'name': name, 'type': CommandGroupType(type_),
            'content': content, 'ignore_case': ignore_case,
        })
        if comment:
            self._body['comment'] = comment


class CreateCommandGroupRequest(
    CreateUpdateCommandGroupParamsMixin, CreateMixin, BaseCommandGroupRequest
):
    """ 创建命令过滤-命令组 """


class UpdateCommandGroupRequest(
    CreateUpdateCommandGroupParamsMixin, UpdateMixin, BaseCommandGroupRequest
):
    """ 更新指定 ID 的命令过滤-命令组属性 """


class DeleteCommandGroupRequest(DeleteMixin, BaseCommandGroupRequest):
    """ 删除指定 ID 的命令过滤-命令组 """


class BaseCommandFilterRequest(Request):
    URL = 'acls/command-filter-acls/'
    InstanceClass = CommandFilterInstance


class DescribeCommandFiltersRequest(ExtraRequestMixin, BaseCommandFilterRequest):
    """ 查询命令过滤列表 """
    def __init__(
            self,
            name: str = '',
            assets: str = '',
            users: str = '',
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称
        :param assets: 资产 ID、名称、地址
        :param users: 用户 ID、名称、用户名
        :param kwargs: 其他参数
        """
        query_params = {}
        if name:
            query_params['name'] = name
        if assets:
            query_params['assets'] = assets
        if users:
            query_params['users'] = users
        super().__init__(**query_params, **kwargs)


class DetailCommandFilterRequest(WithIDMixin, BaseCommandFilterRequest):
    """ 获取指定 ID 的命令过滤详情 """


class CreateUpdateCommandFilterParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            priority: int = 50,
            is_active: bool = True,
            action: str = ACLAction.REJECT,
            comment: str = '',
            command_groups: list = None,
            accounts: AccountParam = None,
            assets: AssetManyFilterParam = None,
            reviewers: list = None,
            users: UserManyFilterParam = None,
            **kwargs
    ):
        """
        :param name: 名称
        :param priority: 优先级
        :param is_active: 是否激活
        :param action: 动作，支持 reject、accept、review、notice
        :param comment: 备注
        :param command_groups: 命令组列表，格式为 ['cmd_filter1_id', 'cmd_filter2_id']
        :param accounts: 账号
        :param assets: 资产
        :param reviewers: 审核接受者
        :param users: 受控制的人
        """
        super().__init__(**kwargs)
        if action in (ACLAction.REVIEW, ACLAction.WARNING) and not reviewers:
            raise ValueError('reviewers can not be empty')
        elif action == ACLAction.NOTICE:
            raise ValueError('action can not be ACLAction.NOTICE(notice)')
        self._body.update({
            'name': name, 'priority': PriorityParam(priority),
            'action': ACLAction(action), 'is_active': is_active,
        })
        if comment:
            self._body['comment'] = comment
        if isinstance(reviewers, list):
            self._body['reviewers'] = reviewers
        if isinstance(command_groups, list):
            self._body['command_groups'] = command_groups
        if isinstance(accounts, AccountParam):
            self._body['accounts'] = accounts.get_accounts()
        if not isinstance(users, UserManyFilterParam):
            users = UserManyFilterParam()
        self._body['users'] = users.get_result()
        if not isinstance(assets, AssetManyFilterParam):
            assets = AssetManyFilterParam()
        self._body['assets'] = assets.get_result()


class CreateCommandFilterRequest(
    CreateUpdateCommandFilterParamsMixin, CreateMixin, BaseCommandFilterRequest
):
    """ 创建命令过滤 """


class UpdateCommandFilterRequest(
    CreateUpdateCommandFilterParamsMixin, UpdateMixin, BaseCommandFilterRequest
):
    """ 更新指定 ID 的命令过滤属性 """


class DeleteCommandFilterRequest(DeleteMixin, BaseCommandFilterRequest):
    """ 删除指定 ID 的命令过滤 """
