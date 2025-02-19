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
    DescribeSessionsRequest, DetailSessionRequest,
    DescribeFTPLogsRequest, DetailFTPLogRequest,
    DescribeCommandsRequest, DetailCommandRequest,
)
from jms_client.v1.models.instance.audits import (
    UserSessionInstance, LoginLogInstance, OperateLogInstance,
    ChangePasswordLogInstance, JobLogInstance, SessionInstance,
    FTPLogInstance, CommandInstance,
)
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

    # --------------------- 会话记录 ---------------------
    def test_list_sessions(self):
        """ 测试获取会话记录列表 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DescribeSessionsRequest(
            limit=2, date_from='2024-06-01 00:00:00',
            date_to='2024-12-31 00:00:00'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_session(self):
        """ 测试获取指定 ID 会话详情 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DetailSessionRequest(id_='73afc136-11ea-4f89-afed-ea203d93a189')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), SessionInstance)

    # --------------------- FTP 记录 ---------------------
    def test_list_ftp_logs(self):
        """ 测试获取 FTP 日志列表 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DescribeFTPLogsRequest(
            limit=2, date_from='2024-06-01 00:00:00',
            date_to='2024-12-31 00:00:00'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_ftp_log(self):
        """ 测试获取指定 ID FTP 日志详情 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DetailFTPLogRequest(id_='6a85275b-9f3d-40c5-9304-942e9f2b9085')
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), FTPLogInstance)

    # --------------------- 命令记录 ---------------------
    def test_list_commands(self):
        """ 测试获取 命令记录 列表 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DescribeCommandsRequest(
            limit=2, date_from='2024-06-01 00:00:00',
            date_to='2024-12-31 00:00:00',
            command_storage_id='854dacc4-c6a8-4691-a56f-3adf2e954ff4'
        )
        resp: Response = self.client.do(request, with_model=True)

        print(resp.get_data())
        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), list)

    def test_retrieve_command(self):
        """ 测试获取指定 ID 命令记录详情 """
        self.client.set_org('7de34b6e-3319-49c2-ad8a-f8c3e4c470d2')
        request = DetailCommandRequest(
            id_='ae4f7f19-1169-48a8-81c5-bde9a5e09af5',
            command_storage_id='854dacc4-c6a8-4691-a56f-3adf2e954ff4'
        )
        resp: Response = self.client.do(request, with_model=True)

        self.assertTrue(resp.is_success())
        self.assertIsInstance(resp.get_data(), CommandInstance)


if __name__ == '__main__':
    unittest.main()
