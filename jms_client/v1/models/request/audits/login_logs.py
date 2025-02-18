from jms_client.v1.models.instance.audits import LoginLogInstance
from jms_client.v1.utils import handle_range_datetime
from ..common import Request
from ..mixins import ExtraRequestMixin, DetailMixin


class BaseLoginLogRequest(Request):
    URL = 'audits/login-logs/'
    InstanceClass = LoginLogInstance


class DescribeLoginLogsRequest(ExtraRequestMixin, BaseLoginLogRequest):
    """ 获取登录日志列表 """
    def __init__(
            self,
            id_: str = '',
            ip: str = '',
            city: str = '',
            type_: str = '',
            status: str = '',
            mfa: str = '',
            username: str = '',
            date_from: str = '',  # 格式为 2021-01-01 00:00:00
            date_to: str = '',  # 格式为 2021-01-01 00:00:00
            **kwargs
    ):
        """
        :param search: 条件搜索，支持 ID、IP、城市、用户信息
        :param id_: ID
        :param ip: IP
        :param city: 城市
        :param type_: 类型
        :param status: 状态
        :param mfa: MFA
        :param username: 用户名
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
        if status:
            query_params['status'] = status
        if mfa:
            query_params['mfa'] = mfa
        if username:
            query_params['username'] = username
        date_from, date_to = handle_range_datetime(date_from, date_to, default_days=7)
        query_params['date_from'] = date_from
        query_params['date_to'] = date_to
        super().__init__(**query_params, **kwargs)


class DetailLoginLogRequest(DetailMixin, BaseLoginLogRequest):
    """ 获取登录日志详情 """
