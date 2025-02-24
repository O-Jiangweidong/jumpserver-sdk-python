from jms_client.v1.models.instance.labels import LabelInstance
from ..common import Request
from ..mixins import (
    ExtraRequestMixin, WithIDMixin, CreateMixin, UpdateMixin, DeleteMixin
)


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
