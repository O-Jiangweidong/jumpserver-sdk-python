from ..common import Instance


class UserSessionInstance(Instance):
    TYPE = 'UserSession'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr ip: IP
        :attr city: 登录城市
        :attr type: 认证类型
        :attr user: 用户信息
        :attr user_agent: 用户代理
        :attr is_active: 是否有效
        :attr backend: 认证方式
        :attr backend_display: 认证方式显示名
        :attr date_created: 创建时间
        :attr date_expired: 过期时间
        :attr is_current_user_session: 是否当前登录用户
        """
        self.id: str = ''
        self.ip: str = ''
        self.city: str = ''
        self.type: dict = {}
        self.user: dict = {}
        self.user_agent: str = ''
        self.is_active: bool = True
        self.backend: str = ''
        self.backend_display: str = ''
        self.date_created: str = ''
        self.date_expired: str = ''
        self.is_current_user_session: bool = False
        super().__init__(**kwargs)

    @property
    def display(self):
        return f'{self.user["name"]}({self.backend_display})'
