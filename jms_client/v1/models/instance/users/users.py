from ..common import Instance


class UserInstance(Instance):
    TYPE = 'User'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr name: 名称
        :attr comment: 备注
        :attr username: 用户名
        :attr email: 邮箱
        :attr wechat: 微信
        :attr avatar_url: 头像链接
        :attr created_by: 创建者
        :attr updated_by: 更新者
        :attr date_api_key_last_used: 最后使用 API Key 的时间
        :attr date_expired: 过期时间
        :attr date_updated: 更新时间
        :attr date_joined: 加入时间
        :attr dingtalk_id: 钉钉 ID
        :attr feishu_id: 飞书 ID
        :attr lark_id: 飞书 ID
        :attr slack_id: Slack ID
        :attr wecom_id: 企业微信 ID
        :attr last_login: 最后登录时间
        :attr date_password_last_updated: 最后修改密码时间
        :attr is_active: 是否有效
        :attr is_valid: 是否有效
        :attr is_expired: 是否过期
        :attr mfa_enabled: 是否启用 MFA
        :attr mfa_force_enabled: 是否强制启用 MFA
        :attr need_update_password: 是否需要修改密码
        :attr is_first_login: 是否首次登录
        :attr login_blocked: 是否被锁定
        :attr is_org_admin: 是否是组织管理员
        :attr is_otp_secret_key_bound: 是否绑定了 OTP 密钥
        :attr is_service_account: 是否是服务账号
        :attr is_superuser: 是否是超级管理员
        :attr can_public_key_auth: 是否可以使用公钥登录
        :attr groups: 组
        :attr labels: 标签
        :attr system_roles: 系统角色
        :attr org_roles: 组织角色
        :attr mfa_level: MFA 等级
        :attr password_strategy: 密码策略
        :attr phone: 手机号
        :attr source: 来源
        :param kwargs: 其他参数
        """
        self.id: str = ''
        self.name: str = ''
        self.username: str = ''
        self.comment: str = ''
        self.email: str = ''
        self.wechat: str = ''
        self.avatar_url: str = ''
        self.created_by: str = ''
        self.updated_by: str = ''
        self.date_api_key_last_used: str = ''
        self.date_expired: str = ''
        self.date_updated: str = ''
        self.date_joined: str = ''
        self.dingtalk_id: str = ''
        self.feishu_id: str = ''
        self.lark_id: str = ''
        self.slack_id: str = ''
        self.wecom_id: str = ''
        self.last_login: str = ''
        self.date_password_last_updated: str = ''
        self.is_active: bool = True
        self.is_valid: bool = True
        self.is_expired: bool = False
        self.mfa_enabled: bool = True
        self.mfa_force_enabled: bool = True
        self.need_update_password: bool = True
        self.is_first_login: bool = True
        self.login_blocked: bool = False
        self.is_org_admin: bool = False
        self.is_otp_secret_key_bound: bool = False
        self.is_service_account: bool = False
        self.is_superuser: bool = False
        self.can_public_key_auth: bool = True
        self.groups: list = []
        self.labels: list = []
        self.system_roles: list = []
        self.org_roles: list = []
        self.mfa_level: dict = {}
        self.password_strategy: dict = {}
        self.phone: dict = {}
        self.source: dict = {}

        super().__init__(**kwargs)
