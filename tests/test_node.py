import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.assets import (
    DescribeNodesRequest, DetailNodeRequest,
    CreateNodeRequest, UpdateNodeRequest, DeleteNodeRequest
)
from jms_client.v1.models.instance.assets import (
    NodeInstance,
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

    def test_list_nodes(self):
        """ 测试获取节点列表 """
        request = DescribeNodesRequest()
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_node(self):
        """ 测试获取指定 ID 节点详情 """
        request = DetailNodeRequest(id_='09306b39-6dba-4849-95dc-9cdfadda7af0')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), NodeInstance)

    def test_create_node(self):
        """ 测试创建节点 """
        request = CreateNodeRequest(
            full_value='sdk-node/test/ok', value='hello'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), NodeInstance)

    def test_update_node(self):
        """ 测试更新指定 ID 节点属性 """
        request = UpdateNodeRequest(
            id_='0e994cbb-a242-4451-9842-85c5110cd7a3',
            value='sdk-node-new',
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), NodeInstance)

    def test_delete_node(self):
        """ 测试删除指定 ID 节点 """
        request = DeleteNodeRequest(id_='0e994cbb-a242-4451-9842-85c5110cd7a3')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
