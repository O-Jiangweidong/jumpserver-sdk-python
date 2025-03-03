import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.accounts import (
    DescribeAccountsRequest, DetailAccountRequest,
    DeleteAccountRequest, CreateAccountRequest,
    UpdateAccountRequest, ClearAccountSecretRequest
)
from jms_client.v1.models.instance.accounts import AccountInstance
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
        self.client.set_org('004b4416-d51d-48d8-a877-fe8e843ce34b')

    def test_list_accounts(self):
        """ 测试获取账号列表 """
        request = DescribeAccountsRequest(limit=10, username='root')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_create_account(self):
        """ 测试创建账号 """
        request = CreateAccountRequest(
            asset='3381308f-7983-45be-a89a-bcaf94bd4b9d', username='test',
            secret_type='password', secret='123456', name='test',
            comment='jumpserver', privileged=True, push_now=True,
            su_from='db11d871-d7d8-4b32-a3b7-cfb87f49c336',
            is_active=True
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AccountInstance)

    def test_retrieve_account(self):
        """ 测试获取指定 ID 账号详情 """
        request = DetailAccountRequest(id_='3381308f-7983-45be-a89a-bcaf94bd4b9d')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AccountInstance)

    def test_update_account(self):
        """ 测试更新指定 ID 账号 """
        request = UpdateAccountRequest(
            id_='3381308f-7983-45be-a89a-bcaf94bd4b9d', username='test',
            asset='3381308f-7983-45be-a89a-bcaf94bd4b9d', comment='test',
            secret_type='password', secret='123456', name='test',
            privileged=True, push_now=True, is_active=True,
            su_from='db11d871-d7d8-4b32-a3b7-cfb87f49c336'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AccountInstance)

    def test_clear_accounts_secret(self):
        """ 测试清除指定 ID 账号密码 """
        request = ClearAccountSecretRequest(
            accounts=[
                '6cee6d36-63a8-4509-b9c2-e0aebc65a290',
                '1ed0287b-d45e-4ce5-bfa2-ed4a3d52f867'
            ]
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())

    def test_delete_account(self):
        """ 测试删除指定 ID 账号 """
        request = DeleteAccountRequest(id_='3381308f-7983-45be-a89a-bcaf94bd4b9d')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())
