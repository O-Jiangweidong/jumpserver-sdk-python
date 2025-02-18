from jms_client.v1.models.instance.audits import OperateLogInstance
from jms_client.v1.utils import handle_range_datetime
from ..common import Request
from ..mixins import ExtraRequestMixin, DetailMixin


class BaseOperateLogRequest(Request):
    URL = 'audits/operate-logs/'
    InstanceClass = OperateLogInstance


class DescribeOperateLogsRequest(ExtraRequestMixin, BaseOperateLogRequest):
    """ 获取操作日志列表 """
    def __init__(
            self,
            user='',
            action='',
            resource='',
            remote_addr='',
            resource_type='',
            date_from: str = '',  # 格式为 2021-01-01 00:00:00
            date_to: str = '',  # 格式为 2021-01-01 00:00:00
            **kwargs
    ):
        """
        :param search: 条件搜索，支持 被操作对象、用户标识
        :param user: 用户标识
        :param action: 操作动作
        :param resource: 被操作对象
        :param resource_type: 被操作对象类型
        :param remote_addr: 操作者的远端地址
        :param kwargs: 其他参数
        """
        query_params = {}
        if user:
            query_params['user'] = user
        if action:
            query_params['action'] = action
        if resource:
            query_params['resource'] = resource
        if remote_addr:
            query_params['remote_addr'] = remote_addr
        if resource_type:
            query_params['resource_type'] = resource_type
        date_from, date_to = handle_range_datetime(date_from, date_to, default_days=7)
        query_params['date_from'] = date_from
        query_params['date_to'] = date_to
        super().__init__(**query_params, **kwargs)


class DetailOperateLogRequest(DetailMixin, BaseOperateLogRequest):
    """ 获取操作日志详情 """
