from jms_client.v1.models.instance.assets import NodeInstance
from ..common import Request
from ..mixins import (
    ExtraRequestMixin, DetailMixin, CreateMixin,
    UpdateMixin, DeleteMixin,
)


class BaseNodeRequest(Request):
    URL = 'assets/nodes/'
    InstanceClass = NodeInstance


class DescribeNodesRequest(ExtraRequestMixin, BaseNodeRequest):
    """ 获取节点列表 """
    def __init__(
            self,
            id_: str = '',
            key: str = '',
            value: str = '',
            **kwargs
    ):
        """
        :param search: 条件搜索，支持全量节点名称
        :param name: 名称
        :param kwargs: 其他参数
        """
        query_params = {}
        if id_:
            query_params['id'] = id_
        if key:
            query_params['key'] = key
        if value:
            query_params['value'] = value
        super().__init__(**query_params, **kwargs)


class DetailNodeRequest(DetailMixin, BaseNodeRequest):
    """ 获取节点详情 """


class CreateUpdateNodeParamsMixin(object):
    _body: dict

    def __init__(
            self,
            value: str = '',
            **kwargs
    ):
        """
        :param value: 子节点名称
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        if value:
            self._body['value'] = value


class CreateNodeRequest(
    CreateUpdateNodeParamsMixin, CreateMixin, BaseNodeRequest
):
    """ 创建 节点 """
    def __init__(
            self,
            full_value: str = '',
            **kwargs
    ):
        """
            :param full_value: 全量节点名称, 优先级大于 value, 当指定 full_value 时，id_ 参数无效
            :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        if full_value:
            self._body['full_value'] = full_value


class UpdateNodeRequest(
    CreateUpdateNodeParamsMixin, UpdateMixin, BaseNodeRequest
):
    """ 更新 节点 """


class DeleteNodeRequest(DeleteMixin, BaseNodeRequest):
    """ 删除指定 ID 的节点 """
