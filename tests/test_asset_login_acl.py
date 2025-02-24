import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.permissions.asset_login_acls import (
    CreateAssetLoginACLRequest, DescribeAssetLoginACLsRequest,
    DetailAssetLoginACLRequest, UpdateAssetLoginACLRequest,
    DeleteAssetLoginACLRequest,
)
from jms_client.v1.models.request.common import (
    UserManyFilterParam, RuleParam, AccountParam, AssetManyFilterParam
)
from jms_client.v1.models.instance.permissions import (
    AssetLoginACLInstance,
)
from jms_client.v1.models.request.const import ACLAction
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

    def test_list_login_user_acls(self):
        """ 测试获取资产登陆控制列表 """
        request = DescribeAssetLoginACLsRequest(limit=2)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_login_user_acl(self):
        """ 测试获取指定 ID 资产登陆控制详情 """
        request = DetailAssetLoginACLRequest(id_='63a34176-cd19-4475-8f25-a9b8bcfd35e0')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AssetLoginACLInstance)

    def test_create_login_user_acl(self):
        """ 测试创建资产登陆控制 """
        users = UserManyFilterParam()
        users.set_filter_attrs([
            {'name': 'name', 'match': 'contains', 'value': 'jms'},
            {'name': 'groups', 'match': 'm2m', 'value': [
                '253ed525-291a-45f5-8e09-88e92577e913'
            ]}
        ])
        assets = AssetManyFilterParam()
        assets.set_specify([
            'def349e4-8667-4ea3-b006-b23719caa0f6',
        ])
        accounts = AccountParam()
        accounts.with_spec(['jms', 'test', 'dev'])
        request = CreateAssetLoginACLRequest(
            id_='e6bf4ebd-0962-4af3-a5fb-dec1bca2c5ff',
            name='sdk-asset-login-acl', users=users, priority=12,
            action=ACLAction.NOTICE, reviewers=[
                '1de7ce70-3172-48b2-80ad-4ece0eafa846',
                'f288c986-79b9-48c8-aa00-7dd8841f1017'
            ], assets=assets, accounts=accounts,
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AssetLoginACLInstance)

    def test_update_login_user_acl(self):
        """ 测试更新指定 ID 资产登陆控制属性 """
        users = UserManyFilterParam()
        users.set_filter_attrs([
            {'name': 'name', 'match': 'contains', 'value': 'jms'},
            {'name': 'email', 'match': 'not', 'value': 'admin@fit2cloud.com'}
        ])
        assets = AssetManyFilterParam()
        assets.set_specify([
            'def349e4-8667-4ea3-b006-b23719caa0f6',
        ])
        accounts = AccountParam()
        accounts.with_spec(['jms', 'test'])
        rules = RuleParam()
        rules.set_ip_group(['192.168.1.0/24', '10.1.1.1-10.1.1.20'])
        rules.set_time_period([1, 3, 4, 5, 0], time_periods=[
            '00:00~02:00', '03:30~05:30', '10:00~11:30', '20:00~00:00'
        ])
        request = UpdateAssetLoginACLRequest(
            id_='e6bf4ebd-0962-4af3-a5fb-dec1bca2c5ff',
            name='sdk-asset-login-acl-new', users=users, priority=72,
            action=ACLAction.REVIEW, reviewers=[
                'f288c986-79b9-48c8-aa00-7dd8841f1017'
            ], assets=assets, accounts=accounts, rules=rules,
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AssetLoginACLInstance)

    def test_delete_login_user_acl(self):
        """ 测试删除指定 ID 资产登陆控制 """
        request = DeleteAssetLoginACLRequest(
            id_='e6bf4ebd-0962-4af3-a5fb-dec1bca2c5ff'
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
