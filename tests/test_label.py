import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.const import ResourceType
from jms_client.v1.models.request.labels import (
    CreateLabelRequest, DescribeLabelsRequest, DetailLabelRequest,
    UpdateLabelRequest, DeleteLabelRequest, DescribeLabelResourceRequest,
    BindLabelForResourceRequest, DescribeLabelResourceTypesRequest,
    UnBindLabelForResourceRequest,
)
from jms_client.v1.models.instance.labels import LabelInstance, ResourceTypeInstance
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

    def test_list_labels(self):
        """ 测试获取标签列表 """
        request = DescribeLabelsRequest(limit=2)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_label(self):
        """ 测试获取指定 ID 标签详情 """
        request = DetailLabelRequest(id_='dab06175-204e-403a-93ad-3f027547138f')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), LabelInstance)

    def test_create_label(self):
        """ 测试创建标签 """
        request = CreateLabelRequest(
            id_='dab06175-204e-403a-93ad-3f02754713aa',
            name='sdk-label', value='sdk-label-value'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), LabelInstance)

    def test_update_label(self):
        """ 测试更新指定 ID 标签属性 """
        request = UpdateLabelRequest(
            id_='dab06175-204e-403a-93ad-3f02754713aa',
            name='sdk-woo', value='woo-value', comment='comment'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), LabelInstance)

    def test_delete_label(self):
        """ 测试删除指定 ID 标签 """
        request = DeleteLabelRequest(id_='dab06175-204e-403a-93ad-3f02754713aa')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    def test_bind_label_for_resource(self):
        """ 测试绑定标签到资源 """
        request = DescribeLabelResourceTypesRequest()
        resp: Response = self.client.do(request, with_model=True)
        types: list[ResourceTypeInstance] = resp.get_data()
        resource_type_id = ''
        for type_ in types:
            if type_.model == ResourceType.ACCOUNT_TEMPLATE:
                resource_type_id = type_.id
                break

        self.assertNotEqual(resource_type_id, '')

        request = BindLabelForResourceRequest(
            label_id='f605f0d9-52e3-40c1-89d2-25f88d45473e',
            resource_type_id=resource_type_id,
            resource_ids=[
                '00f03df3-1dc7-402f-80cc-083eab931e39',
                '4ca51972-3ab1-45da-a834-79f19274340f'
            ],
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())

    def test_list_resource_for_label(self):
        """ 测试获取标签绑定的资源列表 """
        request = DescribeLabelResourceRequest(
            label_id='f605f0d9-52e3-40c1-89d2-25f88d45473e'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_unbind_label_for_resource(self):
        """ 测试给指定资源解除绑定某标签 """
        request = UnBindLabelForResourceRequest(
            id_='edd04dc0-1500-44e3-b2c0-85d45ef5d228',  # DescribeLabelResourceRequest 查询的 ID
            label_id='f605f0d9-52e3-40c1-89d2-25f88d45473e'
        )
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
