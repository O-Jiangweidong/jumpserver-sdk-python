import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.assets import (
    DescribeHostsRequest, DescribeDatabasesRequest,
    DescribeCloudsRequest, DescribeWebsRequest,
    DescribeGPTsRequest, DescribeCustomsRequest,
    DescribeAssetsRequest, DeleteAssetRequest,
    DetailAssetRequest, DetailHostRequest,
    DetailDeviceRequest, DetailDatabaseRequest,
    DetailCloudRequest, DetailWebRequest,
    DetailGPTRequest, DetailCustomRequest,
    CreateHostRequest, UpdateHostRequest,
)
from jms_client.v1.models.instance import (
    AssetInstance,
)
from jms_client.v1.models.response import Response


class TestFunctionality(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        config = configparser.ConfigParser()
        config.read('config.ini')
        username = config['test']['username']
        password = config['test']['password']
        self.client: Client = get_client(
            version='3.10', web_url='https://js-internal.fit2cloud.cn',
            username=username, password=password
        )

    # --------------------- 通用的 ---------------------
    def test_list_assets(self):
        """ 测试获取 所有 类型资产列表 """
        # 切换组织
        self.client.set_org(self.client.default_org)

        request = DescribeAssetsRequest(limit=1, search='jms')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)
        print(resp.get_data())

    def test_retrieve_asset(self):
        """ 测试获取指定 ID 资产详情 """
        request = DetailAssetRequest(id_='bc248546-20ca-4bda-a735-bd47b475d931')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AssetInstance)

    def test_delete_asset(self):
        """ 测试删除指定 ID 资产 """
        request = DeleteAssetRequest(id_='ede0b1c1-9e2f-4355-acbf-7af9550a616b')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())

    # --------------------- 主机类 ---------------------
    def test_list_hosts(self):
        """ 测试获取 主机 类型资产列表 """
        request = DescribeHostsRequest(limit=1)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_host(self):
        """ 测试获取指定 ID 主机详情 """
        request = DetailHostRequest(id_='bc248546-20ca-4bda-a735-bd47b475d931')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AssetInstance)

    def test_create_host(self):
        """ 测试创建主机类型资产 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = CreateHostRequest(
            name='sdk-host', address='1.1.1.1',
            domain='bf6682af-7056-413d-be80-302604129598',
            platform='32', nodes=[
                '02f821c7-a316-4e2e-a50b-e41faf59f68d'
            ],
            protocols=[{'name': 'ssh', 'port': '22'}],
            labels=['大西瓜:big', '水蜜桃:a']
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AssetInstance)

    def test_update_host(self):
        """ 测试更新指定 ID 主机资产属性 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = UpdateHostRequest(
            id_='c2e4dde4-c777-4b24-a084-a8b44e99b5a1',
            name='sdk-host-new', address='192.168.1.1',
            domain='bf6682af-7056-413d-be80-302604129598',
            platform='32', nodes=[
                '02f821c7-a316-4e2e-a50b-e41faf59f68d'
            ],
            protocols=[{'name': 'ssh', 'port': '22'}],
            labels=['新事物:new']
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AssetInstance)

    # --------------------- 数据库类 ---------------------
    def test_list_databases(self):
        """ 测试获取 数据库 类型资产列表 """
        request = DescribeDatabasesRequest(limit=1)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_database(self):
        """ 测试获取指定 ID 数据库详情 """
        request = DetailDatabaseRequest(id_='bc248546-20ca-4bda-a735-bd47b475d931')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AssetInstance)

    # --------------------- 网络设备类 ---------------------
    def test_list_devices(self):
        """ 测试获取 网络设备 类型资产列表 """
        request = DescribeDatabasesRequest(limit=1)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_device(self):
        """ 测试获取指定 ID 网络设备详情 """
        request = DetailDeviceRequest(id_='bc248546-20ca-4bda-a735-bd47b475d931')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AssetInstance)

    # --------------------- 云服务类 ---------------------
    def test_list_clouds(self):
        """ 测试获取 云服务 类型资产列表 """
        request = DescribeCloudsRequest(limit=1)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_cloud(self):
        """ 测试获取指定 ID 云服务详情 """
        request = DetailCloudRequest(id_='bc248546-20ca-4bda-a735-bd47b475d931')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AssetInstance)

    # --------------------- Web 类 ---------------------
    def test_list_webs(self):
        """ 测试获取 Web 类型资产列表 """
        request = DescribeWebsRequest(limit=1)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_web(self):
        """ 测试获取指定 ID Web资产详情 """
        request = DetailWebRequest(id_='bc248546-20ca-4bda-a735-bd47b475d931')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AssetInstance)

    # --------------------- GPT 类 ---------------------
    def test_list_gpts(self):
        """ 测试获取 Gpt 类型资产列表 """
        request = DescribeGPTsRequest(limit=1)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_gpt(self):
        """ 测试获取指定 ID GPT资产详情 """
        request = DetailGPTRequest(id_='2fb4b869-633f-44a0-a6cd-0dd76c859c3d')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AssetInstance)

    # --------------------- 自定义类 ---------------------
    def test_list_customs(self):
        """ 测试获取 自定义 类型资产列表 """
        request = DescribeCustomsRequest(limit=1)
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_custom(self):
        """ 测试获取指定 ID 自定义资产详情 """
        request = DetailCustomRequest(id_='bc248546-20ca-4bda-a735-bd47b475d931')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), AssetInstance)


if __name__ == '__main__':
    unittest.main()
