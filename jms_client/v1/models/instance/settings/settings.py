from ..common import Instance


class BaseInstance(Instance):
    @property
    def display(self):
        return ''


class BasicSettingInstance(BaseInstance):
    """ 基本设置 - 基本 """
    TYPE = 'BasicSetting'

    def __init__(self, **kwargs):
        """
        :attr GLOBAL_ORG_DISPLAY_NAME: 全局组织名
        :attr HELP_DOCUMENT_URL: 文档链接
        :attr HELP_SUPPORT_URL: 支持链接
        :attr SITE_URL: 当前站点 URL
        :attr USER_GUIDE_URL: 用户手册地址
        """
        self.GLOBAL_ORG_DISPLAY_NAME = ''
        self.HELP_DOCUMENT_URL = ''
        self.HELP_SUPPORT_URL = ''
        self.SITE_URL = ''
        self.USER_GUIDE_URL = ''
        super().__init__(**kwargs)


class TerminalSettingInstance(BaseInstance):
    """ 组件设置 - 基本设置 """
    TYPE = 'TerminalSetting'

    def __init__(self, **kwargs):
        """
        :attr SECURITY_SERVICE_ACCOUNT_REGISTRATION: 是否开启组件注册
        :attr TERMINAL_ASSET_LIST_PAGE_SIZE: 资产列表每页数量
        :attr TERMINAL_ASSET_LIST_SORT_BY: 资产列表排序，name/ip
        :attr TERMINAL_KOKO_SSH_ENABLED: 是否启用 SSH Client
        :attr TERMINAL_MAGNUS_ENABLED: 启用数据库组件
        :attr TERMINAL_PASSWORD_AUTH: 终端是否启用密码认证
        :attr TERMINAL_PUBLIC_KEY_AUTH: 终端是否启用密钥认证
        :attr TERMINAL_RAZOR_ENABLED: 是否启用 Razor 服务
        """
        self.SECURITY_SERVICE_ACCOUNT_REGISTRATION = False
        self.TERMINAL_ASSET_LIST_PAGE_SIZE = ''
        self.TERMINAL_ASSET_LIST_SORT_BY = ''
        self.TERMINAL_KOKO_SSH_ENABLED = False
        self.TERMINAL_MAGNUS_ENABLED = False
        self.TERMINAL_PASSWORD_AUTH = False
        self.TERMINAL_PUBLIC_KEY_AUTH = False
        self.TERMINAL_RAZOR_ENABLED = False
        super().__init__(**kwargs)


class SecurityAuthSettingInstance(BaseInstance):
    """ 安全设置 - 认证安全 """
    TYPE = 'SecurityAuthSetting'

    def __init__(self, **kwargs):
        """
        :attr OTP_ISSUER_NAME: OTP 扫描后的名称
        :attr OTP_VALID_WINDOW: OTP 延迟有效次数
        :attr SECURITY_CHECK_DIFFERENT_CITY_LOGIN: 是否异地登录通知
        :attr SECURITY_LOGIN_CAPTCHA_ENABLED: 是否启用登录验证码
        :attr SECURITY_LOGIN_CHALLENGE_ENABLED: 是否启用登录附加码
        :attr SECURITY_MFA_AUTH: 全局启用 MFA 认证，0 未启用/1 所有用户/2 仅仅管理员
        :attr SECURITY_MFA_AUTH_ENABLED_FOR_THIRD_PARTY: 第三方认证是否开启 MFA
        :attr SECURITY_MFA_IN_LOGIN_PAGE: MFA 是否在登录页面输入
        :attr SECURITY_MFA_VERIFY_TTL: MFA 校验有效期
        :attr SECURITY_UNCOMMON_USERS_TTL: 不活跃用户自动禁用 (天)
        :attr VERIFY_CODE_TTL: 验证码有效时间 (秒)
        """
        self.OTP_ISSUER_NAME = ''
        self.OTP_VALID_WINDOW = 1
        self.SECURITY_CHECK_DIFFERENT_CITY_LOGIN = False
        self.SECURITY_LOGIN_CAPTCHA_ENABLED = False
        self.SECURITY_LOGIN_CHALLENGE_ENABLED = False
        self.SECURITY_MFA_AUTH = 0
        self.SECURITY_MFA_AUTH_ENABLED_FOR_THIRD_PARTY = False
        self.SECURITY_MFA_IN_LOGIN_PAGE = False
        self.SECURITY_MFA_VERIFY_TTL = 10
        self.SECURITY_UNCOMMON_USERS_TTL = 99999
        self.VERIFY_CODE_TTL = 300
        super().__init__(**kwargs)


class SecuritySessionSettingInstance(BaseInstance):
    """ 安全设置 - 会话安全 """
    TYPE = 'SecuritySessionSetting'

    def __init__(self, **kwargs):
        """
        :attr SECURITY_LUNA_REMEMBER_AUTH: 是否保存手动输入密码
        :attr SECURITY_MAX_IDLE_TIME: 连接最大空闲时间 (分)
        :attr SECURITY_MAX_SESSION_TIME: 会话连接最大时间 (时)
        :attr SECURITY_SESSION_SHARE: 是否开启会话共享
        :attr SECURITY_WATERMARK_ENABLED: 是否开启水印
        :attr SESSION_EXPIRE_AT_BROWSER_CLOSE: 会话在浏览器关闭时过期
        :param kwargs:
        """
        self.SECURITY_LUNA_REMEMBER_AUTH = False
        self.SECURITY_MAX_IDLE_TIME = 0
        self.SECURITY_MAX_SESSION_TIME = 0
        self.SECURITY_SESSION_SHARE = False
        self.SECURITY_WATERMARK_ENABLED = False
        self.SESSION_EXPIRE_AT_BROWSER_CLOSE = False
        super().__init__(**kwargs)


class SecurityPasswordSettingInstance(BaseInstance):
    """ 安全设置 - 密码安全 """
    TYPE = 'SecurityPasswordSetting'

    def __init__(self, **kwargs):
        """
        :attr OLD_PASSWORD_HISTORY_LIMIT_COUNT: 不能设置近几次密码
        :attr SECURITY_ADMIN_USER_PASSWORD_MIN_LENGTH: 管理员密码最小长度
        :attr SECURITY_PASSWORD_EXPIRATION_TIME: 用户密码过期时间 (天)
        :attr SECURITY_PASSWORD_LOWER_CASE: 必须包含小写字符
        :attr SECURITY_PASSWORD_MIN_LENGTH: 密码最小长度
        :attr SECURITY_PASSWORD_NUMBER: 必须包含数字
        :attr SECURITY_PASSWORD_SPECIAL_CHAR: 必须包含特殊字符
        :attr SECURITY_PASSWORD_UPPER_CASE: 必须包含大写字符
        """
        self.OLD_PASSWORD_HISTORY_LIMIT_COUNT = 0
        self.SECURITY_ADMIN_USER_PASSWORD_MIN_LENGTH = 0
        self.SECURITY_PASSWORD_EXPIRATION_TIME = 0
        self.SECURITY_PASSWORD_LOWER_CASE = 0
        self.SECURITY_PASSWORD_MIN_LENGTH = 0
        self.SECURITY_PASSWORD_NUMBER = False
        self.SECURITY_PASSWORD_SPECIAL_CHAR = False
        self.SECURITY_PASSWORD_UPPER_CASE = False
        super().__init__(**kwargs)


class SecurityLoginLimitSettingInstance(BaseInstance):
    """ 安全设置 - 登录限制 """
    TYPE = 'SecurityLoginLimitSetting'

    def __init__(self, **kwargs):
        """
        :attr ONLY_ALLOW_AUTH_FROM_SOURCE: 仅从用户来源登录
        :attr ONLY_ALLOW_EXIST_USER_AUTH: 仅已存在用户登录
        :attr USER_LOGIN_SINGLE_MACHINE_ENABLED: 仅一台设备登录
        :attr SECURITY_LOGIN_IP_BLACK_LIST: IP 登录白名单
        :attr SECURITY_LOGIN_IP_WHITE_LIST: IP 登录黑名单
        :attr SECURITY_LOGIN_IP_LIMIT_COUNT: 限制 IP 登录失败次数
        :attr SECURITY_LOGIN_IP_LIMIT_TIME: 禁止 IP 登录间隔 (分)
        :attr SECURITY_LOGIN_LIMIT_COUNT: 限制用户登录失败次数
        :attr SECURITY_LOGIN_LIMIT_TIME: 禁止用户登录间隔 (分)
        """
        self.ONLY_ALLOW_AUTH_FROM_SOURCE = False
        self.ONLY_ALLOW_EXIST_USER_AUTH = False
        self.USER_LOGIN_SINGLE_MACHINE_ENABLED = False
        self.SECURITY_LOGIN_IP_BLACK_LIST = []
        self.SECURITY_LOGIN_IP_WHITE_LIST = []
        self.SECURITY_LOGIN_IP_LIMIT_COUNT = 0
        self.SECURITY_LOGIN_IP_LIMIT_TIME = 0
        self.SECURITY_LOGIN_LIMIT_COUNT = 0
        self.SECURITY_LOGIN_LIMIT_TIME = 0
        super().__init__(**kwargs)


class EmailSettingInstance(BaseInstance):
    """ 消息通知 - 邮件设置 """
    TYPE = 'EmailSetting'

    def __init__(self, **kwargs):
        """
        :attr EMAIL_FROM: 发件人
        :attr EMAIL_HOST: 主机
        :attr EMAIL_HOST_USER: 账号
        :attr EMAIL_PORT: 端口
        :attr EMAIL_PROTOCOL: 协议
        :attr EMAIL_RECIPIENT: 测试收件人
        :attr EMAIL_SUBJECT_PREFIX: 主题前缀
        :attr EMAIL_SUFFIX: 邮件后缀
        :attr EMAIL_USE_SSL: 是否使用 SSL
        :attr EMAIL_USE_TLS: 是否使用 TLS
        """
        self.EMAIL_FROM = ''
        self.EMAIL_HOST = ''
        self.EMAIL_HOST_USER = ''
        self.EMAIL_PORT = ''
        self.EMAIL_PROTOCOL = ''
        self.EMAIL_RECIPIENT = ''
        self.EMAIL_SUBJECT_PREFIX = ''
        self.EMAIL_SUFFIX = ''
        self.EMAIL_USE_SSL = ''
        self.EMAIL_USE_TLS = ''
        super().__init__(**kwargs)


class EmailContentSettingInstance(BaseInstance):
    """ 消息通知 - 邮件设置 - 邮件内容定制 """
    TYPE = 'EmailContentSetting'

    def __init__(self, **kwargs):
        """
        :attr EMAIL_CUSTOM_USER_CREATED_BODY: 邮件内容
        :attr EMAIL_CUSTOM_USER_CREATED_HONORIFIC: 邮件问候语
        :attr EMAIL_CUSTOM_USER_CREATED_SIGNATURE: 邮件署名
        :attr EMAIL_CUSTOM_USER_CREATED_SUBJECT: 邮件主题
        """
        self.EMAIL_CUSTOM_USER_CREATED_BODY = ''
        self.EMAIL_CUSTOM_USER_CREATED_HONORIFIC = ''
        self.EMAIL_CUSTOM_USER_CREATED_SIGNATURE = ''
        self.EMAIL_CUSTOM_USER_CREATED_SUBJECT = ''
        super().__init__(**kwargs)


class BasicAuthSettingInstance(BaseInstance):
    """ 认证设置 - 基本 """
    TYPE = 'BasicAuthSetting'

    def __init__(self, **kwargs):
        """
        :attr FORGOT_PASSWORD_URL: 忘记密码 URL
        :attr LOGIN_REDIRECT_MSG_ENABLED: 启用登录跳转提示
        :attr AUTH_CAS: 是否启用 CAS
        :attr AUTH_DINGTALK: 是否启用钉钉
        :attr AUTH_FEISHU: 是否启用飞书
        :attr AUTH_LARK: 是否启用 Lark
        :attr AUTH_LDAP: 是否启用 LDAP
        :attr AUTH_OAUTH2: 是否启用 OAuth2
        :attr AUTH_OPENID: 是否启用 OpenID
        :attr AUTH_PASSKEY: 是否启用 Passkey
        :attr AUTH_RADIUS: 是否启用 Radius
        :attr AUTH_SAML2: 是否启用 SAML2
        :attr AUTH_SLACK: 是否启用 Slack
        :attr AUTH_SSO: 是否启用 SSO
        :attr AUTH_WECOM: 是否启用企业微信
        """
        self.FORGOT_PASSWORD_URL = ''
        self.LOGIN_REDIRECT_MSG_ENABLED = False
        self.AUTH_CAS = False
        self.AUTH_DINGTALK = False
        self.AUTH_FEISHU = False
        self.AUTH_LARK = False
        self.AUTH_LDAP = False
        self.AUTH_OAUTH2 = False
        self.AUTH_OPENID = False
        self.AUTH_PASSKEY = False
        self.AUTH_RADIUS = False
        self.AUTH_SAML2 = False
        self.AUTH_SLACK = False
        self.AUTH_SSO = False
        self.AUTH_WECOM = False
        super().__init__(**kwargs)


class LDAPSettingInstance(BaseInstance):
    """ 认证设置 - LDAP """
    TYPE = 'LDAPSetting'

    def __init__(self, **kwargs):
        """
        :attr AUTH_LDAP: 是否启用 LDAP
        :attr AUTH_LDAP_BIND_DN: 绑定 DN
        :attr AUTH_LDAP_BIND_PASSWORD: 密码
        :attr AUTH_LDAP_CACHE_TIMEOUT: User DN 缓存超时时间 (秒)
        :attr AUTH_LDAP_CONNECT_TIMEOUT: 连接超时时间
        :attr AUTH_LDAP_SEARCH_FILTER: 用户过滤器
        :attr AUTH_LDAP_SEARCH_OU: 用户 OU
        :attr AUTH_LDAP_SEARCH_PAGED_SIZE: 搜索分页数量 (条)
        :attr AUTH_LDAP_SERVER_URI: LDAP 地址
        :attr AUTH_LDAP_SYNC_CRONTAB: 定期执行（crontab 表达式）
        :attr AUTH_LDAP_SYNC_INTERVAL: 周期执行
        :attr AUTH_LDAP_SYNC_IS_PERIODIC: 是否启用定时任务
        :attr AUTH_LDAP_SYNC_ORG_IDS: 同步组织 ID
        :attr AUTH_LDAP_SYNC_RECEIVERS: 同步接收者
        :attr AUTH_LDAP_USER_ATTR_MAP: 用户属性映射
        """
        self.AUTH_LDAP = False
        self.AUTH_LDAP_BIND_DN = ''
        self.AUTH_LDAP_BIND_PASSWORD = ''
        self.AUTH_LDAP_CACHE_TIMEOUT = 0
        self.AUTH_LDAP_CONNECT_TIMEOUT = 0
        self.AUTH_LDAP_SEARCH_FILTER = ''
        self.AUTH_LDAP_SEARCH_OU = ''
        self.AUTH_LDAP_SEARCH_PAGED_SIZE = 0
        self.AUTH_LDAP_SERVER_URI = ''
        self.AUTH_LDAP_SYNC_CRONTAB = ''
        self.AUTH_LDAP_SYNC_INTERVAL = 0
        self.AUTH_LDAP_SYNC_IS_PERIODIC = False
        self.AUTH_LDAP_SYNC_ORG_IDS = []
        self.AUTH_LDAP_SYNC_RECEIVERS = []
        self.AUTH_LDAP_USER_ATTR_MAP = {}
        super().__init__(**kwargs)


class WecomSettingInstance(BaseInstance):
    """ 认证设置 - 企业微信 """
    TYPE = 'WecomSetting'

    def __init__(self, **kwargs):
        """
        :attr AUTH_WECOM: 是否启用企业微信
        :attr WECOM_AGENTID: agentid
        :attr WECOM_CORPID: corpid
        :attr WECOM_SECRET: secret
        """
        self.AUTH_WECOM = False
        self.WECOM_AGENTID = ''
        self.WECOM_CORPID = ''
        self.WECOM_SECRET = ''
        super().__init__(**kwargs)


class DingTalkSettingInstance(BaseInstance):
    """ 认证设置 - 钉钉 """
    TYPE = 'DingTalkSetting'

    def __init__(self, **kwargs):
        """
        :attr AUTH_DINGTALK: 是否启用钉钉
        :attr DINGTALK_AGENTID: AgentId
        :attr DINGTALK_CORPID: AppKey
        :attr DINGTALK_SECRET: AppSecret
        """
        self.AUTH_DINGTALK = False
        self.DINGTALK_AGENTID = ''
        self.DINGTALK_APPKEY = ''
        self.DINGTALK_APPSECRET = ''
        super().__init__(**kwargs)


class FeiShuSettingInstance(BaseInstance):
    """ 认证设置 - 飞书 """
    TYPE = 'FeiShuSetting'

    def __init__(self, **kwargs):
        """
        :attr AUTH_FEISHU: 是否启用飞书
        :attr FEISHU_APP_ID: App ID
        :attr FEISHU_APP_SECRET: App Secret
        """
        self.AUTH_FEISHU = False
        self.FEISHU_APP_ID = ''
        self.FEISHU_APP_SECRET = ''
        super().__init__(**kwargs)


class LarkSettingInstance(BaseInstance):
    """ 认证设置 - Lark """
    TYPE = 'LarkSetting'

    def __init__(self, **kwargs):
        """
        :attr AUTH_LARK: 是否启用 Lark
        :attr LARK_APP_ID: App ID
        :attr LARK_APP_SECRET: App Secret
        """
        self.AUTH_LARK = False
        self.LARK_APP_ID = ''
        self.LARK_APP_SECRET = ''
        super().__init__(**kwargs)


class SlackSettingInstance(BaseInstance):
    """ 认证设置 - Slack """
    TYPE = 'SlackSetting'

    def __init__(self, **kwargs):
        """
        :attr AUTH_SLACK: 是否启用 Slack
        :attr SLACK_BOT_TOKEN: Client bot Token
        :attr SLACK_CLIENT_ID: Client ID
        :attr SLACK_CLIENT_SECRET: Client Secret
        """
        self.AUTH_SLACK = False
        self.SLACK_BOT_TOKEN = ''
        self.SLACK_CLIENT_ID = ''
        self.SLACK_CLIENT_SECRET = ''
        super().__init__(**kwargs)


class OIDCSettingInstance(BaseInstance):
    """ 认证设置 - OIDC """
    TYPE = 'OIDCSetting'

    def __init__(self, **kwargs):
        """
        :attr AUTH_OPENID: 是否启用 OIDC
        :attr BASE_SITE_URL: JumpServer 地址
        :attr AUTH_OPENID_ALWAYS_UPDATE_USER: 是否总是更新用户
        :attr AUTH_OPENID_CLIENT_AUTH_METHOD: 客户端认证方法
        :attr AUTH_OPENID_CLIENT_ID: 客户端 ID
        :attr AUTH_OPENID_CLIENT_SECRET: 客户端密钥
        :attr AUTH_OPENID_CODE_CHALLENGE_METHOD: 验证校验码方式
        :attr AUTH_OPENID_ID_TOKEN_INCLUDE_CLAIMS: 是否包含声明
        :attr AUTH_OPENID_ID_TOKEN_MAX_AGE: 令牌有效时间 (秒)
        :attr AUTH_OPENID_IGNORE_SSL_VERIFICATION: 是否忽略 SSL 证书验证
        :attr AUTH_OPENID_KEYCLOAK: 是否启用 Keycloak
        :attr AUTH_OPENID_PKCE: 是否启用 PKCE
        :attr AUTH_OPENID_PROVIDER_AUTHORIZATION_ENDPOINT: 授权端点地址
        :attr AUTH_OPENID_PROVIDER_ENDPOINT: 端点地址
        :attr AUTH_OPENID_PROVIDER_END_SESSION_ENDPOINT: 注销会话端点地址
        :attr AUTH_OPENID_PROVIDER_JWKS_ENDPOINT: jwks 端点地址
        :attr AUTH_OPENID_PROVIDER_SIGNATURE_ALG: 签名算法
        :attr AUTH_OPENID_PROVIDER_SIGNATURE_KEY: 签名 Key
        :attr AUTH_OPENID_PROVIDER_TOKEN_ENDPOINT: token 端点地址
        :attr AUTH_OPENID_PROVIDER_USERINFO_ENDPOINT: 用户信息端点地址
        :attr AUTH_OPENID_REALM_NAME: 域
        :attr AUTH_OPENID_SCOPES: 连接范围
        :attr AUTH_OPENID_SERVER_URL: 服务器地址
        :attr AUTH_OPENID_SHARE_SESSION: 是否共享会话
        :attr AUTH_OPENID_USER_ATTR_MAP: 用户属性映射
        :attr AUTH_OPENID_USE_NONCE: 是否临时使用
        :attr AUTH_OPENID_USE_STATE: 是否使用状态
        """
        self.AUTH_OPENID = False
        self.BASE_SITE_URL = ''
        self.AUTH_OPENID_ALWAYS_UPDATE_USER = False
        self.AUTH_OPENID_CLIENT_AUTH_METHOD = ''
        self.AUTH_OPENID_CLIENT_ID = ''
        self.AUTH_OPENID_CLIENT_SECRET = ''
        self.AUTH_OPENID_CODE_CHALLENGE_METHOD = ''
        self.AUTH_OPENID_ID_TOKEN_INCLUDE_CLAIMS = False
        self.AUTH_OPENID_ID_TOKEN_MAX_AGE = 0
        self.AUTH_OPENID_IGNORE_SSL_VERIFICATION = False
        self.AUTH_OPENID_KEYCLOAK = False
        self.AUTH_OPENID_PKCE = False
        self.AUTH_OPENID_PROVIDER_AUTHORIZATION_ENDPOINT = ''
        self.AUTH_OPENID_PROVIDER_ENDPOINT = ''
        self.AUTH_OPENID_PROVIDER_END_SESSION_ENDPOINT = ''
        self.AUTH_OPENID_PROVIDER_JWKS_ENDPOINT = ''
        self.AUTH_OPENID_PROVIDER_SIGNATURE_ALG = ''
        self.AUTH_OPENID_PROVIDER_SIGNATURE_KEY = ''
        self.AUTH_OPENID_PROVIDER_TOKEN_ENDPOINT = ''
        self.AUTH_OPENID_PROVIDER_USERINFO_ENDPOINT = ''
        self.AUTH_OPENID_REALM_NAME = ''
        self.AUTH_OPENID_SCOPES = ''
        self.AUTH_OPENID_SERVER_URL = ''
        self.AUTH_OPENID_SHARE_SESSION = False
        self.AUTH_OPENID_USER_ATTR_MAP = {}
        self.AUTH_OPENID_USE_NONCE = False
        self.AUTH_OPENID_USE_STATE = False
        super().__init__(**kwargs)


class RadiusSettingInstance(BaseInstance):
    """ 认证设置 - Radius """
    TYPE = 'RadiusSetting'

    def __init__(self, **kwargs):
        """
        :attr AUTH_RADIUS: 是否启用 Radius
        :attr OTP_IN_RADIUS: 是否启用 Radius OTP
        :attr RADIUS_PORT: 端口
        :attr RADIUS_SECRET: 密钥
        :attr RADIUS_SERVER: 主机
        """
        self.AUTH_RADIUS = False
        self.OTP_IN_RADIUS = False
        self.RADIUS_PORT = 1812
        self.RADIUS_SECRET = ''
        self.RADIUS_SERVER = ''
        super().__init__(**kwargs)


class CASSettingInstance(BaseInstance):
    """ 认证设置 - CAS """
    TYPE = 'CASSetting'

    def __init__(self, **kwargs):
        """
        :attr AUTH_CAS: 是否启用 CAS
        :attr CAS_APPLY_ATTRIBUTES_TO_USER: 是否将 CAS 属性应用到用户
        :attr CAS_CREATE_USER: 创建用户(如果不存在)
        :attr CAS_LOGOUT_COMPLETELY: 是否同步注销
        :attr CAS_RENAME_ATTRIBUTES: 用户属性映射
        :attr CAS_ROOT_PROXIED_AS: 回调地址
        :attr CAS_SERVER_URL: 服务端地址
        :attr CAS_USERNAME_ATTRIBUTE: CAS 用户名属性
        :attr CAS_VERSION: 版本
        """
        self.AUTH_CAS = False
        self.CAS_APPLY_ATTRIBUTES_TO_USER = False
        self.CAS_CREATE_USER = False
        self.CAS_LOGOUT_COMPLETELY = False
        self.CAS_RENAME_ATTRIBUTES = {}
        self.CAS_ROOT_PROXIED_AS = ''
        self.CAS_SERVER_URL = ''
        self.CAS_USERNAME_ATTRIBUTE = ''
        self.CAS_VERSION = ''
        super().__init__(**kwargs)


class SAML2SettingInstance(BaseInstance):
    """ 认证设置 - SAML2 """
    TYPE = 'SAML2Setting'

    def __init__(self, **kwargs):
        """
        :attr AUTH_SAML2: 是否开启 SAML2
        :attr AUTH_SAML2_ALWAYS_UPDATE_USER: 是否总是更新用户信息
        :attr SAML2_IDP_METADATA_URL: IDP metadata URL
        :attr SAML2_IDP_METADATA_XML: IDP metadata XML
        :attr SAML2_LOGOUT_COMPLETELY: 是否同步注销
        :attr SAML2_RENAME_ATTRIBUTES: 用户属性映射
        :attr SAML2_SP_ADVANCED_SETTINGS: 高级配置
        """
        self.AUTH_SAML2 = False
        self.AUTH_SAML2_ALWAYS_UPDATE_USER = False
        self.SAML2_IDP_METADATA_URL = ''
        self.SAML2_IDP_METADATA_XML = ''
        self.SAML2_LOGOUT_COMPLETELY = False
        self.SAML2_RENAME_ATTRIBUTES = {}
        self.SAML2_SP_ADVANCED_SETTINGS = {}
        super().__init__(**kwargs)


class OAuth2SettingInstance(BaseInstance):
    """ 认证设置 - OAuth2 """
    TYPE = 'OAuth2Setting'

    def __init__(self, **kwargs):
        """
        :attr AUTH_OAUTH2: 是否开启 OAuth2
        :attr AUTH_OAUTH2_ACCESS_TOKEN_ENDPOINT: token 端点地址
        :attr AUTH_OAUTH2_ACCESS_TOKEN_METHOD: Token 获取方法
        :attr AUTH_OAUTH2_ALWAYS_UPDATE_USER: 是否总是更新用户信息
        :attr AUTH_OAUTH2_CLIENT_ID: 客户端 ID
        :attr AUTH_OAUTH2_CLIENT_SECRET: 客户端密钥
        :attr AUTH_OAUTH2_LOGOUT_COMPLETELY: 是否同步注销
        :attr AUTH_OAUTH2_LOGO_PATH: 图标地址
        :attr AUTH_OAUTH2_PROVIDER: 服务提供商
        :attr AUTH_OAUTH2_PROVIDER_AUTHORIZATION_ENDPOINT: 授权端点地址
        :attr AUTH_OAUTH2_PROVIDER_USERINFO_ENDPOINT: 用户信息端点地址
        :attr AUTH_OAUTH2_SCOPE: 范围
        :attr AUTH_OAUTH2_USER_ATTR_MAP: 用户属性映射
        """
        self.AUTH_OAUTH2 = False
        self.AUTH_OAUTH2_ACCESS_TOKEN_ENDPOINT = ''
        self.AUTH_OAUTH2_ACCESS_TOKEN_METHOD = ''
        self.AUTH_OAUTH2_ALWAYS_UPDATE_USER = False
        self.AUTH_OAUTH2_CLIENT_ID = ''
        self.AUTH_OAUTH2_CLIENT_SECRET = ''
        self.AUTH_OAUTH2_LOGOUT_COMPLETELY = False
        self.AUTH_OAUTH2_LOGO_PATH = ''
        self.AUTH_OAUTH2_PROVIDER = ''
        self.AUTH_OAUTH2_PROVIDER_AUTHORIZATION_ENDPOINT = ''
        self.AUTH_OAUTH2_PROVIDER_END_SESSION_ENDPOINT = ''
        self.AUTH_OAUTH2_PROVIDER_USERINFO_ENDPOINT = ''
        self.AUTH_OAUTH2_SCOPE = ''
        self.AUTH_OAUTH2_USER_ATTR_MAP = ''
        super().__init__(**kwargs)


class PasskeySettingInstance(BaseInstance):
    """ 认证设置 - Passkey """
    TYPE = 'PasskeySetting'

    def __init__(self, **kwargs):
        """
        :attr AUTH_PASSKEY: 是否启用 Passkey
        :attr FIDO_SERVER_ID: Passkey 服务域名
        :attr FIDO_SERVER_NAME: Passkey 服务名称
        """
        self.AUTH_PASSKEY = False
        self.FIDO_SERVER_ID = ''
        self.FIDO_SERVER_NAME = ''
        super().__init__(**kwargs)


class CleanSettingInstance(BaseInstance):
    """ 系统任务 - 定期清理 """
    TYPE = 'CleanSetting'

    def __init__(self, **kwargs):
        """
        :attr ACTIVITY_LOG_KEEP_DAYS: 保留活动记录天数
        :attr CLOUD_SYNC_TASK_EXECUTION_KEEP_DAYS: 保留云同步记录天数
        :attr FTP_LOG_KEEP_DAYS: 保留上传下载记录天数
        :attr JOB_EXECUTION_KEEP_DAYS: 保留作业中心执行历史记录天数
        :attr LOGIN_LOG_KEEP_DAYS: 保留登陆日志天数
        :attr OPERATE_LOG_KEEP_DAYS: 保留操作日志天数
        :attr PASSWORD_CHANGE_LOG_KEEP_DAYS: 保留用户改密日志天数
        :attr TASK_LOG_KEEP_DAYS: 保留任务日志天数
        :attr TERMINAL_SESSION_KEEP_DURATION: 保留会话日志天数
        """
        self.ACTIVITY_LOG_KEEP_DAYS = 0
        self.CLOUD_SYNC_TASK_EXECUTION_KEEP_DAYS = 0
        self.FTP_LOG_KEEP_DAYS = 0
        self.JOB_EXECUTION_KEEP_DAYS = 0
        self.LOGIN_LOG_KEEP_DAYS = 0
        self.OPERATE_LOG_KEEP_DAYS = 0
        self.PASSWORD_CHANGE_LOG_KEEP_DAYS = 0
        self.TASK_LOG_KEEP_DAYS = 0
        self.TERMINAL_SESSION_KEEP_DURATION = 0
        super().__init__(**kwargs)


class SMSSettingInstance(BaseInstance):
    """ 消息通知 - 短信设置 """
    TYPE = 'SMSSetting'

    def __init__(self, **kwargs):
        """
        :attr SMS_ENABLED: 是否启用短信
        :attr SMS_BACKEND: 短信后端
        :attr SMS_CODE_LENGTH: 短信验证码长度
        """
        self.SMS_ENABLED = False
        self.SMS_BACKEND = ''
        self.SMS_CODE_LENGTH = ''
        super().__init__(**kwargs)


class AlibabaSMSSettingInstance(BaseInstance):
    """ 消息通知 - 短信设置 - 阿里短信设置 """
    TYPE = 'AlibabaSMSSetting'

    def __init__(self, **kwargs):
        """
        :attr ALIBABA_ACCESS_KEY_ID: AccessKey ID
        :attr ALIBABA_ACCESS_KEY_SECRET: AccessKey Secret
        :attr ALIBABA_VERIFY_SIGN_NAME: 短信签名
        :attr ALIBABA_VERIFY_TEMPLATE_CODE: 短信模板
        :attr SMS_TEST_PHONE: 测试手机号
        """
        self.ALIBABA_ACCESS_KEY_ID = ''
        self.ALIBABA_ACCESS_KEY_SECRET = ''
        self.ALIBABA_VERIFY_SIGN_NAME = ''
        self.ALIBABA_VERIFY_TEMPLATE_CODE = ''
        self.SMS_TEST_PHONE = {}
        super().__init__(**kwargs)


class TencentSMSSettingInstance(BaseInstance):
    """ 消息通知 - 短信设置 - 腾讯短信设置 """
    TYPE = 'TencentSMSSetting'

    def __init__(self, **kwargs):
        """
        :attr TENCENT_SDKAPPID: SDK APP ID
        :attr TENCENT_SECRET_ID: Secret ID
        :attr TENCENT_SECRET_KEY: Secret Key
        :attr TENCENT_VERIFY_SIGN_NAME: 短信签名
        :attr TENCENT_VERIFY_TEMPLATE_CODE: 短信模板
        :attr SMS_TEST_PHONE: 测试手机号
        """
        self.TENCENT_SDKAPPID = ''
        self.TENCENT_SECRET_ID = ''
        self.TENCENT_SECRET_KEY = ''
        self.TENCENT_VERIFY_SIGN_NAME = ''
        self.TENCENT_VERIFY_TEMPLATE_CODE = ''
        super().__init__(**kwargs)


class HuaweiSMSSettingInstance(BaseInstance):
    """ 消息通知 - 短信设置 - 华为短信设置 """
    TYPE = 'HuaweiSMSSetting'

    def __init__(self, **kwargs):
        """
        :attr HUAWEI_APP_KEY: App Key
        :attr HUAWEI_APP_SECRET: App Secret
        :attr HUAWEI_SIGN_CHANNEL_NUM: 签名通道号
        :attr HUAWEI_SMS_ENDPOINT: 应用接入地址
        :attr HUAWEI_VERIFY_SIGN_NAME: 签名
        :attr HUAWEI_VERIFY_TEMPLATE_CODE: 模板
        :attr SMS_TEST_PHONE: 测试手机号
        """
        self.HUAWEI_APP_KEY = ''
        self.HUAWEI_APP_SECRET = ''
        self.HUAWEI_SIGN_CHANNEL_NUM = ''
        self.HUAWEI_SMS_ENDPOINT = ''
        self.HUAWEI_VERIFY_SIGN_NAME = ''
        self.HUAWEI_VERIFY_TEMPLATE_CODE = ''
        self.SMS_TEST_PHONE = {}
        super().__init__(**kwargs)


class CMPP2SMSSettingInstance(BaseInstance):
    """ 消息通知 - 短信设置 - CMPP2 短信设置 """
    TYPE = 'CMPP2SMSSetting'

    def __init__(self, **kwargs):
        """
        :attr CMPP2_HOST: 主机
        :attr CMPP2_PORT: 端口
        :attr CMPP2_SERVICE_ID: 业务类型
        :attr CMPP2_SP_ID: 企业代码
        :attr CMPP2_SP_SECRET: 共享密码
        :attr CMPP2_SRC_ID: 原始号码
        :attr CMPP2_VERIFY_SIGN_NAME: 签名
        :attr CMPP2_VERIFY_TEMPLATE_CODE: 模板
        :attr SMS_TEST_PHONE: 测试手机号
        """
        self.CMPP2_HOST = ''
        self.CMPP2_PORT = 7890
        self.CMPP2_SERVICE_ID = ''
        self.CMPP2_SP_ID = ''
        self.CMPP2_SP_SECRET = ''
        self.CMPP2_SRC_ID = ''
        self.CMPP2_VERIFY_SIGN_NAME = ''
        self.CMPP2_VERIFY_TEMPLATE_CODE = ''
        self.SMS_TEST_PHONE = {}
        super().__init__(**kwargs)


class CustomSMSSettingInstance(BaseInstance):
    """ 消息通知 - 短信设置 - 自定义短信设置 """
    TYPE = 'CustomSMSSetting'

    def __init__(self, **kwargs):
        """
        :attr CUSTOM_SMS_API_PARAMS: 短信请求参数
        :attr CUSTOM_SMS_REQUEST_METHOD: 短信 URL 请求方法
        :attr CUSTOM_SMS_URL: 短信平台 URL
        :attr SMS_TEST_PHONE: 测试手机号
        :attr kwargs:
        """
        self.CUSTOM_SMS_API_PARAMS = {}
        self.CUSTOM_SMS_REQUEST_METHOD = ''
        self.CUSTOM_SMS_URL = ''
        self.SMS_TEST_PHONE = {}
        super().__init__(**kwargs)


class VaultSettingInstance(BaseInstance):
    """ 功能设置 - 账号存储 """
    TYPE = 'VaultSetting'

    def __init__(self, **kwargs):
        """
        :attr VAULT_ENABLED: 是否启用账号存储
        :attr VAULT_HCP_HOST: HashiCorp Vault 主机
        :attr VAULT_HCP_MOUNT_POINT: HashiCorp Vault 挂载点
        :attr HISTORY_ACCOUNT_CLEAN_LIMIT: 历史账号保留数量
        """
        self.VAULT_ENABLED = False
        self.VAULT_HCP_HOST = ''
        self.VAULT_HCP_MOUNT_POINT = ''
        self.HISTORY_ACCOUNT_CLEAN_LIMIT = 999
        super().__init__(**kwargs)


class ChatSettingInstance(BaseInstance):
    """ 功能设置 - 智能问答 """
    TYPE = 'ChatSetting'

    def __init__(self, **kwargs):
        """
        :attr CHAT_ENABLED: 是否启用智能问答
        :attr GPT_API_KEY: API Key
        :attr GPT_BASE_URL: 基本地址
        :attr GPT_MODEL: GPT 模型
        :attr GPT_PROXY: 代理
        :param kwargs:
        """
        self.CHAT_AI_ENABLED = False
        self.GPT_API_KEY = ''
        self.GPT_BASE_URL = ''
        self.GPT_MODEL = ''
        self.GPT_PROXY = ''
        super().__init__(**kwargs)


class AnnouncementSettingInstance(BaseInstance):
    """ 功能设置 - 公告 """
    TYPE = 'AnnouncementSetting'

    def __init__(self, **kwargs):
        """
        :attr ANNOUNCEMENT_ENABLED: 是否启用公告
        :attr ANNOUNCEMENT: 公告内容
        """
        self.ANNOUNCEMENT_ENABLED = False
        self.ANNOUNCEMENT = {
            'CONTENT': '', 'ID': '', 'LINK': '', 'SUBJECT': ''
        }
        super().__init__(**kwargs)


class TicketSettingInstance(BaseInstance):
    """ 功能设置 - 工单 """
    TYPE = 'TicketSetting'

    def __init__(self, **kwargs):
        """
        :attr TICKETS_DIRECT_APPROVE: 免登陆审批
        :attr TICKETS_ENABLED: 是否启用工单
        :attr TICKET_AUTHORIZE_DEFAULT_TIME: 默认授权时间
        :attr TICKET_AUTHORIZE_DEFAULT_TIME_UNIT: 默认授权时间单位，day/hour
        """
        self.TICKETS_DIRECT_APPROVE = False
        self.TICKETS_ENABLED = True
        self.TICKET_AUTHORIZE_DEFAULT_TIME = 1
        self.TICKET_AUTHORIZE_DEFAULT_TIME_UNIT = 'day'
        super().__init__(**kwargs)


class OPSSettingInstance(BaseInstance):
    """ 功能设置 - 任务中心 """
    TYPE = 'OPSSetting'

    def __init__(self, **kwargs):
        """
        :attr SECURITY_COMMAND_EXECUTION: 是否启用任务中心
        :attr SECURITY_COMMAND_BLACKLIST: 作业中心命令黑名单
        """
        self.SECURITY_COMMAND_EXECUTION = True
        self.SECURITY_COMMAND_BLACKLIST = []
        super().__init__(**kwargs)


class VirtualAPPSettingInstance(BaseInstance):
    """ 功能设置 - 虚拟应用 """
    TYPE = 'VirtualSetting'

    def __init__(self, **kwargs):
        """
        :attr VIRTUAL_APP_ENABLED: 是否启用虚拟应用
        """
        self.VIRTUAL_APP_ENABLED = False
        super().__init__(**kwargs)
