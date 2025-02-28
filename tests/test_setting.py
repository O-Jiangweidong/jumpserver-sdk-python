import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.settings import (
    DetailBasicSettingRequest, DetailTerminalSettingRequest,
    DetailSecurityAuthSettingRequest, DetailSecuritySessionSettingRequest,
    DetailSecurityPasswordSettingRequest, DetailSecurityLoginLimitSettingRequest,
    DetailEmailSettingRequest, DetailEmailContentSettingRequest,
    DetailBasicAuthSettingRequest, DetailLDAPSettingRequest,
    DetailWecomSettingRequest, DetailDingTalkSettingRequest,
    DetailFeiShuSettingRequest,
    DetailSlackSettingRequest, DetailOIDCSettingRequest,
    DetailRadiusSettingRequest, DetailCASSettingRequest,
    DetailSAML2SettingRequest, DetailOAuth2SettingRequest,
    DetailPasskeySettingRequest, DetailCleanSettingRequest,
    DetailSMSSettingRequest, DetailAlibabaSMSSettingRequest,
    DetailTencentSMSSettingRequest, DetailHuaweiSMSSettingRequest,
    DetailCMPP2SMSSettingRequest, DetailCustomSMSSettingRequest,
    DetailVaultSettingRequest, DetailChatSettingRequest,
    DetailAnnouncementSettingRequest, DetailTicketSettingRequest,
    DetailOPSSettingRequest, DetailVirtualAPPSettingRequest
)
from jms_client.v1.models.instance.settings import (
    BasicSettingInstance, TerminalSettingInstance, SecurityAuthSettingInstance,
    SecuritySessionSettingInstance, SecurityPasswordSettingInstance,
    SecurityLoginLimitSettingInstance, EmailSettingInstance,
    EmailContentSettingInstance, BasicAuthSettingInstance,
    LDAPSettingInstance, WecomSettingInstance, DingTalkSettingInstance,
    FeiShuSettingInstance, SlackSettingInstance, OIDCSettingInstance,
    RadiusSettingInstance, CASSettingInstance, SAML2SettingInstance,
    OAuth2SettingInstance, PasskeySettingInstance, CleanSettingInstance,
    SMSSettingInstance, AlibabaSMSSettingInstance, TencentSMSSettingInstance,
    HuaweiSMSSettingInstance, CMPP2SMSSettingInstance, CustomSMSSettingInstance,
    VaultSettingInstance, ChatSettingInstance, AnnouncementSettingInstance,
    TicketSettingInstance, OPSSettingInstance, VirtualAPPSettingInstance
)
from jms_client.v1.models.response import Response


class TestFunctionality(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        config = configparser.ConfigParser()
        config.read('config.ini')
        username = config['test']['username']
        password = config['test']['password']
        web_url = config['test']['web_url']
        version = config['test']['version']
        self.client: Client = get_client(
            version=version, web_url=web_url,
            username=username, password=password
        )
        self.client.set_org(self.client.root_org)

    def test_detail_basic_setting(self):
        """ 测试查询 '基本设置 - 基本' 详情 """
        request = DetailBasicSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), BasicSettingInstance)

    def test_detail_terminal_setting(self):
        """ 测试查询 '组件设置 - 基本设置' 详情 """
        request = DetailTerminalSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), TerminalSettingInstance)

    def test_detail_security_auth_setting(self):
        """ 测试查询 '安全设置 - 认证安全' 详情 """
        request = DetailSecurityAuthSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), SecurityAuthSettingInstance)

    def test_detail_security_session_setting(self):
        """ 测试查询 '安全设置 - 会话安全' 详情 """
        request = DetailSecuritySessionSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), SecuritySessionSettingInstance)

    def test_detail_security_password_setting(self):
        """ 测试查询 '安全设置 - 密码安全' 详情 """
        request = DetailSecurityPasswordSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), SecurityPasswordSettingInstance)

    def test_detail_security_login_limit_setting(self):
        """ 测试查询 '安全设置 - 登录限制' 详情 """
        request = DetailSecurityLoginLimitSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), SecurityLoginLimitSettingInstance)

    def test_detail_email_setting(self):
        """ 测试查询 '消息通知 - 邮件设置' 详情 """
        request = DetailEmailSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), EmailSettingInstance)

    def test_detail_email_content_setting(self):
        """ 测试查询 '消息通知 - 邮件设置 - 邮件内容定制' 详情 """
        request = DetailEmailContentSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), EmailContentSettingInstance)

    def test_detail_basic_auth_setting(self):
        """ 测试查询 '认证设置 - 基本' 详情 """
        request = DetailBasicAuthSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), BasicAuthSettingInstance)

    def test_detail_ldap_setting(self):
        """ 测试查询 '认证设置 - LDAP' 详情 """
        request = DetailLDAPSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), LDAPSettingInstance)

    def test_detail_wecom_setting(self):
        """ 测试查询 '认证设置 - 企业微信' 详情 """
        request = DetailWecomSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), WecomSettingInstance)

    def test_detail_saml2_setting(self):
        """ 测试查询 '认证设置 - SAML2' 详情 """
        request = DetailSAML2SettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), SAML2SettingInstance)

    def test_detail_dingtalk_setting(self):
        """ 测试查询 '认证设置 - 钉钉' 详情 """
        request = DetailDingTalkSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), DingTalkSettingInstance)

    def test_detail_feishu_setting(self):
        """ 测试查询 '认证设置 - 飞书' 详情 """
        request = DetailFeiShuSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), FeiShuSettingInstance)

    def test_detail_slack_setting(self):
        """ 测试查询 '认证设置 - Slack' 详情 """
        request = DetailSlackSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), SlackSettingInstance)

    def test_detail_oidc_setting(self):
        """ 测试查询 '认证设置 - OIDC' 详情 """
        request = DetailOIDCSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), OIDCSettingInstance)

    def test_detail_radius_setting(self):
        """ 测试查询 '认证设置 - RADIUS' 详情 """
        request = DetailRadiusSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), RadiusSettingInstance)

    def test_detail_cas_setting(self):
        """ 测试查询 '认证设置 - CAS' 详情 """
        request = DetailCASSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), CASSettingInstance)

    def test_detail_oauth2_setting(self):
        """ 测试查询 '认证设置 - OAuth2' 详情 """
        request = DetailOAuth2SettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), OAuth2SettingInstance)

    def test_detail_passkey_setting(self):
        """ 测试查询 '认证设置 - Passkey' 详情 """
        request = DetailPasskeySettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), PasskeySettingInstance)

    def test_detail_clean_setting(self):
        """ 测试查询 '系统任务 - 定期清理' 详情 """
        request = DetailCleanSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), CleanSettingInstance)

    def test_detail_sms_setting(self):
        """ 测试查询 '消息通知 - 短信设置' 详情 """
        request = DetailSMSSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), SMSSettingInstance)

    def test_detail_alibaba_sms_setting(self):
        """ 测试查询 '消息通知 - 短信设置 - 阿里云' 详情 """
        request = DetailAlibabaSMSSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AlibabaSMSSettingInstance)

    def test_detail_tencent_sms_setting(self):
        """ 测试查询 '消息通知 - 短信设置 - 腾讯云' 详情 """
        request = DetailTencentSMSSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), TencentSMSSettingInstance)

    def test_detail_huawei_sms_setting(self):
        """ 测试查询 '消息通知 - 短信设置 - 华为云' 详情 """
        request = DetailHuaweiSMSSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), HuaweiSMSSettingInstance)

    def test_detail_cmpp2_sms_setting(self):
        """ 测试查询 '消息通知 - 短信设置 - CMPP2' 详情 """
        request = DetailCMPP2SMSSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), CMPP2SMSSettingInstance)

    def test_detail_custom_sms_setting(self):
        """ 测试查询 '消息通知 - 短信设置 - 自定义' 详情 """
        request = DetailCustomSMSSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), CustomSMSSettingInstance)

    def test_detail_vault_setting(self):
        """ 测试查询 '功能设置 - 账号存储' 详情 """
        request = DetailVaultSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), VaultSettingInstance)

    def test_detail_chat_setting(self):
        """ 测试查询 '功能设置 - 智能问答' 详情 """
        request = DetailChatSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), ChatSettingInstance)

    def test_detail_announcement_setting(self):
        """ 测试查询 '功能设置 - 公告' 详情 """
        request = DetailAnnouncementSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AnnouncementSettingInstance)

    def test_detail_ticket_setting(self):
        """ 测试查询 '功能设置 - 工单' 详情 """
        request = DetailTicketSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), TicketSettingInstance)

    def test_detail_ops_setting(self):
        """ 测试查询 '功能设置 - 任务中心' 详情 """
        request = DetailOPSSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), OPSSettingInstance)

    def test_detail_virtual_app_setting(self):
        """ 测试查询 '功能设置 - 虚拟应用' 详情 """
        request = DetailVirtualAPPSettingRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), VirtualAPPSettingInstance)


if __name__ == '__main__':
    unittest.main()
