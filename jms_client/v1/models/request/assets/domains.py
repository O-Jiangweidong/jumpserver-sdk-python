from jms_client.v1.models.instance.domains import DomainInstance
from ..common import Request
from ..mixins import ExtraRequestMixin, DetailMixin, CreateMixin


class BaseDomainRequest(Request):
    URL = 'assets/domains/'
    InstanceClass = DomainInstance


class DescribeDomainsRequest(ExtraRequestMixin, BaseDomainRequest):
    """
    获取网域列表
    """
    def __init__(
            self,
            name: str = '',
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称
        :param name: 名称
        :param kwargs: 其他参数
        """
        query_params = {}
        if name:
            query_params['name'] = name
        super().__init__(**query_params, **kwargs)


class DetailDomainRequest(DetailMixin, BaseDomainRequest):
    """
    获取网域详情
    """


class CreateUpdateDomainParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            assets: list = None,
            gateways: list = None,
            comment: str = '',
            **kwargs
    ):
        """
        :param name: 名称
        :param assets: 资产列表，格式为 ['asset1_id', 'asset2_id']
        :param gateways: 网关列表，格式为 ['gateway1_id', 'gateway2_id']
        :param comment: 备注
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self._body.update({
            'name': name,  'comment': comment,
        })
        if assets is not None:
            self._body['assets'] = assets
        if gateways is not None:
            self._body['gateways'] = gateways


class CreateDomainRequest(
    CreateUpdateDomainParamsMixin, CreateMixin, BaseDomainRequest
):
    """
    创建 网域
    """


class UpdateDomainRequest(
    CreateUpdateDomainParamsMixin, DetailMixin, BaseDomainRequest
):
    """
    更新 网域
    """
    def get_method(self):
        return 'put'


class DeleteDomainRequest(DetailMixin, BaseDomainRequest):
    """
    删除指定 ID 的网域
    """

    def get_method(self):
        return 'delete'
