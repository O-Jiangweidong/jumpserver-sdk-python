from jms_client.v1.models.instance.audits import JobLogInstance
from jms_client.v1.utils import handle_range_datetime
from ..common import Request
from ..mixins import ExtraRequestMixin, DetailMixin


class BaseJobLogRequest(Request):
    URL = 'audits/job-logs/'
    InstanceClass = JobLogInstance


class DescribeJobLogsRequest(ExtraRequestMixin, BaseJobLogRequest):
    """ 获取作业日志列表 """
    def __init__(
            self,
            creator_name: str = '',
            material: str = '',
            date_from: str = '',  # 格式为 2021-01-01 00:00:00
            date_to: str = '',  # 格式为 2021-01-01 00:00:00
            **kwargs
    ):
        """
        :param search: 条件搜索，支持 创建者名称、作业内容
        :param creator_name: 创建者名称
        :param material: 作业内容
        :param kwargs: 其他参数
        """
        query_params = {}
        if creator_name:
            query_params['creator_name'] = creator_name
        if material:
            query_params['material'] = material
        date_from, date_to = handle_range_datetime(date_from, date_to, default_days=7)
        query_params['date_from'] = date_from
        query_params['date_to'] = date_to
        super().__init__(**query_params, **kwargs)


class DetailJobLogRequest(DetailMixin, BaseJobLogRequest):
    """ 获取作业日志详情 """
