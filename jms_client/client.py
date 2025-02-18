import requests

from datetime import datetime

from . import authentication, session as jms_session
from .const import DEFAULT_ORG
from .utils import record_time, import_string


class SessionClient(object):
    def __init__(self, session, *args, **kwargs):
        self.timer = 0  # 用于统计接口耗时
        self.org_id = DEFAULT_ORG
        self.session = session
        self.web_url = session.auth.web_url
        self.api_version = kwargs.pop('api_version', None)

    def set_org(self, org_id):
        self.org_id = org_id

    @record_time
    def request(self, url, method, headers=None, data=None, **kwargs):
        headers, data = headers or {}, data or {}
        request_headers = {
            'X-JMS-ORG': self.org_id,
            'Accept': 'application/json',
            'Date': datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        }
        if self.session.token:
            request_headers['Authorization'] = self.session.token
        request_headers.update(headers)

        action = getattr(requests, method, 'get')
        return action(
            f'{self.web_url}/{url}', auth=self.session.ak_auth,
            headers=request_headers, json=data, verify=False
        )


def construct_http_client(
        api_version=None, auth=None, auth_token=None, web_url=None,
        username=None, password=None, key_id=None, secret_id=None,
        session=None, **kwargs
):
    if not session:
        if key_id and secret_id:
            auth = authentication.AccessKey(
                web_url=web_url, key_id=key_id, secret_id=secret_id
            )
        if not auth and auth_token:
            auth = authentication.Token(web_url=web_url, auth_token=auth_token)
        elif not auth:
            auth = authentication.Password(
                web_url=web_url, username=username, password=password,
            )
        session = jms_session.Session(auth=auth)

    return SessionClient(
        api_version=api_version, auth=auth, session=session, **kwargs
    )


def _get_client_class_and_version(version):
    # 先写死，后期换成 ApiVersion 对象管理
    return version, import_string("jms_client.v1.client.Client")


def get_client(
        version, username=None, password=None, web_url=None,
        access_key=None, secret_key=None, **kwargs
):
    """
    :param web_url: JumpServer 堡垒机网页地址，如 127.0.0.1：8080
    :param version: JumpServer 堡垒机版本信息，如 3.10
    :param access_key: JumpServer 个人信息- API Key - ID
    :param secret_key: JumpServer 个人信息- API Key - Secret
    :param username: 登陆 JumpServer 的用户名
    :param password: 登陆 JumpServer 的密码
    :param kwargs: 其他参数
    :return: JMSClient
    """
    api_version, client_class = _get_client_class_and_version(version)
    web_url = web_url[:-1] if web_url.endswith('/') else web_url
    return client_class(
        api_version=api_version, web_url=web_url,
        username=username, password=password,
        key_id=access_key, secret_id=secret_key,
        **kwargs
    )
