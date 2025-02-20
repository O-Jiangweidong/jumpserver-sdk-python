import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.permissions.user_login_acl import (
    CreateUserLoginACLRequest, DescribeUserLoginACLsRequest,
    DetailUserLoginACLRequest, UpdateUserLoginACLRequest,
    DeleteUserLoginACLRequest, UserParam, RuleParam
)
from jms_client.v1.models.instance.permissions import (
    UserLoginACLInstance,
)
from jms_client.v1.models.request.const import UserLoginACLAction
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

    def test_list_login_user_acls(self):
        """ 测试获取用户登陆控制列表 """
        request = DescribeUserLoginACLsRequest(limit=2)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_login_user_acl(self):
        """ 测试获取指定 ID 用户登陆控制详情 """
        request = DetailUserLoginACLRequest(id_='44c68eb2-7dae-4d5a-944f-f9542b346205')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), UserLoginACLInstance)

    def test_create_login_user_acl(self):
        """ 测试创建用户登陆控制 """
        self.client.set_org(self.client.root_org)
        users = UserParam()
        users.set_attr_users([
            {'name': 'name', 'match': 'contains', 'value': 'jms'},
            {'name': 'groups', 'match': 'm2m', 'value': [
                '253ed525-291a-45f5-8e09-88e92577e913'
            ]}
        ])
        request = CreateUserLoginACLRequest(
            id_='e6bf4ebd-0962-4af3-a5fb-dec1bca2c5cc',
            name='sdk-user-login-acl', users=users, priority=12,
            action=UserLoginACLAction.NOTICE, reviewers=[
                '1de7ce70-3172-48b2-80ad-4ece0eafa846',
                'f288c986-79b9-48c8-aa00-7dd8841f1017'
            ]
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), UserLoginACLInstance)

    def test_update_login_user_acl(self):
        """ 测试更新指定 ID 用户登陆控制属性 """
        self.client.set_org(self.client.root_org)
        users = UserParam()
        users.set_attr_users([
            {'name': 'name', 'match': 'contains', 'value': 'jms'},
            {'name': 'groups', 'match': 'm2m_all', 'value': [
                '253ed525-291a-45f5-8e09-88e92577e913'
            ]},
            {'name': 'is_first_login', 'match': 'exact', 'value': True}
        ])
        rules = RuleParam()
        rules.set_ip_group(['192.168.1.0/24', '10.1.1.1-10.1.1.20'])
        rules.set_time_period([1, 3, 4, 5, 0], time_periods=[
            '00:00~02:00', '03:30~05:30', '10:00~11:30', '20:00~00:00'
        ])
        request = UpdateUserLoginACLRequest(
            id_='e6bf4ebd-0962-4af3-a5fb-dec1bca2c5cc', rules=rules,
            name='sdk-user-login-acl-new', users=users, priority=12,
            action=UserLoginACLAction.REVIEW, reviewers=[
                '1de7ce70-3172-48b2-80ad-4ece0eafa846',
                'f288c986-79b9-48c8-aa00-7dd8841f1017'
            ]
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), UserLoginACLInstance)

    def test_delete_login_user_acl(self):
        """ 测试删除指定 ID 用户登陆控制 """
        request = DeleteUserLoginACLRequest(
            id_='e6bf4ebd-0962-4af3-a5fb-dec1bca2c5cc'
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
