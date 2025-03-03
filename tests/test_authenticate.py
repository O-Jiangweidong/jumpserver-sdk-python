import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.models.request.users import UserProfileRequest
from jms_client.v1.models.response import Response
from jms_client.v1.models.instance.users import UserProfileInstance


class TestFunctionality(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

    def _assert_response(self, client):
        resp: Response = client.do(UserProfileRequest(), with_model=True)
        user: UserProfileInstance = resp.get_data()

        self.assertTrue(resp.is_request_ok())
        self.assertTrue(user.is_active)

    def test_access_key_auth(self):
        """ 测试 AccessKey/SecretKey 认证 """
        web_url = self.config['test']['web_url']
        version = self.config['test']['version']
        access_key = self.config['test']['access_key']
        secret_key = self.config['test']['secret_key']
        client = get_client(
            web_url=web_url, version=version,
            access_key=access_key, secret_key=secret_key,
        )
        self._assert_response(client)

    def test_username_password_auth(self):
        """ 测试 用户名/密码 认证 """
        web_url = self.config['test']['web_url']
        version = self.config['test']['version']
        username = self.config['test']['username']
        password = self.config['test']['password']
        client = get_client(
            web_url=web_url, version=version,
            username=username, password=password
        )
        self._assert_response(client)


if __name__ == '__main__':
    unittest.main()
