import configparser

import unittest

from jms_client.client import get_client
from jms_client.const import ORG_USER, ORG_AUDITOR
from jms_client.v1.client import Client
from jms_client.v1.models.request.const import Source, MFALevel
from jms_client.v1.models.request.users import (
    DescribeUsersRequest, DetailUserRequest, AuthStrategyParam,
    CreateUserRequest, UpdateUserRequest, DeleteUserRequest,
    RemoveUserRequest, InviteUserRequest, DescribeAuthorizedUsersForAssetRequest,
    DescribeUsersForPermissionRequest,
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
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')

    def test_list_users(self):
        """ 测试获取用户列表 """
        request = DescribeUsersRequest(limit=2)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_user(self):
        """ 测试获取指定 ID 用户详情 """
        request = DetailUserRequest(id_='90c61428-5ff3-4ee7-b220-451de8a275c5')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), UserInstance)

    def test_create_user(self):
        """ 测试创建用户 """
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
        request = DeleteUserRequest(id_='90c61428-5ff3-4ee7-b220-451de8a275c1')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_invite_users(self):
        """ 测试邀请用户到当前组织 """
        request = InviteUserRequest(
            users=[
                'b58d578a-77c4-4a46-9b58-d1d8ac23b094',
                'e3eae720-e41e-4a2c-ae26-222d4024666e'
            ],
            org_roles=[ORG_USER, ORG_AUDITOR]
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_remove_user(self):
        """ 测试移除指定 ID 用户【非删除，只是把用户从某个组织移除】 """
        request = RemoveUserRequest(id_='f89bfaf0-c823-4fb7-9bed-0e4a5c5b2c50')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_list_authorized_users_for_asset_request(self):
        """ 测试获取`资产`被授权的用户 """
        request = DescribeAuthorizedUsersForAssetRequest(
            asset_id='e0bdf9e2-3184-43b1-b80e-ce3edbd50253'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_list_users_for_permission(self):
        """ 测试获取`授权`的用户  """
        request = DescribeUsersForPermissionRequest(
            id_='d43c9898-1b73-46ab-91dd-ed0db1305817',
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)


if __name__ == '__main__':
    unittest.main()
