import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.permissions import (
    DescribeCommandGroupsRequest, DetailCommandGroupRequest,
    CreateCommandGroupRequest, UpdateCommandGroupRequest, 
    DeleteCommandGroupRequest
)
from jms_client.v1.models.request.const import CommandGroupType
from jms_client.v1.models.instance.permissions import (
    CommandGroupInstance,
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

    def test_list_domains(self):
        """ 测试获取命令过滤-命令组列表 """
        request = DescribeCommandGroupsRequest(limit=2)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_domain(self):
        """ 测试获取指定 ID 命令过滤-命令组详情 """
        request = DetailCommandGroupRequest(id_='7a003d30-7e9d-4ab2-b566-f766a1576056')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), CommandGroupInstance)

    def test_create_domain(self):
        """ 测试创建命令过滤-命令组 """
        request = CreateCommandGroupRequest(
            id_='bf6682af-7056-413d-be80-3026041295dd',
            name='sdk-command-group', content='rm',
            comment='sdk-command-group-comment',
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), CommandGroupInstance)

    def test_update_domain(self):
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

    def test_delete_domain(self):
        """ 测试删除指定 ID 命令过滤-命令组 """
        request = DeleteCommandGroupRequest(id_='bf6682af-7056-413d-be80-3026041295dd')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
