from jms_client.v1.models.instance.permissions import ConnectMethodACLInstance
from ..common import Request, UserManyFilterParam, PriorityParam, SimpleProtocolParam
from ..const import ACLAction
from ..mixins import (
    WithIDMixin, CreateMixin, DeleteMixin, UpdateMixin, ExtraRequestMixin
)


class BaseConnectMethodACLRequest(Request):
    URL = 'acls/connect-method-acls/'
    InstanceClass = ConnectMethodACLInstance


class DescribeConnectMethodACLsRequest(
    ExtraRequestMixin, BaseConnectMethodACLRequest
):
    """ 查询连接方式 ACL 列表 """

    def __init__(
            self,
            name: str = '',
            user: str = '',
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称
        :param name: 名称
        :param user: 用户，支持用户 ID、用户名、名称
        :param kwargs: 其他参数
        """
        query_params = {}
        if name:
            query_params['name'] = name
        if user:
            query_params['users'] = user
        super().__init__(**query_params, **kwargs)


class DetailConnectMethodACLRequest(WithIDMixin, BaseConnectMethodACLRequest):
    """ 获取指定 ID 的 连接方式ACL 详情 """


class CreateUpdateConnectMethodACLParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            comment: str = '',
            is_active: bool = True,
            priority: int = 50,
            connect_methods: SimpleProtocolParam = None,
            users: UserManyFilterParam = None,
            **kwargs
    ):
        """
        :param name: 名称
        :param comment: 备注
        :param action: 动作，支持 reject、accept、review、notice
        :param is_active: 是否激活
        :param priority: 优先级, 1-100
        :param connect_methods: 限制的连接协议
        :param users: 受控制的人
        """
        super().__init__(**kwargs)
        self._body.update({
            'name': name, 'is_active': is_active, 'action': ACLAction.REJECT,
            'priority': PriorityParam(priority),
        })
        if comment:
            self._body['comment'] = comment
        if isinstance(connect_methods, SimpleProtocolParam):
            self._body['connect_methods'] = connect_methods.get_protocols(only_name=True)
        if not isinstance(users, UserManyFilterParam):
            users = UserManyFilterParam()
        self._body['users'] = users.get_result()


class CreateConnectMethodACLRequest(
    CreateUpdateConnectMethodACLParamsMixin, CreateMixin, BaseConnectMethodACLRequest
):
    """ 创建连接方式 ACL """


class UpdateConnectMethodACLRequest(
    CreateUpdateConnectMethodACLParamsMixin, UpdateMixin, BaseConnectMethodACLRequest
):
    """ 更新指定 ID 的连接方式 ACL 属性 """


class DeleteConnectMethodACLRequest(DeleteMixin, BaseConnectMethodACLRequest):
    """ 删除指定 ID 的连接方式 ACL """
