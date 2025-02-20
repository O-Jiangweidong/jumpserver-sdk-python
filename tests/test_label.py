import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.labels import (
    CreateLabelRequest, DescribeLabelsRequest,
    DetailLabelRequest, UpdateLabelRequest, DeleteLabelRequest
)
from jms_client.v1.models.instance.labels import LabelInstance
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

    def test_list_labels(self):
        """ 测试获取标签列表 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DescribeLabelsRequest(limit=2)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_label(self):
        """ 测试获取指定 ID 标签详情 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DetailLabelRequest(id_='dab06175-204e-403a-93ad-3f027547138f')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), LabelInstance)

    def test_create_label(self):
        """ 测试创建标签 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = CreateLabelRequest(
            id_='dab06175-204e-403a-93ad-3f02754713aa',
            name='sdk-label', value='sdk-label-value'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), LabelInstance)

    def test_update_label(self):
        """ 测试更新指定 ID 标签属性 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = UpdateLabelRequest(
            id_='dab06175-204e-403a-93ad-3f02754713aa',
            name='sdk-woo', value='woo-value', comment='comment'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), LabelInstance)

    def test_delete_label(self):
        """ 测试删除指定 ID 标签 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DeleteLabelRequest(id_='dab06175-204e-403a-93ad-3f02754713aa')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
