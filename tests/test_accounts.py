import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.accounts import (
    DescribeAccountsRequest, DetailAccountRequest,
    DeleteAccountRequest, CreateAccountRequest,
    UpdateAccountRequest
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

    def test_retrieve_account(self):
        """ 测试获取指定 ID 账号详情 """
        request = DetailAccountRequest(id_='db11d871-d7d8-4b32-a3b7-cfb87f49c336')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AccountInstance)

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

    def test_update_account(self):
        """ 测试更新指定 ID 账号 """
        request = UpdateAccountRequest(
            id_='2fc7034d-5902-4e94-87cb-95455d410cc0', username='test',
            asset='3381308f-7983-45be-a89a-bcaf94bd4b9d', comment='test',
            secret_type='password', secret='123456', name='test',
            privileged=True, push_now=True, is_active=True,
            su_from='db11d871-d7d8-4b32-a3b7-cfb87f49c336'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AccountInstance)

    def test_delete_account(self):
        """ 测试删除指定 ID 账号 """
        request = DeleteAccountRequest(id_='04cf23e8-b4b2-4687-b4c9-1b5001be5c98')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())
