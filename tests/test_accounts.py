import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.accounts import DescribeAccountsRequest, DetailAccountRequest
from jms_client.v1.models.instance.accounts import AccountInstance
from jms_client.v1.models.response import Response


class TestFunctionality(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        config = configparser.ConfigParser()
        config.read('config.ini')
        username = config['test']['username']
        password = config['test']['password']
        self.client: Client = get_client(
            version='3.10', web_url='https://js-internal.fit2cloud.cn',
            username=username, password=password
        )

    def test_list_accounts(self):
        """ 测试获取账号列表 """
        # 切换组织
        self.client.set_org(self.client.default_org)

        request = DescribeAccountsRequest(limit=10, username='root')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_account(self):
        """ 测试获取指定 ID 账号详情 """
        request = DetailAccountRequest(id_='a0428ae7-da57-4ec3-8922-a399ca86ed4b')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AccountInstance)
