from jms_client.v1.models.instance.organizations import (
    OrganizationInstance
)
from ..common import Request
from ..mixins import DetailMixin, ExtraRequestMixin


class BaseAssetRequest(Request):
    URL = 'orgs/orgs/'
    InstanceClass = OrganizationInstance


class DescribeOrganizationsRequest(ExtraRequestMixin, BaseAssetRequest):
    """ 查询组织列表 """
    def __init__(
            self,
            search: str = '',
            name: str = '',
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称、备注
        :param name: 组织名称过滤
        :param kwargs: 其他参数
        """
        query_params = {}
        if search:
            query_params['search'] = search
        if name:
            query_params['name'] = name
        super().__init__(**query_params, **kwargs)


class DetailOrganizationRequest(DetailMixin, BaseAssetRequest):
    """ 获取指定 ID 的组织详情 """


class CreateUpdateOrganizationParamsMixin(object):
    def __init__(
            self,
            name: str,
            **kwargs
    ):
        """
        :param name: 组织名称
        """
        self._body = {
            'name': name
        }
        super().__init__(**kwargs)


class CreateOrganizationRequest(
    CreateUpdateOrganizationParamsMixin, BaseAssetRequest
):
    """ 创建组织 """
    def __init__(
            self,
            id_: str = '',
            **kwargs
    ):
        """
        :param id_: 组织 ID
        :param kwargs: 其他参数
        """
        if id_:
            self._body['id'] = id_
        super().__init__(**kwargs)

    def get_method(self):
        return 'post'

    def get_data(self):
        return self._body


class UpdateOrganizationRequest(
    CreateUpdateOrganizationParamsMixin,
    DetailMixin, BaseAssetRequest
):
    """ 更新指定 ID 的组织属性 """
    def get_method(self):
        return 'put'

    def get_data(self):
        return self._body


class DeleteOrganizationRequest(DetailMixin, BaseAssetRequest):
    """ 删除指定 ID 的资产 """

    def get_method(self):
        return 'delete'
