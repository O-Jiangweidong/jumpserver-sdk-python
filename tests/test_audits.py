import configparser

import unittest

from jms_client.client import get_client
from jms_client.v1.client import Client
from jms_client.v1.models.request.audits import (
    DescribeUserSessionsRequest, DetailUserSessionRequest,
    DescribeLoginLogsRequest, DetailLoginLogRequest,
    DescribeOperateLogsRequest, DetailOperateLogRequest,
    DescribeChangePasswordLogsRequest, DetailChangePasswordLogRequest,
    DescribeJobLogsRequest, DetailJobLogRequest,
)
from jms_client.v1.models.instance.audits import (
    UserSessionInstance, LoginLogInstance, OperateLogInstance,
    ChangePasswordLogInstance, JobLogInstance,
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

    # --------------------- 在线用户 ---------------------
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

    # --------------------- 登录日志 ---------------------
    def test_list_login_logs(self):
        """ 测试获取登录日志列表 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DescribeLoginLogsRequest(
            limit=2, date_from='2024-06-01 00:00:00',
            date_to='2024-12-31 00:00:00'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_login_logs(self):
        """ 测试获取指定 ID 登录日志详情 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DetailLoginLogRequest(id_='031f14a5-362c-4647-b66f-75e43bf0bde6')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), LoginLogInstance)

    # --------------------- 操作日志 ---------------------
    def test_list_operate_logs(self):
        """ 测试获取操作日志列表 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DescribeOperateLogsRequest(
            limit=2, date_from='2024-06-01 00:00:00',
            date_to='2024-12-31 00:00:00'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_operate_logs(self):
        """ 测试获取指定 ID 操作日志详情 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DetailOperateLogRequest(id_='06f9a4c4-8685-463b-b23d-192e6177bb33')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), OperateLogInstance)

    # --------------------- 改密日志 ---------------------
    def test_list_change_password_logs(self):
        """ 测试获取用户改密日志列表 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DescribeChangePasswordLogsRequest(
            limit=2, date_from='2024-06-01 00:00:00',
            date_to='2024-12-31 00:00:00'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_change_password_logs(self):
        """ 测试获取指定 ID 用户改密日志详情 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DetailChangePasswordLogRequest(id_='7e50357d-dea7-4ca6-95d6-615b38343c90')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), ChangePasswordLogInstance)

    # --------------------- 作业日志 ---------------------
    def test_list_job_logs(self):
        """ 测试获取作业日志列表 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DescribeJobLogsRequest(
            limit=2, date_from='2024-06-01 00:00:00',
            date_to='2024-12-31 00:00:00'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_job_logs(self):
        """ 测试获取指定 ID 作业日志详情 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DetailJobLogRequest(id_='250b2665-3a5e-43ea-81a2-9ae54172a5e3')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), JobLogInstance)


if __name__ == '__main__':
    unittest.main()
