from jms_client.v1.models.instance.permissions import (
    CommandGroupInstance
)
from jms_client.v1.utils import handle_range_datetime
from ..common import Request
from ..const import CommandGroupType
from ..mixins import (
    DetailMixin, CreateMixin, DeleteMixin,
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


class DetailCommandGroupRequest(DetailMixin, BaseCommandGroupRequest):
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
