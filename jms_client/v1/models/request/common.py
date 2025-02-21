from urllib.parse import urlencode

from .const import PlatformType


class Request(object):
    URL = ''
    InstanceClass = None

    def __init__(
            self, instance=None, **kwargs
    ):
        self.url_prefix = 'api/v1/'
        self.instance = instance
        self.other = kwargs
        self._body = {}

    @staticmethod
    def get_method():
        return 'get'

    @staticmethod
    def get_params():
        return {}

    def get_url(self):
        params = self.get_params()
        params.update(self.other)
        return f'{self.url_prefix}{self.URL}?{urlencode(params)}'

    def get_data(self):
        return self._body

    @staticmethod
    def get_headers():
        return {}


class ProtocolParam(object):
    def __init__(self, type_):
        self._pre_check = True
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

    def get_protocols(self, only_name=False):
        protocols = self._protocols
        if only_name:
            protocols = [p['name'] for p in protocols]
        return protocols

    def _append(self, name, protocol):
        if self._pre_check and name not in self._supported:
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
        return self

    def append_sftp(self, port=22, sftp_home='/tmp'):
        protocol = {
            'name': 'sftp', 'port': port, 'public': True,
            'secret_types': ['password', 'ssh_key'],
            'setting': {'sftp_home': sftp_home},
        }
        self._append(name='sftp', protocol=protocol)
        return self

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
        return self

    def append_vnc(self, port=5900):
        protocol = {
            'name': 'vnc', 'port': port, 'public': True,
            'secret_types': ['password'], 'setting': {},
        }
        self._append(name='vnc', protocol=protocol)
        return self

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
        return self

    def append_winrm(self, port=5985, use_ssl=False):
        protocol = {
            'name': 'winrm', 'port': port,
            'secret_types': ['password'], 'public': False,
            'setting': {'use_ssl': use_ssl},
        }
        self._append(name='winrm', protocol=protocol)
        return self

    def append_mysql(self, port=3306):
        protocol = {
            'name': 'mysql', 'port': port,
            'required': True, 'default': True, 'public': True,
            'secret_types': ['password'], 'setting': {},
        }
        self._append(name='mysql', protocol=protocol)
        return self

    def append_mariadb(self, port=3306):
        protocol = {
            'name': 'mariadb', 'port': port,
            'required': True, 'default': True, 'public': True,
            'secret_types': ['password'], 'setting': {},
        }
        self._append(name='mariadb', protocol=protocol)
        return self

    def append_postgresql(self, port=5432):
        protocol = {
            'name': 'postgresql', 'port': port,
            'required': True, 'default': True,
            'xpack': True, 'public': True,
            'secret_types': ['password'], 'setting': {},
        }
        self._append(name='postgresql', protocol=protocol)
        return self

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
        return self

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
        return self

    def append_db2(self, port=5000):
        protocol = {
            'name': 'db2', 'port': port,
            'required': True, 'default': True,
            'xpack': True, 'public': True,
            'secret_types': ['password'], 'setting': {},
        }
        self._append(name='db2', protocol=protocol)
        return self

    def append_dameng(self, port=5236):
        protocol = {
            'name': 'dameng', 'port': port,
            'required': True, 'default': True, 'xpack': True,
            'secret_types': ['password'], 'setting': {},
        }
        self._append(name='dameng', protocol=protocol)
        return self

    def append_clickhouse(self, port=9000):
        protocol = {
            'name': 'clickhouse', 'port': port,
            'required': True, 'default': True,
            'xpack': True, 'public': True,
            'secret_types': ['password'], 'setting': {},
        }
        self._append(name='clickhouse', protocol=protocol)
        return self

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
        return self

    def append_redis(self, port=6379, auth_username=False):
        protocol = {
            'name': 'redis', 'port': port,
            'required': True, 'default': True, 'public': True,
            'secret_types': ['password'], 'setting': {
                'auth_username': auth_username,
            },
        }
        self._append(name='redis', protocol=protocol)
        return self

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
        return self

    def append_k8s(self, port=443, port_from_attr=True):
        protocol = {
            'name': 'k8s', 'port': port,
            'required': True, 'default': True, 'public': True,
            'port_from_attr': port_from_attr,
            'secret_types': ['token'], 'setting': {},
        }
        self._append(name='k8s', protocol=protocol)
        return self

    def append_chatgpt(
            self,
            port=443,
            port_from_attr=True,
            api_mode='gpt-4o-mini'  # gpt-4o-mini/gpt-4o/gpt-4-turbo
    ):
        protocol = {
            'name': 'chatgpt', 'port': port,
            'required': True, 'default': True, 'public': True,
            'port_from_attr': port_from_attr,
            'secret_types': ['api_key'], 'setting': {
                'api_mode': api_mode
            },
        }
        self._append(name='chatgpt', protocol=protocol)
        return self


class UserParam(object):
    def __init__(self):
        self._users = {}
        self.set_all_users()

    def get_users(self):
        return self._users

    def set_all_users(self):
        self._users = {'type': 'all', 'username_group': ''}

    def set_specify_users(self, users: list):
        """
        :param users: 指定用户，格式为 ['user1_id', 'user2_id']
        """
        self._users = {'type': 'ids', 'ids': users}

    def set_attr_users(self, attrs: list):
        """
        :param attrs: 指定用户属性，格式为 [{'name': '', 'match': '', 'value': ''}]
            以下为 'name' 为某个属性时，match 支持的内容 及 value 的内容格式
            name: 用户名称、value: 值、match：
                in：在...中
                exact：等于
                not：不等于
                contains：包含
                startswith：以...开头
                endswith：以...结尾
                regex：正则表达式
            username: 用户名、value: 值、match：同上方 name 的 match 取值
            email: 邮箱、value: 值、match：同上方 name 的 match 取值
            comment: 备注、value: 值、match：同上方 name 的 match 取值
            is_active: 是否激活、value: True/False、match：
                exact：等于
                not：不等于
            is_first_login: 是否首次登录、value: True/False、match：同上方 is_active 的 match 取值
            system_roles: 系统角色、value: ['id1', 'id2']、match：
                m2m: 任意包含
                m2m_all: 同时包含
            org_roles: 组织角色、value: ['id1', 'id2']、match：同上方 system_roles 的 match 取值
            groups: 组、value: ['id1', 'id2']、match：同上方 system_roles 的 match 取值
        """
        str_match = ('in', 'exact', 'not', 'contains', 'startswith', 'endswith', 'regex')
        bool_match = ('exact', 'not')
        m2m_match = ('m2m', 'm2m_all')
        attr_rule_map = {
            'name': {'match': str_match}, 'username': {'match': str_match},
            'email': {'match': str_match}, 'comment': {'match': str_match},
            'is_active': {'match': bool_match}, 'is_first_login': {'match': bool_match},
            'system_roles': {'match': m2m_match}, 'org_roles': {'match': m2m_match},
            'groups': {'match': m2m_match},
        }
        for attr in attrs:
            name = attr.get('name')
            if not name or name not in attr_rule_map.keys():
                raise ValueError(f'Param attrs item name must be in {attr_rule_map.keys()}')

            match_value = attr.get('match', '')
            match_rule = attr_rule_map[name]['match']
            if match_value not in match_rule:
                raise ValueError(f'Param attrs [{name}] match must be in {match_rule}')
        self._users = {'type': 'attrs', 'attrs': attrs}
