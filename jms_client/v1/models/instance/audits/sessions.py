from ..common import Instance


class SessionInstance(Instance):
    TYPE = 'Session'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr comment: 备注
        :attr account: 账号
        :attr account_id: 账号 ID
        :attr asset: 资产
        :attr asset_id: 资产 ID
        :attr can_join: 是否可加入
        :attr can_replay: 是否可回放
        :attr can_terminate: 是否可终止
        :attr command_amount: 命令数量
        :attr date_start: 开始时间
        :attr date_end: 结束时间
        :attr duration: 持续时间
        :attr org_id: 组织 ID
        :attr org_name: 组织名称
        :attr protocol: 协议
        :attr remote_addr: 远程地址
        :attr terminal_display: 终端显示名
        :attr user: 用户
        :attr user_id: 用户 ID
        :attr error_reason: 错误原因
        :attr login_from: 登录来源
        :attr terminal: 终端
        :attr type: 类型
        :attr has_command: 是否有命令
        :attr has_replay: 是否有回放
        :attr is_finished: 是否已结束
        :attr is_locked: 是否锁定
        :attr is_success: 是否成功
        :param kwargs:  其他参数
        """
        self.id: str = ''
        self.comment: str = ''
        self.account: str = ''
        self.account_id: str = ''
        self.asset: str = ''
        self.asset_id: str = ''
        self.can_join: bool = False
        self.can_replay: bool = False
        self.can_terminate: bool = False
        self.command_amount: int = 0
        self.date_start: str = ''
        self.date_end: str = ''
        self.duration: str = ''
        self.org_id: str = ''
        self.org_name: str = ''
        self.protocol: str = ''
        self.remote_addr: str = ''
        self.terminal_display: str = ''
        self.user: str = ''
        self.user_id: str = ''
        self.error_reason: dict = {}
        self.login_from: dict = {}
        self.terminal: dict = {}
        self.type: dict = {}
        self.has_command: bool = False
        self.has_replay: bool = False
        self.is_finished: bool = False
        self.is_locked: bool = False
        self.is_success: bool = False
        super().__init__(**kwargs)

    @property
    def display(self):
        return f'{self.asset}({self.account})'
