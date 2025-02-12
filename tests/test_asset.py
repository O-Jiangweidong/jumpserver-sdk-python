import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.assets import (
    DescribeHostsRequest, DescribeDatabasesRequest,
    DescribeCloudsRequest, DescribeWebsRequest,
    DescribeGPTsRequest, DescribeCustomsRequest,
    DescribeAssetsRequest, DeleteAssetRequest,
)
from jms_client.v1.models.instance import (
    GenerateDeleteInstance,
)
from jms_client.v1.models.response import Response


class TestFunctionality(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client: Client = get_client(
            version='3.10', web_url='https://js-internal.fit2cloud.cn',
            username='jumpserver', password='Calong@2015'
        )

    def test_retrieve_assets(self):
        """
        测试获取 所有 类型资产列表
        :return:
        """
        request = DescribeAssetsRequest(limit=1)
        resp: Response = self.client.do(request, with_model=True)
        is_ok = resp.is_success()
        self.assertTrue(is_ok)

        result = resp.get_data()
        print(result)
        self.assertIsInstance(result, list)

    def test_delete_asset(self):
        """
        测试删除指定资产
        """
        instance = GenerateDeleteInstance(id='ede0b1c1-9e2f-4355-acbf-7af9550a616b')
        request = DeleteAssetRequest(instance=instance)
        resp: Response = self.client.do(request)
        is_ok = resp.is_request_ok()
        self.assertTrue(is_ok)

    def test_retrieve_hosts(self):
        """
        测试获取 主机 类型资产列表
        """
        request = DescribeHostsRequest(limit=1)
        resp: Response = self.client.do(request)
        is_ok = resp.is_success()
        self.assertTrue(is_ok)

        result = resp.get_data()
        self.assertIsInstance(result, list)

    def test_retrieve_databases(self):
        """
        测试获取 数据库 类型资产列表
        """
        request = DescribeDatabasesRequest(limit=1)
        resp: Response = self.client.do(request)
        is_ok = resp.is_success()
        self.assertTrue(is_ok)

        result = resp.get_data()
        self.assertIsInstance(result, list)

    def test_retrieve_devices(self):
        """
        测试获取 网络设备 类型资产列表
        """
        request = DescribeDatabasesRequest(limit=1)
        resp: Response = self.client.do(request)
        is_ok = resp.is_success()
        self.assertTrue(is_ok)

        result = resp.get_data()
        self.assertIsInstance(result, list)

    def test_retrieve_clouds(self):
        """
        测试获取 云服务 类型资产列表
        """
        request = DescribeCloudsRequest(limit=1)
        resp: Response = self.client.do(request)
        is_ok = resp.is_success()
        self.assertTrue(is_ok)

        result = resp.get_data()
        self.assertIsInstance(result, list)

    def test_retrieve_webs(self):
        """
        测试获取 Web 类型资产列表
        """
        request = DescribeWebsRequest(limit=1)
        resp: Response = self.client.do(request)
        is_ok = resp.is_success()
        self.assertTrue(is_ok)

        result = resp.get_data()
        self.assertIsInstance(result, list)

    def test_retrieve_gpts(self):
        """
        测试获取 Gpt 类型资产列表
        """
        request = DescribeGPTsRequest(limit=1)
        resp: Response = self.client.do(request)
        is_ok = resp.is_success()
        self.assertTrue(is_ok)

        result = resp.get_data()
        self.assertIsInstance(result, list)

    def test_retrieve_customs(self):
        """
        测试获取 自定义 类型资产列表
        """
        request = DescribeCustomsRequest(limit=1)
        resp: Response = self.client.do(request)
        is_ok = resp.is_success()
        self.assertTrue(is_ok)

        result = resp.get_data()
        self.assertIsInstance(result, list)


if __name__ == '__main__':
    unittest.main()
