import re

from typing import List

from .const import PlatformType, SecretType


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


class SimpleProtocolParam(ProtocolParam):
    def __init__(self):
        super().__init__(type_=None)
        self._pre_check = False


class ManyToManyFilterParam(object):
    str_match = ('in', 'exact', 'not', 'contains', 'startswith', 'endswith', 'regex')
    bool_match = ('exact', 'not')
    m2m_match = ('m2m', 'm2m_all')

    def __init__(self):
        self._results = {}
        self.set_all()

    def _get_attrs_rule_map(self):
        return {}

    def set_all(self):
        self._results = {'type': 'all'}

    def set_specify(self,  obj_ids: List):
        """
        :param obj_ids: 指定对象，格式为 ['obj1_id', 'obj2_id']
        """
        self._results = {'type': 'ids', 'ids': obj_ids}

    def set_filter_attrs(self, attrs: List):
        attrs_rule_map = self._get_attrs_rule_map()
        for attr in attrs:
            name = attr.get('name')
            if not name or name not in attrs_rule_map.keys():
                raise ValueError(f'Param attrs item name must be in {attrs_rule_map.keys()}')

            match_value = attr.get('match', '')
            match_rule = attrs_rule_map[name]['match']
            if match_value not in match_rule:
                raise ValueError(f'Param attrs [{name}] match must be in {match_rule}')
        self._results = {'type': 'attrs', 'attrs': attrs}

    def get_result(self):
        return self._results


class UserManyFilterParam(ManyToManyFilterParam):
    """
     :method set_specify(obj_ids: List => [user1_id, user2_id]): 指定用户

     :method set_filter_attrs(attrs: List => 具体用法看下方注释): 指定用户属性
        attrs: 用户属性，格式为 [{'name': '', 'match': '', 'value': ''}]
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

    def _get_attrs_rule_map(self):
        return {
            'name': {'match': self.str_match},
            'username': {'match': self.str_match},
            'email': {'match': self.str_match},
            'comment': {'match': self.str_match},
            'is_active': {'match': self.bool_match},
            'is_first_login': {'match': self.bool_match},
            'system_roles': {'match': self.m2m_match},
            'org_roles': {'match': self.m2m_match},
            'groups': {'match': self.m2m_match},
        }


class AssetManyFilterParam(ManyToManyFilterParam):
    """
     :method set_specify(obj_ids: List => [user1_id, user2_id]): 指定用户

     :method set_filter_attrs(attrs: List => 具体用法看下方注释): 指定资产属性
        attrs: 资产属性，格式为 [{'name': '', 'match': '', 'value': ''}]
            以下为 'name' 为某个属性时，match 支持的内容 及 value 的内容格式
            name: 用户名称、value: 值、match：
                in：在...中
                exact：等于
                not：不等于
                contains：包含
                startswith：以...开头
                endswith：以...结尾
                regex：正则表达式
            address: 地址、value: 值、match：同上方 name 的 match 取值
            comment: 备注、value: 值、match：同上方 name 的 match 取值
            nodes: 节点、value: ['id1', 'id2']、match：
                m2m: 任意包含
                m2m_all: 同时包含
            platform: 平台、value: ['id1', 'id2']、match：同上方 nodes 的 match 取值
            labels: 标签、value: ['id1', 'id2']、match：同上方 nodes 的 match 取值
            category: 平台类别、value: 参考 PlatformCategory 、match：
                in：在...中
            type: 平台类型、value: 参考 PlatformType 、match：同上方 category 的 match 取值
            protocols: 协议、value: 参考 ProtocolParam[only_name] 、match：同上方 category 的 match 取值
    """

    def _get_attrs_rule_map(self):
        only_in = ('in',)
        return {
            'name': {'match': self.str_match},
            'address': {'match': self.str_match},
            'comment': {'match': self.str_match},
            'platform': {'match': self.m2m_match},
            'nodes': {'match': self.m2m_match},
            'labels': {'match': self.m2m_match},
            'category': {'match': only_in},
            'type': {'match': only_in},
            'protocols': {'match': only_in},
        }


class PriorityParam(object):
    def __new__(cls, priority=50):
        try:
            priority = int(priority)
        except ValueError:
            raise ValueError('priority must be int')
        if priority < 0 or priority > 100:
            raise ValueError('priority must be in [0-100]')
        return priority


class AccountParam(object):
    ALL = '@ALL'
    INPUT = '@INPUT'
    SPEC = '@SPEC'
    ANON = '@ANON'
    USER = '@USER'

    def __init__(self):
        self._accounts = []

    def get_accounts(self):
        if {self.ALL, self.SPEC}.issubset(set(self._accounts)):
            raise ValueError('AccountParam 中不能同时包含 所有账号 和 指定账号')
        return self._accounts

    def with_all(self):
        self._accounts.append(self.ALL)
        return self

    def with_input(self):
        """ 设置手动账号 """
        self._accounts.append(self.INPUT)
        return self

    def with_user(self):
        """ 设置同名账号 """
        self._accounts.append(self.USER)
        return self

    def with_spec(self, username: List):
        """ 设置指定账号
        :param username:
        """
        self._accounts.extend([self.SPEC, *username])
        return self

    def with_anon(self):
        """ 设置匿名账号 """
        self._accounts.append(self.ANON)
        return self


class RuleParam(object):
    def __init__(self):
        self._time_pattern = re.compile(
            r'^(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])~(0[0-9]|1[0-9]|2[0-3]):([0-5][0-9])$'
        )
        self._time_period = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
        self._rule = {'ip_group': ['*']}

    def get_rule(self):
        self._rule['time_period'] = [
            {'id': k, 'value': '、'.join(v)} for k, v in self._time_period.items()
        ]
        return self._rule

    def set_ip_group(self, ip_groups: List):
        self._rule['ip_group'] = ip_groups

    def set_time_period(self, weeks: List[int], time_periods: List):
        """
        :param weeks: 星期，取值范围 0-6、分别代表星期日至星期六
        :param time_periods: 时间段，元素格式为 00:00~00:00
        """
        for week in weeks:
            if week not in self._time_period.keys():
                raise ValueError('week must be in [0-6]')

        for time_period in time_periods:
            if not self._time_pattern.match(time_period):
                raise ValueError('time_period must be in format 00:00~00:00')
            for week in weeks:
                self._time_period[week].append(time_period)


class PushParam(object):
    def __init__(self):
        self._result = {}

    def get_result(self):
        return self._result

    def set_aix_params(
            self,
            groups: List = None,
            home: str = '',
            modify_sudo: bool = False,
            shell: str = '/bin/bash',
            sudo: str = '/bin/whoami'
    ):
        groups = groups or []
        self._result['push_account_aix'] = {
            'groups': ','.join(groups), 'home': home, 'sudo': sudo,
            'modify_sudo': modify_sudo, 'shell': shell,
        }

    def set_windows_params(self, groups: List = None):
        groups = groups or ['Users', 'Remote Desktop Users']
        self._result['push_account_local_windows'] = {
            'groups': ','.join(groups)
        }

    def set_posix_params(
            self,
            groups: List = None,
            home: str = '',
            modify_sudo: bool = False,
            shell: str = '/bin/bash',
            sudo: str = '/bin/whoami'
    ):
        groups = groups or []
        self._result['push_account_posix'] = {
            'groups': ','.join(groups), 'home': home, 'sudo': sudo,
            'modify_sudo': modify_sudo, 'shell': shell,
        }


class AccountListParam(object):
    def __init__(self):
        self._result = []

    def get_result(self):
        return self._result

    def add_account(
            self,
            name: str,
            username: str,
            secret: str = '',
            is_active: bool = True,
            privileged: bool = False,
            push_now: bool = False,
            secret_type: str = SecretType.PASSWORD,
            params: PushParam = None,

    ):
        if push_now and not isinstance(params, PushParam):
            params = PushParam()
        secret_type = SecretType(secret_type)
        self._result.append({
            'name': name, 'username': username, 'secret': secret,
            'is_active': bool(is_active), 'push_now': bool(push_now),
            'privileged': bool(privileged), 'secret_type': secret_type,
            'params': params.get_result()
        })
