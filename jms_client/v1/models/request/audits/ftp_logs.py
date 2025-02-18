from jms_client.v1.models.instance.audits import FTPLogInstance
from jms_client.v1.utils import handle_range_datetime
from ..common import Request
from ..mixins import ExtraRequestMixin, DetailMixin


class BaseFTPLogRequest(Request):
    URL = 'audits/ftp-logs/'
    InstanceClass = FTPLogInstance


class DescribeFTPLogsRequest(ExtraRequestMixin, BaseFTPLogRequest):
    """ 获取 FTP日志 列表 """
    def __init__(
            self,
            user: str = '',
            asset: str = '',
            account: str = '',
            filename: str = '',
            session: str = '',
            date_from: str = '',  # 格式为 2021-01-01 00:00:00
            date_to: str = '',  # 格式为 2021-01-01 00:00:00
            **kwargs
    ):
        """
        :param search: 条件搜索，支持 用户、资产、账号、文件名、会话 ID
        :param user: 用户
        :param asset: 资产
        :param account: 账号
        :param filename: 文件名
        :param session: 会话 ID
        :param date_from: 开始时间
        :param date_to: 结束时间
        :param kwargs: 其他参数
        """
        query_params = {}
        if user:
            query_params['user'] = user
        if asset:
            query_params['asset'] = asset
        if account:
            query_params['account'] = account
        if filename:
            query_params['filename'] = filename
        if session:
            query_params['session'] = session
        date_from, date_to = handle_range_datetime(date_from, date_to, default_days=7)
        query_params['date_from'] = date_from
        query_params['date_to'] = date_to
        super().__init__(**query_params, **kwargs)


class DetailFTPLogRequest(DetailMixin, BaseFTPLogRequest):
    """ 获取 FTP日志 详情 """
