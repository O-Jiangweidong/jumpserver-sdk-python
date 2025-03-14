import configparser

import unittest

from jms_client.const import SYSTEM_ADMIN
from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.users.roles import (
    DescribeRolesRequest, DetailRoleRequest,
    CreateRoleRequest, UpdateRoleRequest, DeleteRoleRequest,
    DescribeUsersWithRoleRequest, AppendUsersToRoleRequest,
    RemoveUserFromRoleRequest
)
from jms_client.v1.models.instance.users import RoleInstance, RoleUserInstance
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

    def test_list_roles(self):
        """ 测试获取用户角色列表 """
        request = DescribeRolesRequest(limit=10, scope='org')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_role(self):
        """ 测试获取指定 ID 角色详情 """
        request = DetailRoleRequest(id_='c7d74aa7-223a-47c1-b9a6-40b2edbe7a1b')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), RoleInstance)

    def test_create_role(self):
        """ 测试创建角色 """
        request = CreateRoleRequest(
            id_='f288c986-79b9-48c8-aa00-7dd8841f1aaa',
            name='sdk-role', scope='org', comment='sdk-role-comment',
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), RoleInstance)

    def test_update_role(self):
        """ 测试更新指定 ID 角色属性 """
        request = UpdateRoleRequest(
            id_='f288c986-79b9-48c8-aa00-7dd8841f1aaa',
            name='sdk-role-new', scope='org', comment='sdk-role-comment',
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), RoleInstance)

    def test_delete_role(self):
        """ 测试删除指定 ID 角色 """
        request = DeleteRoleRequest(id_='f288c986-79b9-48c8-aa00-7dd8841f1aaa')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_list_role_relation_users(self):
        """ 测试获取指定角色关联的用户列表 """
        self.client.set_org(self.client.root_org)
        request = DescribeUsersWithRoleRequest(
            role_id=SYSTEM_ADMIN, scope='org', limit=3
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_request_ok())
        self.assertIsInstance(resp.get_data(), list)

    def test_append_user_to_role(self):
        """ 测试向指定角色批量添加用户 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = AppendUsersToRoleRequest(
            role_id='06554ef8-674f-4d9d-aaaf-3b370832a8e2',
            scope='org',
            users=[
                'f288c986-79b9-48c8-aa00-7dd8841f1017',
                'afe6fabe-ba16-42e8-80bc-2f5faab84f72',
            ]
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_remove_user_from_role(self):
        """ 测试从指定角色移除用户 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        # 先查询出用户和角色的关联 ID
        role_id = '06554ef8-674f-4d9d-aaaf-3b370832a8e2'
        scope = 'org'
        request = DescribeUsersWithRoleRequest(
            role_id=role_id, scope=scope, limit=1
        )
        resp: Response = self.client.do(request, with_model=True)
        if resp.total < 1:
            return

        relation_obj: RoleUserInstance = resp.get_data()[0]
        request = RemoveUserFromRoleRequest(
            relation_id=relation_obj.id, scope=scope, role_id=role_id
        )
        resp: Response = self.client.do(request)
        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
