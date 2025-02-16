import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.const import (
    PlatformCategory, PlatformType, AutomationMethod
)
from jms_client.v1.models.request.assets import (
    DescribePlatformsRequest, DetailPlatformRequest,
    CreatePlatformRequest, UpdatePlatformRequest, DeletePlatformRequest,
    AutomationParam, ProtocolParam, SuParam
)
from jms_client.v1.models.instance import (
    PlatformInstance,
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

    def test_list_platforms(self):
        """ 测试获取平台列表 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DescribePlatformsRequest(
            limit=2, category=PlatformCategory.DEVICE
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_platform(self):
        """ 测试获取指定 ID 平台详情 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DetailPlatformRequest(id_='207')
        resp: Response = self.client.do(request, with_model=True)
        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), PlatformInstance)

    def test_create_platform(self):
        """ 测试创建平台 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        type_ = PlatformType.GENERAL
        # 配置协议
        protocols = ProtocolParam(type_=type_)
        protocols.append_ssh(port=3322)
        protocols.append_telnet(port=3323)
        # 配置用户切换方式
        su_param = SuParam(type_=type_)
        su_param.set_method_super_level()
        # 配置自动化任务
        automation = AutomationParam(type_=type_)
        automation.set_method(AutomationMethod.CHANGE_SECRET_BY_SSH)
        request = CreatePlatformRequest(
            id_='200', name='sdk-platform', type_=type_,
            comment='sdk-platform-comment',
            protocols=protocols, su=su_param, automation=automation
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), PlatformInstance)

    def test_update_platform(self):
        """ 测试更新指定 ID 平台属性 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        type_ = PlatformType.GENERAL
        # 配置协议
        protocols = ProtocolParam(type_=type_)
        protocols.append_ssh(port=2222)
        protocols.append_telnet(port=3333)
        # 配置用户切换方式
        su_param = SuParam(type_=type_)
        su_param.set_method_enable()
        # 配置自动化任务
        automation = AutomationParam(type_=type_)
        automation.set_method(AutomationMethod.PING_BY_TELNET)
        request = UpdatePlatformRequest(
            id_='200', name='sdk-platform-new', type_=type_,
            comment='sdk-platform-comment-new',
            protocols=protocols, su=su_param, automation=automation
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), PlatformInstance)

    def test_delete_platform(self):
        """ 测试删除指定 ID 平台 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DeletePlatformRequest(id_='200')
        resp: Response = self.client.do(request)

        self.assertTrue(resp.is_request_ok())


if __name__ == '__main__':
    unittest.main()
