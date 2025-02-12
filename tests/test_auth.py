import unittest

from jms_client.client import get_client


class TestFunctionality(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        self.base_info = {
            'version': '3.10', 'web_url': 'https://jumpserver.org'
        }
        super().__init__(*args, **kwargs)

    def test_access_key_auth(self):
        """
        测试 AccessKey/SecretKey 认证
        :return:
        """
        client = get_client(
            access_key='access_key', secret_key='secret_key', **self.base_info
        )
        self.assertTrue(client.ping())

    def test_username_password_auth(self):
        """
        测试 用户名/密码 认证
        :return:
        """
        client = get_client(
            username='username', password='password', **self.base_info
        )
        self.assertTrue(client.ping())


if __name__ == '__main__':
    unittest.main()
