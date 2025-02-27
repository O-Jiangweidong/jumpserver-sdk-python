from jms_client.v1.models.instance.labels import (
    LabelInstance, ResourceTypeInstance, LabelResourceInstance
)
from ..common import Request
from ..mixins import (
    ExtraRequestMixin, WithIDMixin, CreateMixin, UpdateMixin, DeleteMixin
)


__all__ = [
    'DescribeLabelsRequest', 'DetailLabelRequest',
    'CreateLabelRequest', 'UpdateLabelRequest', 'DeleteLabelRequest',
    'BindLabelForResourceRequest', 'DescribeLabelResourceTypesRequest',
    'DescribeLabelResourceRequest', 'UnBindLabelForResourceRequest'
]


class BaseLabelRequest(Request):
    URL = 'labels/labels/'
    InstanceClass = LabelInstance


class DescribeLabelsRequest(ExtraRequestMixin, BaseLabelRequest):
    """ 查询标签列表 """
    def __init__(
            self,
            name: str = '',
            value: str = '',
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称、值
        :param name: 名称过滤
        :param value: 值过滤
        :param kwargs: 其他参数
        """
        query_params = {}
        if name:
            query_params['name'] = name
        if value:
            query_params['value'] = value
        super().__init__(**query_params, **kwargs)


class DetailLabelRequest(WithIDMixin, BaseLabelRequest):
    """ 获取指定 ID 的标签详情 """


class CreateUpdateLabelParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            value: str,
            comment: str,
            **kwargs
    ):
        """
        :param name: 名称
        :param value: 值
        :param comment: 备注
        """
        super().__init__(**kwargs)
        self._body.update({'name': name, 'value': value})
        if comment:
            self._body['comment'] = comment


class CreateLabelRequest(
    CreateUpdateLabelParamsMixin, CreateMixin, BaseLabelRequest
):
    """ 创建标签 """


class UpdateLabelRequest(
    CreateUpdateLabelParamsMixin, UpdateMixin, BaseLabelRequest
):
    """ 更新指定 ID 的标签属性 """


class DeleteLabelRequest(DeleteMixin, BaseLabelRequest):
    """ 删除指定 ID 的标签 """


class DescribeLabelResourceTypesRequest(Request):
    """ 获取资源类型列表(绑定标签使用) """
    URL = 'labels/resource-types/'
    InstanceClass = ResourceTypeInstance


class BaseLabelResourceRequest(Request):
    URL = 'labels/labeled-resources/'
    InstanceClass = LabelResourceInstance

    def __init__(
            self,
            label_id: str,
            **kwargs
    ):
        super().__init__(label=label_id, **kwargs)


class DescribeLabelResourceRequest(ExtraRequestMixin, BaseLabelResourceRequest):
    """ 获取标签绑定的资源列表 """


class UnBindLabelForResourceRequest(DeleteMixin, BaseLabelResourceRequest):
    """ 给指定资源解除绑定某标签 """


class BindLabelForResourceRequest(UpdateMixin, Request):
    """ 给绑定资源标签 """
    def __init__(
            self,
            label_id: str,
            resource_type_id: str,
            resource_ids: list,
            **kwargs
    ):
        """
        :param label_id: 标签 ID
        :param resource_type_id: 资源类型 ID，如平台 ID
        :param resource_ids: 资源 ID，格式为 ['obj1_id', 'obj2_id']
        """
        self.URL = 'labels/labels/{id}/resource-types/' + f'{resource_type_id}/resources/'
        super().__init__(id_=label_id, **kwargs)
        self._body.update({'res_ids': resource_ids})
