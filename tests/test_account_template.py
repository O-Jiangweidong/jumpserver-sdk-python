import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.accounts.account_templates import (
    DescribeAccountTemplatesRequest, DetailAccountTemplateRequest,
    CreateAccountTemplateRequest, UpdateAccountTemplateRequest,
    DeleteAccountTemplateRequest, SyncAccountTemplateInfoRequest,
    SecretParam, ProtocolParam, PushParams
)
from jms_client.v1.models.instance.accounts.account_templates import (
    AccountTemplateInstance
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
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')

    def test_list_account_templates(self):
        """ 测试获取账号模板列表 """
        protocols = ProtocolParam().append_ssh()
        request = DescribeAccountTemplatesRequest(limit=20, protocols=protocols)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_account_template(self):
        """ 测试获取指定 ID 账号模板详情 """
        request = DetailAccountTemplateRequest(id_='079ec32d-1b9e-459a-85d9-cf0ccec01dab')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AccountTemplateInstance)

    def test_create_account_template(self):
        """ 测试创建账号模板 """
        secret = SecretParam()
        secret.set_specific_secret('123456')
        request = CreateAccountTemplateRequest(
            id_='bf6682af-7056-413d-be80-302604129666',
            name='sdk-account-template', comment='sdk-account-template-comment',
            username='jms', privileged=False, secret=secret, auto_push=False,
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AccountTemplateInstance)

    def test_update_account_template(self):
        """ 测试更新指定 ID 账号模板属性 """
        secret = SecretParam()
        secret.random_gen_secret(length=10, exclude_symbols='@#$', digit=False)
        push_params = PushParams()
        push_params.set_aix_params(groups=['dev', 'jms'], shell='/bin/sh')
        request = UpdateAccountTemplateRequest(
            id_='bf6682af-7056-413d-be80-302604129666',
            name='sdk-account-template-new', comment='sdk-account-template-comment-new',
            su_from='8c47e070-3c80-4eeb-8661-b9270609be52', push_params=push_params,
            username='jms-test', privileged=True, secret=secret, auto_push=True,
            platforms=['17', '32', '102']
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AccountTemplateInstance)

    def test_delete_account_template(self):
        """ 测试删除指定 ID 账号模板 """
        request = DeleteAccountTemplateRequest(id_='079ec32d-1b9e-459a-85d9-cf0ccec01dab')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_sync_account_template_info_to_accounts(self):
        """ 同步账号模板信息到关联账号 """
        request = SyncAccountTemplateInfoRequest(id_='00f03df3-1dc7-402f-80cc-083eab931e39')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
