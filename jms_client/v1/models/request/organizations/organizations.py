from jms_client.v1.models.instance.organizations import (
    OrganizationInstance
)
from ..common import Request
from ..mixins import (
    ExtraRequestMixin, DetailMixin, CreateMixin,
    UpdateMixin, DeleteMixin
)


class BaseOrganizationRequest(Request):
    URL = 'orgs/orgs/'
    InstanceClass = OrganizationInstance


class DescribeOrganizationsRequest(ExtraRequestMixin, BaseOrganizationRequest):
    """ 查询组织列表 """
    def __init__(
            self,
            name: str = '',
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称、备注
        :param name: 名称过滤
        :param kwargs: 其他参数
        """
        query_params = {}
        if name:
            query_params['name'] = name
        super().__init__(**query_params, **kwargs)


class DetailOrganizationRequest(DetailMixin, BaseOrganizationRequest):
    """ 获取指定 ID 的组织详情 """


class CreateUpdateOrganizationParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            **kwargs
    ):
        """
        :param name: 名称
        """
        super().__init__(**kwargs)
        self._body['name'] = name


class CreateOrganizationRequest(
    CreateUpdateOrganizationParamsMixin, CreateMixin, BaseOrganizationRequest
):
    """ 创建组织 """


class UpdateOrganizationRequest(
    CreateUpdateOrganizationParamsMixin,
    UpdateMixin, BaseOrganizationRequest
):
    """ 更新指定 ID 的组织属性 """


class DeleteOrganizationRequest(DeleteMixin, BaseOrganizationRequest):
    """ 删除指定 ID 的资产 """
