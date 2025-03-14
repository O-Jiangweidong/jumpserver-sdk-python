import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.permissions import (
    CreatePermissionRequest, DescribePermissionsRequest,
    DetailPermissionRequest, UpdatePermissionRequest,
    DeletePermissionRequest, DescribePermsForAssetAndUserRequest,
    DescribePermsForAssetAndUserGroupRequest,
    AppendUsersToPermissionRequest, RemoveUserFromPermissionRequest,
    AppendUserGroupsToPermissionRequest, RemoveUserGroupFromPermissionRequest,
    AppendAssetsToPermissionRequest, RemoveAssetFromPermissionRequest,
    AppendNodesToPermissionRequest, RemoveNodeFromPermissionRequest,
    AccountParam, ActionParam, ProtocolParam
)
from jms_client.v1.models.instance.permissions import (
    PermissionInstance,
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

    def test_list_permissions(self):
        """ 测试获取授权列表 """
        request = DescribePermissionsRequest(limit=1)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_permission(self):
        """ 测试获取指定 ID 授权详情 """
        request = DetailPermissionRequest(id_='d43c9898-1b73-46ab-91dd-ed0db1305817')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), PermissionInstance)

    def test_create_permission(self):
        """ 测试创建授权 """
        # 设置授权账号
        accounts = AccountParam()
        accounts.with_input().with_spec(['root', 'jms'])
        # 设置授权动作
        actions = ActionParam()
        actions.set_clipboard()
        # 设置授权协议
        protocols = ProtocolParam()
        protocols.append_all()
        request = CreatePermissionRequest(
            id_='e6bf4ebd-0962-4af3-a5fb-dec1bca2c5aa', name='sdk-perm',
            date_start='2025-01-01 12:00:00', date_expired='2025-02-01 11:00:00',
            is_active=False, users=['02537731-93c1-4096-ba1e-182ab3bb693e'],
            assets=['26b4630c-b91f-4bf1-9012-69a30b2da5c4'],
            nodes=['6d93bf17-94bf-4c24-9f0d-3d251a1a3e1a'],
            user_groups=['253ed525-291a-45f5-8e09-88e92577e913'],
            accounts=accounts, actions=actions, protocols=protocols,
            comment='SDK permission test'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), PermissionInstance)

    def test_update_permission(self):
        """ 测试更新指定 ID 授权属性 """
        # 设置授权账号
        accounts = AccountParam()
        accounts.with_input().with_anon().with_user()
        # 设置授权动作
        actions = ActionParam()
        actions.set_clipboard()
        # 设置授权协议
        protocols = ProtocolParam()
        protocols.append_all()
        request = UpdatePermissionRequest(
            id_='e6bf4ebd-0962-4af3-a5fb-dec1bca2c5aa', name='sdk-perm-new',
            date_start='2025-01-03 12:00:00',
            is_active=True, users=['02537731-93c1-4096-ba1e-182ab3bb693e'],
            assets=['26b4630c-b91f-4bf1-9012-69a30b2da5c4'],
            nodes=['6d93bf17-94bf-4c24-9f0d-3d251a1a3e1a'], user_groups=[],
            accounts=accounts, actions=actions, protocols=protocols,
            comment='SDK permission test - New'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), PermissionInstance)

    def test_delete_permission(self):
        """ 测试删除指定 ID 授权 """
        request = DeletePermissionRequest(id_='e6bf4ebd-0962-4af3-a5fb-dec1bca2c5aa')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_list_authorized_perms_for_asset_and_user_request(self):
        """ 测试查询`用户和资产`对应的授权 """
        request = DescribePermsForAssetAndUserRequest(
            asset_id='e0bdf9e2-3184-43b1-b80e-ce3edbd50253',
            user_id='90c61428-5ff3-4ee7-b220-451de8a275c5',
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_list_authorized_perms_for_asset_and_user_group_request(self):
        """ 测试查询`用户组和资产`对应的授权 """
        request = DescribePermsForAssetAndUserGroupRequest(
            asset_id='e0bdf9e2-3184-43b1-b80e-ce3edbd50253',
            user_group_id='70df0624-246f-43b0-b18a-9b3f58da9030',
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_add_users_to_permission(self):
        """ 测试向指定授权批量添加用户 """
        request = AppendUsersToPermissionRequest(
            permission_id='d43c9898-1b73-46ab-91dd-ed0db1305817',
            users=[
                'b8f95980-f4c9-424a-8f79-025f2a0171a7',
                '17dfb3ba-45da-4861-882d-2ba7e22be3c6'
            ]
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_remove_user_from_permission(self):
        """ 测试从指定授权移除用户 """
        request = RemoveUserFromPermissionRequest(
            user_id='17dfb3ba-45da-4861-882d-2ba7e22be3c6',
            permission_id='d43c9898-1b73-46ab-91dd-ed0db1305817'
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_add_user_groups_to_permission(self):
        """ 测试向指定授权批量添加用户组 """
        request = AppendUserGroupsToPermissionRequest(
            permission_id='d43c9898-1b73-46ab-91dd-ed0db1305817',
            user_groups=[
                '70df0624-246f-43b0-b18a-9b3f58da9030',
                '253ed525-291a-45f5-8e09-88e92577e913'
            ]
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_remove_user_group_from_permission(self):
        """ 测试从指定授权移除用户组 """
        request = RemoveUserGroupFromPermissionRequest(
            user_group_id='253ed525-291a-45f5-8e09-88e92577e913',
            permission_id='d43c9898-1b73-46ab-91dd-ed0db1305817'
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_add_assets_to_permission(self):
        """ 测试向指定授权批量添加资产 """
        request = AppendAssetsToPermissionRequest(
            permission_id='d43c9898-1b73-46ab-91dd-ed0db1305817',
            assets=[
                'e1db4ccc-89a6-4af6-8244-2ded48b4f5ff',
                '663aea5c-7e6a-4aea-8bf2-9e1633b54126'
            ]
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_remove_asset_from_permission(self):
        """ 测试从指定授权移除资产 """
        request = RemoveAssetFromPermissionRequest(
            asset_id='663aea5c-7e6a-4aea-8bf2-9e1633b54126',
            permission_id='d43c9898-1b73-46ab-91dd-ed0db1305817'
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_add_nodes_to_permission(self):
        """ 测试向指定授权批量添加节点 """
        request = AppendNodesToPermissionRequest(
            permission_id='d43c9898-1b73-46ab-91dd-ed0db1305817',
            nodes=[
                '1c9fbd6a-d797-4554-b4d5-3a1b70cb48ae',
                'e35127a3-c6fb-4a20-820a-77e88ca94f71'
            ]
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_remove_node_from_permission(self):
        """ 测试从指定授权移除节点 """
        request = RemoveNodeFromPermissionRequest(
            node_id='e35127a3-c6fb-4a20-820a-77e88ca94f71',
            permission_id='d43c9898-1b73-46ab-91dd-ed0db1305817'
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
