import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.common import SimpleProtocolParam
from jms_client.v1.models.request.permissions.connect_method_acls import (
    CreateConnectMethodACLRequest, DescribeConnectMethodACLsRequest,
    DetailConnectMethodACLRequest, UpdateConnectMethodACLRequest,
    DeleteConnectMethodACLRequest, UserManyFilterParam
)
from jms_client.v1.models.instance.permissions import (
    ConnectMethodACLInstance,
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
        self.client.set_org(self.client.root_org)

    def test_list_connect_method_acls(self):
        """ 测试获取连接方式控制列表 """
        request = DescribeConnectMethodACLsRequest(limit=2)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_connect_method_acl(self):
        """ 测试获取指定 ID 连接方式控制详情 """
        request = DetailConnectMethodACLRequest(id_='ba177a3a-b0cc-48e2-8eab-b0283ef89c91')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), ConnectMethodACLInstance)

    def test_create_connect_method_acl(self):
        """ 测试创建连接方式控制 """
        users = UserManyFilterParam()
        users.set_filter_attrs([
            {'name': 'name', 'match': 'contains', 'value': 'jms'},
            {'name': 'groups', 'match': 'm2m', 'value': [
                '253ed525-291a-45f5-8e09-88e92577e913'
            ]}
        ])
        methods = SimpleProtocolParam().append_vnc().append_rdp()
        request = CreateConnectMethodACLRequest(
            id_='e6bf4ebd-0962-4af3-a5fb-dec1bca2c5ff',
            name='sdk-connect-method-acl', users=users, priority=12,
            connect_methods=methods
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), ConnectMethodACLInstance)

    def test_update_connect_method_acl(self):
        """ 测试更新指定 ID 连接方式控制属性 """
        users = UserManyFilterParam()
        users.set_filter_attrs([
            {'name': 'name', 'match': 'contains', 'value': 'jms'},
            {'name': 'groups', 'match': 'm2m_all', 'value': [
                '253ed525-291a-45f5-8e09-88e92577e913'
            ]},
            {'name': 'is_first_login', 'match': 'exact', 'value': True}
        ])
        methods = SimpleProtocolParam()
        methods.append_vnc().append_rdp().append_k8s()
        request = UpdateConnectMethodACLRequest(
            id_='e6bf4ebd-0962-4af3-a5fb-dec1bca2c5ff',
            name='sdk-connect-acl-new', users=users, priority=22,
            connect_methods=methods
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), ConnectMethodACLInstance)

    def test_delete_connect_method_acl(self):
        """ 测试删除指定 ID 连接方式控制 """
        request = DeleteConnectMethodACLRequest(
            id_='e6bf4ebd-0962-4af3-a5fb-dec1bca2c5ff'
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
