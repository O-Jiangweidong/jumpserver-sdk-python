import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.assets import (
    DescribeHostsRequest, DescribeDatabasesRequest,
    DescribeCloudsRequest, DescribeWebsRequest,
    DescribeGPTsRequest, DescribeCustomsRequest,
    DescribeAssetsRequest, DeleteAssetRequest,
    DetailAssetRequest,
)
from jms_client.v1.models.instance import (
    GenerateInstance, AssetInstance,
)
from jms_client.v1.models.response import Response


class TestFunctionality(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client: Client = get_client(
            version='3.10', web_url='https://js-internal.fit2cloud.cn',
            username='jumpserver', password='Calong@2015'
        )

    # --------------------- 通用的 ---------------------
    def test_list_assets(self):
        """
        测试获取 所有 类型资产列表
        :return:
        """
        request = DescribeAssetsRequest(limit=1)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_asset(self):
        instance = GenerateInstance(id='bc248546-20ca-4bda-a735-bd47b475d931')
        request = DetailAssetRequest(instance=instance)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AssetInstance)

    def test_delete_asset(self):
        """
        测试删除指定资产
        """
        instance = GenerateInstance(id='ede0b1c1-9e2f-4355-acbf-7af9550a616b')
        request = DeleteAssetRequest(instance=instance)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    # --------------------- 主机类 ---------------------
    def test_list_hosts(self):
        """
        测试获取 主机 类型资产列表
        """
        request = DescribeHostsRequest(limit=1)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    # --------------------- 数据库类 ---------------------
    def test_list_databases(self):
        """
        测试获取 数据库 类型资产列表
        """
        request = DescribeDatabasesRequest(limit=1)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    # --------------------- 网络设备类 ---------------------
    def test_list_devices(self):
        """
        测试获取 网络设备 类型资产列表
        """
        request = DescribeDatabasesRequest(limit=1)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    # --------------------- 云服务类 ---------------------
    def test_list_clouds(self):
        """
        测试获取 云服务 类型资产列表
        """
        request = DescribeCloudsRequest(limit=1)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    # --------------------- Web 类 ---------------------
    def test_list_webs(self):
        """
        测试获取 Web 类型资产列表
        """
        request = DescribeWebsRequest(limit=1)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    # --------------------- GPT 类 ---------------------
    def test_list_gpts(self):
        """
        测试获取 Gpt 类型资产列表
        """
        request = DescribeGPTsRequest(limit=1)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    # --------------------- 自定义类 ---------------------
    def test_list_customs(self):
        """
        测试获取 自定义 类型资产列表
        """
        request = DescribeCustomsRequest(limit=1)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)


if __name__ == '__main__':
    unittest.main()
