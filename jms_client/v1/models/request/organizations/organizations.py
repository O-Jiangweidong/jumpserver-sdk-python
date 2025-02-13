from jms_client.v1.models.instance.organizations import (
    OrganizationInstance
)
from ..common import Request
from ..mixins import DetailMixin


class DescribeOrganizationsRequest(Request):
    """
    查询组织列表
    """
    URL = 'orgs/orgs/'
    InstanceClass = OrganizationInstance

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
        father_kwargs = {}
        if search:
            father_kwargs['search'] = search
        if name:
            father_kwargs['name'] = name
        super().__init__(**father_kwargs, **kwargs)


class DetailOrganizationRequest(DetailMixin, DescribeOrganizationsRequest):
    """
    获取指定 ID 的组织详情
    """


class DeleteOrganizationRequest(DetailMixin, Request):
    """
    删除指定 ID 的资产
    """
    URL = 'orgs/orgs/'

    def get_method(self):
        return 'delete'
