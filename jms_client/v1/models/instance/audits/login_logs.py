from ..common import Instance


class LoginLogInstance(Instance):
    TYPE = 'LoginLog'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr ip: IP
        :attr city: 登录城市
        :attr type: 认证类型
        :attr backend: 认证方式
        :attr backend_display: 认证方式显示名
        :attr datetime: 登录日期
        :attr mfa: MFA
        :attr reason: 原因
        :attr reason_display: 原因描述
        :attr status: 状态
        :attr username: 用户信息
        :attr user_agent: 用户代理
        """
        self.id: str = ''
        self.ip: str = ''
        self.city: str = ''
        self.type: dict = {}
        self.backend: str = ''
        self.backend_display: str = ''
        self.datetime: str = ''
        self.mfa: dict = {}
        self.reason: str = ''
        self.reason_display: str = ''
        self.status: dict = {}
        self.username: str = ''
        self.user_agent: str = ''
        super().__init__(**kwargs)

    @property
    def display(self):
        return f'{self.username}({self.backend_display})'
