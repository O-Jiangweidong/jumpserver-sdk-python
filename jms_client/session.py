import requests

from httpsig.requests_auth import HTTPSignatureAuth

from .authentication import Password, Token, AccessKey
from .exceptions import JMSException
from .utils import LazyProperty


class Session(object):
    def __init__(self, auth):
        self.auth = auth

    def get_token(self):
        url = f'{self.auth.web_url}/api/v1/authentication/tokens/'
        data = {
            'username': self.auth.username, 'password': self.auth.password
        }
        response = requests.post(url=url, json=data, verify=False)
        try:
            response_json = response.json()
            token = f"{response_json['keyword']} {response_json['token']}"
        except Exception:
            raise JMSException(f'获取 Token 失败，原因：{response.text}')
        return token

    def get_access_key(self):
        signature_headers = ['(request-target)', 'accept', 'date']
        return HTTPSignatureAuth(
            key_id=self.auth.key_id, secret=self.auth.secret_id,
            algorithm='hmac-sha256', headers=signature_headers
        )

    @LazyProperty
    def token(self):
        token = None
        if isinstance(self.auth, Password):
            token = self.get_token()
        elif isinstance(self.auth, Token):
            token = self.auth.auth_token
        return token

    @LazyProperty
    def ak_auth(self):
        access_key = None
        if isinstance(self.auth, AccessKey):
            access_key = self.get_access_key()
        return access_key
