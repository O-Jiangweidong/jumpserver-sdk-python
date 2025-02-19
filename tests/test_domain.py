import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.assets import (
    DescribeDomainsRequest, DetailDomainRequest,
    CreateDomainRequest, UpdateDomainRequest, DeleteDomainRequest
)
from jms_client.v1.models.instance.assets import (
    DomainInstance,
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

    def test_list_domains(self):
        """ 测试获取网域列表 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DescribeDomainsRequest(limit=2)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_domain(self):
        """ 测试获取指定 ID 网域详情 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DetailDomainRequest(id_='bf6682af-7056-413d-be80-302604129598')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), DomainInstance)

    def test_create_domain(self):
        """ 测试创建网域 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = CreateDomainRequest(
            id_='bf6682af-7056-413d-be80-302604129597',
            name='sdk-domain', comment='sdk-domain-comment',
            assets=[
                'def349e4-8667-4ea3-b006-b23719caa0f6',
                'e1db4ccc-89a6-4af6-8244-2ded48b4f5ff'
            ],
            gateways=[
                '368bb289-26b4-43f8-9c43-d7edb605e984',
                '206606e7-9612-4313-aa3c-e9ddd79df950'
            ],
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), DomainInstance)

    def test_update_domain(self):
        """ 测试更新指定 ID 网域属性 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = UpdateDomainRequest(
            id_='bf6682af-7056-413d-be80-302604129597', name='sdk-domain-new',
            assets=[], gateways=[
                '368bb289-26b4-43f8-9c43-d7edb605e984',
            ],
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), DomainInstance)

    def test_delete_domain(self):
        """ 测试删除指定 ID 网域 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DeleteDomainRequest(id_='bf6682af-7056-413d-be80-302604129597')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
