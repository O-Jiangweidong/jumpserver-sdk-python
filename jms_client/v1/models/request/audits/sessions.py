from jms_client.v1.models.instance.audits import SessionInstance
from jms_client.v1.utils import handle_range_datetime
from ..common import Request
from ..mixins import ExtraRequestMixin, DetailMixin


class BaseSessionLogRequest(Request):
    URL = 'terminal/sessions/'
    InstanceClass = SessionInstance


class DescribeSessionsRequest(ExtraRequestMixin, BaseSessionLogRequest):
    """ 获取会话记录列表 """
    def __init__(
            self,
            user: str = '',
            user_id: str = '',
            asset: str = '',
            asset_id: str = '',
            account: str = '',
            remote_addr: str = '',
            protocol: str = '',
            login_from: str = '',
            terminal: str = '',
            is_finished: bool = None,
            date_from: str = '',  # 格式为 2021-01-01 00:00:00
            date_to: str = '',  # 格式为 2021-01-01 00:00:00
            **kwargs
    ):
        """
        :param search: 条件搜索，支持 用户、资产、账号、远端地址、协议、登录来源
        :param user: 用户
        :param user_id: 用户 ID
        :param asset: 资产
        :param asset_id: 资产 ID
        :param account: 账号
        :param remote_addr: 远端地址
        :param protocol: 协议
        :param login_from: 登录来源
        :param terminal: 终端 ID/名称
        :param is_finished: 是否已结束
        :param date_from: 开始时间
        :param date_to: 结束时间
        :param kwargs: 其他参数
        """
        query_params = {}
        if user:
            query_params['user'] = user
        if user_id:
            query_params['user_id'] = user_id
        if asset:
            query_params['asset'] = asset
        if asset_id:
            query_params['asset_id'] = asset_id
        if account:
            query_params['account'] = account
        if remote_addr:
            query_params['remote_addr'] = remote_addr
        if protocol:
            query_params['protocol'] = protocol
        if login_from:
            query_params['login_from'] = login_from
        if terminal:
            query_params['terminal'] = terminal
        if is_finished is not None:
            query_params['is_finished'] = is_finished
        date_from, date_to = handle_range_datetime(date_from, date_to, default_days=7)
        query_params['date_from'] = date_from
        query_params['date_to'] = date_to
        super().__init__(**query_params, **kwargs)


class DetailSessionRequest(DetailMixin, BaseSessionLogRequest):
    """ 获取会话记录详情 """
