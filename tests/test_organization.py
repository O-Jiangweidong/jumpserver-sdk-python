import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.organizations import (
    CreateOrganizationRequest,
    DescribeOrganizationsRequest,
    DetailOrganizationRequest,
    UpdateOrganizationRequest,
    DeleteOrganizationRequest
)
from jms_client.v1.models.instance.organizations import (
    OrganizationInstance,
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

    def test_list_organizations(self):
        """ 测试获取组织列表 """
        request = DescribeOrganizationsRequest(limit=1)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_organization(self):
        """ 测试获取指定 ID 组织详情 """
        request = DetailOrganizationRequest(id_='e6bf4ebd-0962-4af3-a5fb-dec1bca2c5bb')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), OrganizationInstance)

    def test_create_organization(self):
        """ 测试创建组织 """
        request = CreateOrganizationRequest(name='sdk-org')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), OrganizationInstance)

    def test_update_organization(self):
        """ 测试更新指定 ID 组织属性 """
        request = UpdateOrganizationRequest(
            id_='e6bf4ebd-0962-4af3-a5fb-dec1bca2c5bb', name='woo',
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), OrganizationInstance)

    def test_delete_organization(self):
        """ 测试删除指定 ID 组织 """
        request = DeleteOrganizationRequest(id_='ede0b1c1-9e2f-4355-acbf-7af9550a616b')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
