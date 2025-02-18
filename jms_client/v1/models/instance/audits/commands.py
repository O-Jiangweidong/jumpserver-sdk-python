from ..common import Instance


class CommandInstance(Instance):
    TYPE = 'Command'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr user: 用户标识
        :attr account: 账号
        :attr asset: 资产
        :attr org_id: 组织 ID
        :attr remote_addr: 远程地址
        :attr input: 输入
        :attr output: 输出
        :attr session: 会话 ID
        :attr timestamp: 时间戳
        :attr timestamp_display: 时间戳显示
        :attr risk_level: 风险等级
        :param kwargs:  其他参数
        """
        self.id: str = ''
        self.user: str = ''
        self.account: str = ''
        self.asset: str = ''
        self.org_id: str = ''
        self.remote_addr: str = ''
        self.input: str = ''
        self.output: str = ''
        self.session: str = ''
        self.timestamp: str = ''
        self.timestamp_display: str = ''
        self.risk_level: dict = {}
        super().__init__(**kwargs)

    @property
    def display(self):
        return f'{self.input}({self.asset})'
