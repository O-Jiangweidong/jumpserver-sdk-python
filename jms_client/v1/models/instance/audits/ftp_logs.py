from ..common import Instance


class FTPLogInstance(Instance):
    TYPE = 'FTPLog'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr filename: 文件名
        :attr account: 账号
        :attr asset: 资产
        :attr date_start: 开始时间
        :attr has_file: 是否有文件
        :attr is_success: 是否成功
        :attr operate: 动作
        :attr org_id: 组织 ID
        :attr remote_addr: 远端地址
        :attr session: 会话 ID
        :attr user: 用户标识
        """
        self.id: str = ''
        self.filename: str = ''
        self.account: str = ''
        self.asset: str = ''
        self.date_start: str = ''
        self.has_file: bool = False
        self.is_success: bool = False
        self.operate: dict = {}
        self.org_id: str = ''
        self.remote_addr: str = ''
        self.session: str = ''
        self.user: str = ''
        super().__init__(**kwargs)

    @property
    def display(self):
        return f'{self.filename}({self.user})'
