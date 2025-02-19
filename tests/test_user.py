import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.const import Source, MFALevel
from jms_client.v1.models.request.users import (
    DescribeUsersRequest, DetailUserRequest, AuthStrategyParam,
    CreateUserRequest, UpdateUserRequest, DeleteUserRequest,
)
from jms_client.v1.models.instance.users import (
    UserInstance,
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

    def test_list_users(self):
        """ 测试获取用户列表 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DescribeUsersRequest(limit=2)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_user(self):
        """ 测试获取指定 ID 用户详情 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DetailUserRequest(id_='90c61428-5ff3-4ee7-b220-451de8a275c5')
        resp: Response = self.client.do(request, with_model=True)

        print(resp.get_data())
        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), UserInstance)

    def test_create_user(self):
        """ 测试创建用户 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        auth_strategy = AuthStrategyParam()
        auth_strategy.set_password('hello', need_update=False)
        request = CreateUserRequest(
            id_='90c61428-5ff3-4ee7-b220-451de8a275c1', username='sdk-user',
            name='sdk-user', email='sdk@test.com', comment='sdk-user-comment',
            groups=['253ed525-291a-45f5-8e09-88e92577e913'],
            auth_strategy=auth_strategy, source=Source.OPENID,
            mfa_level=MFALevel.ENABLED, is_active=True, phone='+8616677778888'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), UserInstance)

    def test_update_user(self):
        """ 测试更新指定 ID 用户属性 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = UpdateUserRequest(
            id_='90c61428-5ff3-4ee7-b220-451de8a275c1', username='sdk-user',
            name='sdk-user-new', email='sdk@test-new.com', comment='sdk-user-new-comment',
            groups=['253ed525-291a-45f5-8e09-88e92577e913'],
            source=Source.LOCAL, mfa_level=MFALevel.ENABLED,
            is_active=True, phone='+8616677778888'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), UserInstance)

    def test_delete_user(self):
        """ 测试删除指定 ID 用户 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DeleteUserRequest(id_='90c61428-5ff3-4ee7-b220-451de8a275c1')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
