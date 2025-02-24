from jms_client.v1.models.instance.audits import CommandInstance
from jms_client.v1.utils import handle_range_datetime
from ..common import Request
from ..mixins import ExtraRequestMixin, WithIDMixin


class BaseCommandRequest(Request):
    URL = 'terminal/commands/'
    InstanceClass = CommandInstance


class DescribeCommandsRequest(ExtraRequestMixin, BaseCommandRequest):
    """ 获取命令列表 """
    def __init__(
            self,
            command_storage_id: str,  # 在系统设置 - 存储设置 - 命令存储 中获取
            asset: str = '',
            asset_id: str = '',
            account: str = '',
            user: str = '',
            session: str = '',
            session_id: str = '',
            risk_level: str = '',
            input_: str = '',
            date_from: str = '',  # 格式为 2021-01-01 00:00:00
            date_to: str = '',  # 格式为 2021-01-01 00:00:00
            **kwargs
    ):
        """
        :param search: 条件搜索，支持 命令输入
        :param asset: 资产
        :param asset_id: 资产 ID
        :param account: 账号
        :param user: 用户
        :param session: 会话
        :param session_id: 会话 ID
        :param risk_level: 风险等级
        :param input_: 命令输入
        :param command_storage_id: 命令存储 ID
        :param date_from: 开始时间
        :param date_to: 结束时间
        :param kwargs: 其他参数
        """
        query_params = {'command_storage_id': command_storage_id}
        if asset:
            query_params['asset'] = asset
        if asset_id:
            query_params['asset_id'] = asset_id
        if account:
            query_params['account'] = account
        if user:
            query_params['user'] = user
        if session:
            query_params['session'] = session
        if session_id:
            query_params['session_id'] = session_id
        if risk_level:
            query_params['risk_level'] = risk_level
        if input_:
            query_params['input'] = input_
        date_from, date_to = handle_range_datetime(date_from, date_to, default_days=7)
        query_params['date_from'] = date_from
        query_params['date_to'] = date_to
        super().__init__(**query_params, **kwargs)


class DetailCommandRequest(WithIDMixin, BaseCommandRequest):
    """ 获取命令详情 """

    def __init__(self, command_storage_id: str, **kwargs):
        super().__init__(command_storage_id=command_storage_id, **kwargs)
