from jms_client.v1.models.instance.platforms import PlatformInstance
from ..common import Request
from ..const import (
    PlatformType, SuMethod, AutomationMethod,
    LINUX_AUTOMATION, WINDOWS_AUTOMATION, UNIX_AUTOMATION,
    GENERAL_AUTOMATION, SWITCH_AUTOMATION, ROUTER_AUTOMATION,
    FIREWALL_AUTOMATION, MYSQL_AUTOMATION, MARIADB_AUTOMATION,
    POSTGRESQL_AUTOMATION, ORACLE_AUTOMATION, SQLSERVER_AUTOMATION,
    MONGODB_AUTOMATION,
)
from ..mixins import ExtraRequestMixin, DetailMixin, CreateMixin


class BasePlatformRequest(Request):
    URL = 'assets/platforms/'
    InstanceClass = PlatformInstance


class DescribePlatformsRequest(ExtraRequestMixin, BasePlatformRequest):
    """
    获取平台列表
    """
    def __init__(
            self,
            name: str = '',
            category: str = '',
            type_: str = '',
            **kwargs
    ):
        """
        :param search: 条件搜索，支持名称
        :param name: 名称
        :param category: 类别
        :param type_: 类型
        :param kwargs: 其他参数
        """
        query_params = {}
        if name:
            query_params['name'] = name
        if category:
            query_params['category'] = category
        if type_:
            query_params['type'] = type_
        super().__init__(**query_params, **kwargs)


class DetailPlatformRequest(DetailMixin, BasePlatformRequest):
    """
    获取平台详情
    """


class ProtocolParam(object):
    def __init__(self, type_):
        self._protocols = []
        self.type = type_
        self._supported_protocols = {
            PlatformType.LINUX: ['ssh', 'sftp', 'telnet', 'vnc', 'rdp'],
            PlatformType.UNIX: ['ssh', 'sftp', 'telnet', 'vnc', 'rdp'],
            PlatformType.WINDOWS: ['ssh', 'sftp', 'vnc', 'rdp', 'winrm'],
            PlatformType.OTHER: ['ssh', 'sftp', 'telnet', 'vnc', 'rdp'],
            PlatformType.GENERAL: ['ssh', 'sftp', 'telnet'],
            PlatformType.SWITCH: ['ssh', 'sftp', 'telnet'],
            PlatformType.ROUTER: ['ssh', 'sftp', 'telnet'],
            PlatformType.FIREWALL: ['ssh', 'sftp', 'telnet'],
            PlatformType.MYSQL: ['mysql'],
            PlatformType.MARIADB: ['mariadb'],
            PlatformType.POSTGRESQL: ['postgresql'],
            PlatformType.ORACLE: ['oracle'],
            PlatformType.SQLSERVER: ['sqlserver'],
            PlatformType.DB2: ['db2'],
            PlatformType.DAMENG: ['dameng'],
            PlatformType.CLICKHOUSE: ['clickhouse'],
            PlatformType.MONGODB: ['mongodb'],
            PlatformType.REDIS: ['redis'],
            PlatformType.PRIVATE: ['http'],
            PlatformType.PUBLIC: ['http'],
            PlatformType.K8S: ['k8s'],
            PlatformType.WEBSITE: ['http'],
            PlatformType.CHATGPT: ['chatgpt'],
        }
        self._supported = self._supported_protocols.get(self.type, [])

    def get_protocols(self):
        return self._protocols

    def _append(self, name, protocol):
        if name not in self._supported:
            raise ValueError(
                f'Type {self.type} does not support the protocol {name}, '
                f'support {", ".join(self._supported)}'
            )
        self._protocols.append(protocol)

    def append_ssh(self, port=22, old_ssh_version=False, default=True):
        protocol = {
            'name': 'ssh', 'port': port,
            'default': default, 'public': True,
            'secret_types': ['password', 'ssh_key'],
            'setting': {'old_ssh_version': old_ssh_version},
        }
        self._append(name='ssh', protocol=protocol)

    def append_sftp(self, port=22, sftp_home='/tmp'):
        protocol = {
            'name': 'sftp', 'port': port, 'public': True,
            'secret_types': ['password', 'ssh_key'],
            'setting': {'sftp_home': sftp_home},
        }
        self._append(name='sftp', protocol=protocol)

    def append_telnet(
            self,
            port=23,
            username_prompt='username:|login:',
            password_prompt='password:',
            success_prompt=r'success|成功|#|>|\\$'
    ):
        protocol = {
            'name': 'telnet', 'port': port, 'public': True,
            'secret_types': ['password'],
            'setting': {
                'username_prompt': username_prompt,
                'password_prompt': password_prompt,
                'success_prompt': success_prompt,
            }
        }
        self._append(name='telnet', protocol=protocol)

    def append_vnc(self, port=5900):
        protocol = {
            'name': 'vnc', 'port': port, 'public': True,
            'secret_types': ['password'], 'setting': {},
        }
        self._append(name='vnc', protocol=protocol)

    def append_rdp(
            self,
            port=3389,
            console=False,
            security='any',
            ad_domain='',
            default=True
    ):
        protocol = {
            'name': 'rdp', 'port': port, 'default': default,
            'secret_types': ['password'], 'public': True,
            'setting': {
                'console': console, 'security': security, 'ad_domain': ad_domain,
            },
        }
        self._append(name='rdp', protocol=protocol)

    def append_winrm(self, port=5985, use_ssl=False):
        protocol = {
            'name': 'winrm', 'port': port,
            'secret_types': ['password'], 'public': False,
            'setting': {'use_ssl': use_ssl},
        }
        self._append(name='winrm', protocol=protocol)

    def append_mysql(self, port=3306):
        protocol = {
            'name': 'mysql', 'port': port,
            'required': True, 'default': True, 'public': True,
            'secret_types': ['password'], 'setting': {},
        }
        self._append(name='mysql', protocol=protocol)

    def append_mariadb(self, port=3306):
        protocol = {
            'name': 'mariadb', 'port': port,
            'required': True, 'default': True, 'public': True,
            'secret_types': ['password'], 'setting': {},
        }
        self._append(name='mariadb', protocol=protocol)

    def append_postgresql(self, port=5432):
        protocol = {
            'name': 'postgresql', 'port': port,
            'required': True, 'default': True,
            'xpack': True, 'public': True,
            'secret_types': ['password'], 'setting': {},
        }
        self._append(name='postgresql', protocol=protocol)

    def append_oracle(self, port=1521, sysdba=False):
        protocol = {
            'name': 'oracle', 'port': port,
            'required': True, 'default': True,
            'xpack': True, 'public': True,
            'secret_types': ['password'], 'setting': {
                'sysdba': sysdba,
            },
        }
        self._append(name='oracle', protocol=protocol)

    def append_sqlserver(
            self,
            port=1433,
            version='>=2014'  # >=2014/<2014
    ):
        protocol = {
            'name': 'sqlserver', 'port': port,
            'required': True, 'default': True,
            'xpack': True, 'public': True,
            'secret_types': ['password'], 'setting': {
                'version': version,
            },
        }
        self._append(name='sqlserver', protocol=protocol)

    def append_db2(self, port=5000):
        protocol = {
            'name': 'db2', 'port': port,
            'required': True, 'default': True,
            'xpack': True, 'public': True,
            'secret_types': ['password'], 'setting': {},
        }
        self._append(name='db2', protocol=protocol)

    def append_dameng(self, port=5236):
        protocol = {
            'name': 'dameng', 'port': port,
            'required': True, 'default': True, 'xpack': True,
            'secret_types': ['password'], 'setting': {},
        }
        self._append(name='dameng', protocol=protocol)

    def append_clickhouse(self, port=9000):
        protocol = {
            'name': 'clickhouse', 'port': port,
            'required': True, 'default': True,
            'xpack': True, 'public': True,
            'secret_types': ['password'], 'setting': {},
        }
        self._append(name='clickhouse', protocol=protocol)

    def append_mongodb(
            self,
            port=27017,
            auth_source='admin',
            connection_options=''
    ):
        protocol = {
            'name': 'mongodb', 'port': port,
            'required': True, 'default': True, 'public': True,
            'secret_types': ['password'], 'setting': {
                'auth_source': auth_source,
                'connection_options': connection_options,
            },
        }
        self._append(name='mongodb', protocol=protocol)

    def append_redis(self, port=6379, auth_username=False):
        protocol = {
            'name': 'redis', 'port': port,
            'required': True, 'default': True, 'public': True,
            'secret_types': ['password'], 'setting': {
                'auth_username': auth_username,
            },
        }
        self._append(name='redis', protocol=protocol)

    def append_http(
            self,
            port=80,
            port_from_attr=True,
            safe_mode=False,
            autofill='basic',  # no/basic/script
            username_selector='name=username',
            password_selector='name=password',
            submit_selector='type=submit',
            script=None
    ):
        protocol = {
            'name': 'http', 'port': port, 'port_from_attr': port_from_attr,
            'required': True, 'default': True, 'public': True,
            'secret_types': ['password'],
            'setting': {
                'safe_mode': safe_mode, 'autofill': autofill, 'script': script or [],
                'username_selector': username_selector,  'password_selector': password_selector,
                'submit_selector': submit_selector,
            }
        }
        self._append(name='http', protocol=protocol)

    def append_k8s(self, port=443, port_from_attr=True):
        protocol = {
            'name': 'mariadb', 'port': port,
            'required': True, 'default': True, 'public': True,
            'port_from_attr': port_from_attr,
            'secret_types': ['token'], 'setting': {},
        }
        self._append(name='k8s', protocol=protocol)

    def append_chatgpt(
            self,
            port=443,
            port_from_attr=True,
            api_mode='gpt-4o-mini'  # gpt-4o-mini/gpt-4o/gpt-4-turbo
    ):
        protocol = {
            'name': 'mariadb', 'port': port,
            'required': True, 'default': True, 'public': True,
            'port_from_attr': port_from_attr,
            'secret_types': ['api_key'], 'setting': {
                'api_mode': api_mode
            },
        }
        self._append(name='chatgpt', protocol=protocol)


class SuParam(object):
    def __init__(self, type_):
        self.type = type_
        self._su_info = {
            'su_enabled': False, 'su_method': ''
        }
        host_methods = [
            SuMethod.SU, SuMethod.SUDO, SuMethod.ONLY_SU, SuMethod.ONLY_SUDO
        ]
        device_methods = [
            SuMethod.ENABLE, SuMethod.SUPER, SuMethod.SUPER_LEVEL
        ]
        self._supported_methods = {
            PlatformType.LINUX: host_methods,
            PlatformType.UNIX: host_methods,
            PlatformType.GENERAL: device_methods,
            PlatformType.SWITCH: device_methods,
            PlatformType.ROUTER: device_methods,
            PlatformType.FIREWALL: device_methods,
        }
        self._supported = self._supported_methods.get(type_, [])

    def get_su_info(self):
        return self._su_info

    def set_method_su(self):
        self._set_su_method(SuMethod.SU)

    def set_method_sudo(self):
        self._set_su_method(SuMethod.SUDO)

    def set_method_only_su(self):
        self._set_su_method(SuMethod.ONLY_SU)

    def set_method_only_sudo(self):
        self._set_su_method(SuMethod.ONLY_SUDO)

    def set_method_enable(self):
        self._set_su_method(SuMethod.ENABLE)

    def set_method_super(self):
        self._set_su_method(SuMethod.SUPER)

    def set_method_super_level(self):
        self._set_su_method(SuMethod.SUPER_LEVEL)

    def _set_su_method(self, method: str):
        if method not in self._supported:
            raise ValueError(
                f'Type {self.type} does not support the method {method}, '
                f'support {", ".join(self._supported)}'
            )
        self._su_info['su_enabled'] = True
        self._su_info['su_method'] = str(method)


class AutomationParam(object):
    def __init__(self, type_=''):
        """ type_ 为资产类型，不传递则表示不开启自动化任务 """
        self.type = type_
        self._supported_methods: dict = {
            PlatformType.LINUX: LINUX_AUTOMATION,
            PlatformType.WINDOWS: WINDOWS_AUTOMATION,
            PlatformType.UNIX: UNIX_AUTOMATION,
            PlatformType.GENERAL: GENERAL_AUTOMATION,
            PlatformType.SWITCH: SWITCH_AUTOMATION,
            PlatformType.ROUTER: ROUTER_AUTOMATION,
            PlatformType.FIREWALL: FIREWALL_AUTOMATION,
            PlatformType.MYSQL: MYSQL_AUTOMATION,
            PlatformType.MARIADB: MARIADB_AUTOMATION,
            PlatformType.POSTGRESQL: POSTGRESQL_AUTOMATION,
            PlatformType.ORACLE: ORACLE_AUTOMATION,
            PlatformType.SQLSERVER: SQLSERVER_AUTOMATION,
            PlatformType.MONGODB: MONGODB_AUTOMATION,
        }

        self._automation_standard = self._supported_methods.get(type_, {})
        self._automation = self._set_default()

    def _set_default(self):
        default = {'ansible_enabled': False}
        if not self._automation_standard:
            return default

        for key, value in self._automation_standard.items():
            if key.endswith('_methods'):
                if isinstance(value, list) and len(value) > 0:
                    status = True
                    default[key[:-1]] = value[0]
                else:
                    status = False
                    default[key] = ''
                default[f'{key[:-8]}_enabled'] = status
            else:
                default[key] = value
        return default

    def set_method(self, method: str, enabled=True):
        category = AutomationMethod.get_category(method)
        if not category:
            raise ValueError(f'Automation method [{method}] is not defined')

        if not enabled:
            self._automation[f'{method[:-8]}_enabled'] = False
            return

        supported = self._automation_standard.get(f'{category}s', [])
        if method not in supported:
            raise ValueError(
                f'Automation method [{method}] is not supported, '
                f'support {", ".join(supported)}'
            )
        self._automation['ansible_enabled'] = True
        self._automation[category] = method

    def get_automation(self):
        return self._automation


class CreateUpdatePlatformParamsMixin(object):
    _body: dict

    def __init__(
            self,
            name: str,
            type_: str,
            charset: str = 'utf-8',  # utf-8/gbk
            domain_enabled: bool = True,
            su: SuParam = None,
            protocols: ProtocolParam = None,
            automation: AutomationParam = None,
            comment: str = '',
            **kwargs
    ):
        """
        :param name: 名称
        :param type_: 类型
        :param charset: 编码
        :param domain_enabled: 是否开启网域
        :param su: 切换用户配置项，具体参考 SuParam
        :param protocols: 支持的协议，具体参考 ProtocolParam
        :param automation: 自动化配置，具体参考 AutomationParam
        :param comment: 备注
        :param kwargs: 其他参数
        """
        super().__init__(**kwargs)
        self._body.update({
            'name': name,  'comment': comment, 'type': type_,
            'category': PlatformType(type_).get_category(),
            'charset': charset, 'domain_enabled': domain_enabled,
        })
        if isinstance(su, SuParam):
            self._body.update(su.get_su_info())
        if isinstance(protocols, ProtocolParam):
            self._body['protocols'] = protocols.get_protocols()
        automation = automation or AutomationParam()
        self._body['automation'] = automation.get_automation()


class CreatePlatformRequest(
    CreateUpdatePlatformParamsMixin, CreateMixin, BasePlatformRequest
):
    """ 创建 平台 """


class UpdatePlatformRequest(
    CreateUpdatePlatformParamsMixin, DetailMixin, BasePlatformRequest
):
    """ 更新 网域 """
    def get_method(self):
        return 'put'


class DeletePlatformRequest(DetailMixin, BasePlatformRequest):
    """ 删除指定 ID 的平台 """

    def get_method(self):
        return 'delete'
