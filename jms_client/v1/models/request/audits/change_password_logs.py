from jms_client.v1.models.instance.audits import ChangePasswordLogInstance
from jms_client.v1.utils import handle_range_datetime
from ..common import Request
from ..mixins import ExtraRequestMixin, WithIDMixin


class BaseChangePasswordLogRequest(Request):
    URL = 'audits/password-change-logs/'
    InstanceClass = ChangePasswordLogInstance


class DescribeChangePasswordLogsRequest(
    ExtraRequestMixin, BaseChangePasswordLogRequest
):
    """ 获取用户改密日志列表 """
    def __init__(
            self,
            user='',
            change_by='',
            remote_addr='',
            date_from: str = '',  # 格式为 2021-01-01 00:00:00
            date_to: str = '',  # 格式为 2021-01-01 00:00:00
            **kwargs
    ):
        """
        :param search: 条件搜索，支持 用户标识，改密者，远端地址
        :param user: 用户标识
        :param change_by: 改密者
        :param remote_addr: 改密者的远端地址
        :param kwargs: 其他参数
        """
        query_params = {}
        if user:
            query_params['user'] = user
        if change_by:
            query_params['change_by'] = change_by
        if remote_addr:
            query_params['remote_addr'] = remote_addr
        date_from, date_to = handle_range_datetime(date_from, date_to, default_days=7)
        query_params['date_from'] = date_from
        query_params['date_to'] = date_to
        super().__init__(**query_params, **kwargs)


class DetailChangePasswordLogRequest(WithIDMixin, BaseChangePasswordLogRequest):
    """ 获取用户改密日志详情 """
