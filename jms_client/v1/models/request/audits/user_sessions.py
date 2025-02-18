from jms_client.v1.models.instance.audits import UserSessionInstance
from ..common import Request
from ..mixins import (
    ExtraRequestMixin, DetailMixin,
)


class BaseUserSessionRequest(Request):
    URL = 'audits/user-sessions/'
    InstanceClass = UserSessionInstance


class DescribeUserSessionsRequest(ExtraRequestMixin, BaseUserSessionRequest):
    """ 获取在线用户列表 """
    def __init__(
            self,
            id_: str = '',
            ip: str = '',
            city: str = '',
            type_: str = '',
            is_active: bool = None,
            **kwargs
    ):
        """
        :param search: 条件搜索，支持 ID、IP、城市
        :param id_: ID
        :param ip: IP
        :param city: 城市
        :param type_: 类型
        :param is_active: 是否活跃
        :param kwargs: 其他参数
        """
        query_params = {}
        if id_:
            query_params['id'] = id_
        if ip:
            query_params['ip'] = ip
        if city:
            query_params['city'] = city
        if type_:
            query_params['type'] = type_
        if is_active is not None:
            query_params['is_active'] = is_active
        super().__init__(**query_params, **kwargs)


class DetailUserSessionRequest(DetailMixin, BaseUserSessionRequest):
    """ 获取在线用户详情 """
