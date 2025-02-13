from jms_client import client
from jms_client.const import ROOT_ORG, DEFAULT_ORG
from jms_client.v1.models.response import Response


class Client(object):
    """
    访问 JumpServer 资源客户端
    """

    def __init__(
            self, api_version=None, auth=None, auth_token=None, web_url=None,
            username=None, password=None, key_id=None, secret_id=None,
            session=None, timeout=None, **kwargs
    ):
        self.root_org = ROOT_ORG
        self.default_org = DEFAULT_ORG
        self.web_url = web_url[:-1] if web_url.endswith('/') else web_url
        self.client = client.construct_http_client(
            api_version=api_version, auth=auth, auth_token=auth_token, web_url=web_url,
            username=username, password=password, key_id=key_id, secret_id=secret_id,
            session=session, timeout=timeout, **kwargs
        )

    def set_org(self, org_id):
        """
        切换组织
        :param org_id: 组织 ID
        """
        self.client.set_org(org_id)

    def do(self, request_instance, with_model=False):
        """
        :param request_instance: 请求的实例
        :param with_model: 是否将数据转为 python 对应的实例对象，默认 False 是返回 json 格式
        :return:
        """
        response = self.client.request(
            url=request_instance.get_url(),
            method=request_instance.get_method(),
            headers=request_instance.get_headers(),
            data=request_instance.get_data(),
        )
        init_data = {'net_response': response}
        if with_model:
            init_data['ins_class'] = request_instance.InstanceClass
        return Response(**init_data)

    def ping(self):
        try:
            profile = self.user.get_profile()
            status = profile.is_active
        except Exception: # noqa
            status = False
        return status
