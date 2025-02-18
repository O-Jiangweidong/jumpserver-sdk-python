import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.audits import (
    DescribeUserSessionsRequest, DetailUserSessionRequest,
)
from jms_client.v1.models.instance.audits import (
    UserSessionInstance,
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

    def test_list_user_sessions(self):
        """ 测试获取在线用户列表 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DescribeUserSessionsRequest(limit=2)
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_user_session(self):
        """ 测试获取指定 ID 在线用户详情 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DetailUserSessionRequest(id_='addfd032-7e27-4392-a01b-efcaa32c3ab1')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), UserSessionInstance)


if __name__ == '__main__':
    unittest.main()
