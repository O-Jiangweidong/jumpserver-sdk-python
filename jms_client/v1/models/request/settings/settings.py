from jms_client.v1.models.instance.settings import (
    BasicSettingInstance, TerminalSettingInstance, SecurityAuthSettingInstance,
    SecuritySessionSettingInstance, SecurityPasswordSettingInstance,
    SecurityLoginLimitSettingInstance, EmailSettingInstance,
    EmailContentSettingInstance, BasicAuthSettingInstance,
    LDAPSettingInstance, WecomSettingInstance, DingTalkSettingInstance,
    FeiShuSettingInstance, LarkSettingInstance, SlackSettingInstance,
    OIDCSettingInstance, RadiusSettingInstance, CASSettingInstance,
    SAML2SettingInstance, OAuth2SettingInstance, PasskeySettingInstance,
    CleanSettingInstance,SMSSettingInstance, AlibabaSMSSettingInstance,
    TencentSMSSettingInstance, HuaweiSMSSettingInstance, CMPP2SMSSettingInstance,
    CustomSMSSettingInstance, VaultSettingInstance,ChatSettingInstance,
    AnnouncementSettingInstance, TicketSettingInstance, OPSSettingInstance,
    VirtualAPPSettingInstance,
)
from ..common import Request


class BaseSettingRequest(Request):
    URL = 'settings/setting/'


class DetailBasicSettingRequest(BaseSettingRequest):
    """ 查询 '基本设置 - 基本' 详情 """
    InstanceClass = BasicSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='basic', **kwargs)


class DetailTerminalSettingRequest(BaseSettingRequest):
    """ 查询 '组件设置 - 基本设置' 详情 """
    InstanceClass = TerminalSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='terminal', **kwargs)


class DetailSecurityAuthSettingRequest(BaseSettingRequest):
    """ 查询 '安全设置 - 认证安全' 详情 """
    InstanceClass = SecurityAuthSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='security_auth', **kwargs)


class DetailSecuritySessionSettingRequest(BaseSettingRequest):
    """ 查询 '安全设置 - 会话安全' 详情 """
    InstanceClass = SecuritySessionSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='security_session', **kwargs)


class DetailSecurityPasswordSettingRequest(BaseSettingRequest):
    """ 查询 '安全设置 - 密码安全' 详情 """
    InstanceClass = SecurityPasswordSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='security_password', **kwargs)


class DetailSecurityLoginLimitSettingRequest(BaseSettingRequest):
    """ 查询 '安全设置 - 登录限制' 详情 """
    InstanceClass = SecurityLoginLimitSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='security_login_limit', **kwargs)


class DetailEmailSettingRequest(BaseSettingRequest):
    """ 查询 '消息通知 - 邮件设置' 详情 """
    InstanceClass = EmailSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='email', **kwargs)


class DetailEmailContentSettingRequest(BaseSettingRequest):
    """ 查询 '消息通知 - 邮件设置 - 邮件内容定制' 详情 """
    InstanceClass = EmailContentSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='email_content', **kwargs)


class DetailBasicAuthSettingRequest(BaseSettingRequest):
    """ 查询 '认证设置 - 基本' 详情 """
    InstanceClass = BasicAuthSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='auth', **kwargs)


class DetailLDAPSettingRequest(BaseSettingRequest):
    """ 查询 '认证设置 - LDAP' 详情 """
    InstanceClass = LDAPSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='ldap', **kwargs)


class DetailWecomSettingRequest(BaseSettingRequest):
    """ 查询 '认证设置 - 企业微信' 详情 """
    InstanceClass = WecomSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='wecom', **kwargs)


class DetailDingTalkSettingRequest(BaseSettingRequest):
    """ 查询 '认证设置 - 钉钉' 详情 """
    InstanceClass = DingTalkSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='dingtalk', **kwargs)


class DetailFeiShuSettingRequest(BaseSettingRequest):
    """ 查询 '认证设置 - 飞书' 详情 """
    InstanceClass = FeiShuSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='feishu', **kwargs)


class DetailLarkSettingRequest(BaseSettingRequest):
    """ 查询 '认证设置 - Lark' 详情 """
    InstanceClass = LarkSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='lark', **kwargs)


class DetailSlackSettingRequest(BaseSettingRequest):
    """ 查询 '认证设置 - Slack' 详情 """
    InstanceClass = SlackSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='slack', **kwargs)


class DetailOIDCSettingRequest(BaseSettingRequest):
    """ 查询 '认证设置 - OIDC' 详情 """
    InstanceClass = OIDCSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='oidc', **kwargs)


class DetailRadiusSettingRequest(BaseSettingRequest):
    """ 查询 '认证设置 - Radius' 详情 """
    InstanceClass = RadiusSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='radius', **kwargs)


class DetailCASSettingRequest(BaseSettingRequest):
    """ 查询 '认证设置 - CAS' 详情 """
    InstanceClass = CASSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='cas', **kwargs)


class DetailSAML2SettingRequest(BaseSettingRequest):
    """ 查询 '认证设置 - SAML2' 详情 """
    InstanceClass = SAML2SettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='saml2', **kwargs)


class DetailOAuth2SettingRequest(BaseSettingRequest):
    """ 查询 '认证设置 - OAuth2' 详情 """
    InstanceClass = OAuth2SettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='oauth2', **kwargs)


class DetailPasskeySettingRequest(BaseSettingRequest):
    """ 查询 '认证设置 - Passkey' 详情 """
    InstanceClass = PasskeySettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='passkey', **kwargs)


class DetailCleanSettingRequest(BaseSettingRequest):
    """ 查询 '系统任务 - 定期清理' 详情 """
    InstanceClass = CleanSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='clean', **kwargs)


class DetailSMSSettingRequest(BaseSettingRequest):
    """ 查询 '消息通知 - 短信设置' 详情 """
    InstanceClass = SMSSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='sms', **kwargs)


class DetailAlibabaSMSSettingRequest(BaseSettingRequest):
    """ 查询 '消息通知 - 短信设置 - 阿里短信设置' 详情 """
    InstanceClass = AlibabaSMSSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='alibaba', **kwargs)


class DetailTencentSMSSettingRequest(BaseSettingRequest):
    """ 查询 '消息通知 - 短信设置 - 腾讯短信设置' 详情 """
    InstanceClass = TencentSMSSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='tencent', **kwargs)


class DetailHuaweiSMSSettingRequest(BaseSettingRequest):
    """ 查询 '消息通知 - 短信设置 - 华为短信设置' 详情 """
    InstanceClass = HuaweiSMSSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='huawei', **kwargs)


class DetailCMPP2SMSSettingRequest(BaseSettingRequest):
    """ 查询 '消息通知 - 短信设置 - CMPP2 短信设置' 详情 """
    InstanceClass = CMPP2SMSSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='cmpp2', **kwargs)


class DetailCustomSMSSettingRequest(BaseSettingRequest):
    """ 查询 '消息通知 - 短信设置 - 自定义短信设置' 详情 """
    InstanceClass = CustomSMSSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='custom', **kwargs)


class DetailVaultSettingRequest(BaseSettingRequest):
    """ 查询 '功能设置 - 账号存储' 详情 """
    InstanceClass = VaultSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='vault', **kwargs)


class DetailChatSettingRequest(BaseSettingRequest):
    """ 查询 '功能设置 - 智能问答' 详情 """
    InstanceClass = ChatSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='chat', **kwargs)


class DetailAnnouncementSettingRequest(BaseSettingRequest):
    """ 查询 '功能设置 - 公告' 详情 """
    InstanceClass = AnnouncementSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='announcement', **kwargs)


class DetailTicketSettingRequest(BaseSettingRequest):
    """ 查询 '功能设置 - 工单' 详情 """
    InstanceClass = TicketSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='ticket', **kwargs)


class DetailOPSSettingRequest(BaseSettingRequest):
    """ 查询 '功能设置 - 任务中心' 详情 """
    InstanceClass = OPSSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='ops', **kwargs)


class DetailVirtualAPPSettingRequest(BaseSettingRequest):
    """ 查询 '功能设置 - 虚拟应用' 详情 """
    InstanceClass = VirtualAPPSettingInstance

    def __init__(self, **kwargs):
        super().__init__(category='virtualapp', **kwargs)
