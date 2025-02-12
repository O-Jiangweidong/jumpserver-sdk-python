class BaseAuth(object):
    def __init__(self, web_url):
        self.web_url = web_url


class Token(BaseAuth):
    def __init__(self, web_url, auth_token):
        super().__init__(web_url)
        self.auth_token = auth_token


class Password(BaseAuth):
    def __init__(self, web_url, username, password):
        super().__init__(web_url)
        self.username = username
        self.password = password


class AccessKey(BaseAuth):
    def __init__(self, web_url, key_id, secret_id):
        super().__init__(web_url)
        self.key_id = key_id
        self.secret_id = secret_id
