import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.users import (
    DescribeUserGroupsRequest, DetailUserGroupRequest,
    CreateUserGroupRequest, UpdateUserGroupRequest,
    DeleteUserGroupRequest, AppendUserToGroupRequest,
    RemoveUserFromGroupRequest,
)
from jms_client.v1.models.instance.users import (
    UserGroupInstance,
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

    def test_list_user_groups(self):
        """ 测试获取用户组列表 """
        request = DescribeUserGroupsRequest(limit=2)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_user_group(self):
        """ 测试获取指定 ID 用户组详情 """
        request = DetailUserGroupRequest(id_='f8ed5d74-8e91-479b-a0eb-fccf16e3b1a4')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), UserGroupInstance)

    def test_create_user_group(self):
        """ 测试创建用户组 """
        request = CreateUserGroupRequest(
            id_='f288c986-79b9-48c8-aa00-7dd8841f1018',
            name='sdk-user-group', comment='sdk-user-group-comment',
            users=[
                '1de7ce70-3172-48b2-80ad-4ece0eafa846',
                'f288c986-79b9-48c8-aa00-7dd8841f1017'
            ],
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), UserGroupInstance)

    def test_update_user_group(self):
        """ 测试更新指定 ID 用户组属性 """
        request = UpdateUserGroupRequest(
            id_='f288c986-79b9-48c8-aa00-7dd8841f1018',
            name='sdk-user-group-new',
            users=[
                'f288c986-79b9-48c8-aa00-7dd8841f1017'
            ],
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), UserGroupInstance)

    def test_delete_user_group(self):
        """ 测试删除指定 ID 用户组 """
        request = DeleteUserGroupRequest(id_='f288c986-79b9-48c8-aa00-7dd8841f1018')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_add_user_to_user_group(self):
        """ 测试向指定用户组批量添加用户 """
        request = AppendUserToGroupRequest(
            group_id='f8ed5d74-8e91-479b-a0eb-fccf16e3b1a4',
            users=[
                'afe6fabe-ba16-42e8-80bc-2f5faab84f72',
                '1fd111c4-d8e4-4183-8317-6197ea52f77a'
            ]
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_remove_user_from_user_group(self):
        """ 测试从指定用户组移除用户 """
        request = RemoveUserFromGroupRequest(
            user_id='1fd111c4-d8e4-4183-8317-6197ea52f77a',
            group_id='f8ed5d74-8e91-479b-a0eb-fccf16e3b1a4'
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
