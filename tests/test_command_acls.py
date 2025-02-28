import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.params import (
    UserManyFilterParam, AssetManyFilterParam, AccountParam, SimpleProtocolParam
)
from jms_client.v1.models.request.permissions import (
    DescribeCommandFiltersRequest, DetailCommandFilterRequest,
    CreateCommandFilterRequest, UpdateCommandFilterRequest,
    DeleteCommandFilterRequest,
    DescribeCommandGroupsRequest, DetailCommandGroupRequest,
    CreateCommandGroupRequest, UpdateCommandGroupRequest, 
    DeleteCommandGroupRequest
)
from jms_client.v1.models.request.const import CommandGroupType, ACLAction
from jms_client.v1.models.instance.permissions import (
    CommandFilterInstance, CommandGroupInstance,
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

    # --------------------- 命令组相关操作 ---------------------
    def test_list_command_groups(self):
        """ 测试获取命令过滤-命令组列表 """
        request = DescribeCommandGroupsRequest(limit=2)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_command_group(self):
        """ 测试获取指定 ID 命令过滤-命令组详情 """
        request = DetailCommandGroupRequest(id_='7a003d30-7e9d-4ab2-b566-f766a1576056')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), CommandGroupInstance)

    def test_create_command_group(self):
        """ 测试创建命令过滤-命令组 """
        request = CreateCommandGroupRequest(
            id_='bf6682af-7056-413d-be80-3026041295dd',
            name='sdk-command-group', content='rm',
            comment='sdk-command-group-comment',
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), CommandGroupInstance)

    def test_update_command_group(self):
        """ 测试更新指定 ID 命令过滤-命令组属性 """
        request = UpdateCommandGroupRequest(
            id_='bf6682af-7056-413d-be80-3026041295dd',
            name='sdk-command-group-new', content='rm -rf',
            comment='sdk-command-group-comment-new',
            type_=CommandGroupType.REGEX, ignore_case=False,
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), CommandGroupInstance)

    def test_delete_command_group(self):
        """ 测试删除指定 ID 命令过滤-命令组 """
        request = DeleteCommandGroupRequest(id_='bf6682af-7056-413d-be80-3026041295dd')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    # --------------------- 命令过滤相关操作 ---------------------
    def test_list_command_filters(self):
        """ 测试获取命令过滤列表 """
        request = DescribeCommandFiltersRequest(limit=2)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_command_filter(self):
        """ 测试获取指定 ID 命令过滤详情 """
        request = DetailCommandFilterRequest(id_='4ed8e190-f378-4348-a7bd-fbc215512883')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), CommandFilterInstance)

    def test_create_command_filter(self):
        """ 测试创建命令过滤 """
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
            '5eb26405-65d0-4cdb-b853-6bf25bfbbce9'
        ])
        accounts = AccountParam()
        accounts.with_spec(['root', 'jms', 'dev'])
        request = CreateCommandFilterRequest(
            id_='bf6682af-7056-413d-be80-3026041295ee', priority=12,
            name='sdk-command-filter', users=users, assets=assets,
            action=ACLAction.WARNING, reviewers=[
                '1de7ce70-3172-48b2-80ad-4ece0eafa846',
                'f288c986-79b9-48c8-aa00-7dd8841f1017'
            ], accounts=accounts,
            command_groups=['7a003d30-7e9d-4ab2-b566-f766a1576056'],
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), CommandFilterInstance)

    def test_update_command_filter(self):
        """ 测试更新指定 ID 命令过滤属性 """
        users = UserManyFilterParam()
        users.set_all()
        protocols = SimpleProtocolParam().append_vnc().append_rdp()
        protocol_names = protocols.get_protocols(only_name=True)
        assets = AssetManyFilterParam()
        assets.set_filter_attrs([
            {'name': 'name', 'match': 'contains', 'value': 'jms'},
            {'name': 'protocols', 'match': 'in', 'value': protocol_names}
        ])
        accounts = AccountParam()
        accounts.with_spec(['test', 'jms'])
        request = UpdateCommandFilterRequest(
            id_='bf6682af-7056-413d-be80-3026041295ee', priority=99,
            name='sdk-command-filter-new', users=users, assets=assets,
            action=ACLAction.REVIEW, reviewers=[
                '1de7ce70-3172-48b2-80ad-4ece0eafa846',
            ], accounts=accounts,
            command_groups=['7a003d30-7e9d-4ab2-b566-f766a1576056'],
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), CommandFilterInstance)

    def test_delete_command_filter(self):
        """ 测试删除指定 ID 命令过滤 """
        request = DeleteCommandFilterRequest(id_='bf6682af-7056-413d-be80-3026041295ee')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
