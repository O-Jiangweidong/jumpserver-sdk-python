from enum import Enum


class PlatformCategory(str, Enum):
    HOST = 'host'
    DEVICE = 'device'
    DATABASE = 'database'
    CLOUD = 'cloud'
    WEB = 'web'
    GPT = 'gpt'
    CUSTOM = 'custom'

    def __str__(self) -> str:
        return self.value


# Platform
class PlatformType(str, Enum):
    # Host
    LINUX = 'linux'
    WINDOWS = 'windows'
    UNIX = 'unix'
    OTHER = 'other'
    # Device
    GENERAL = 'general'
    SWITCH = 'switch'
    ROUTER = 'router'
    FIREWALL = 'firewall'
    # Database
    MYSQL = 'mysql'
    MARIADB = 'mariadb'
    POSTGRESQL = 'postgresql'
    ORACLE = 'oracle'
    SQLSERVER = 'sqlserver'
    DB2 = 'db2'
    DAMENG = 'dameng'
    CLICKHOUSE = 'clickhouse'
    MONGODB = 'mongodb'
    REDIS = 'redis'
    # Cloud
    PUBLIC = 'public'
    PRIVATE = 'private'
    K8S = 'k8s'
    # Web
    WEBSITE = 'website'
    # GPT
    CHATGPT = 'chatgpt'
    # Custom 为动态创建的，这里先不搞了
    CUSTOM = 'custom'

    def __str__(self) -> str:
        return self.value

    def get_category(self):
        category = self.CUSTOM
        if self.value in (
            self.LINUX, self.WINDOWS, self.UNIX, self.OTHER
        ):
            category = PlatformCategory.HOST
        elif self.value in (
            self.GENERAL, self.SWITCH, self.ROUTER, self.FIREWALL
        ):
            category = PlatformCategory.DEVICE
        elif self.value in (
            self.MYSQL, self.MARIADB, self.POSTGRESQL, self.ORACLE,
            self.SQLSERVER, self.DB2, self.DAMENG, self.CLICKHOUSE,
            self.MONGODB, self.REDIS
        ):
            category = PlatformCategory.DATABASE
        elif self.value in (
            self.PUBLIC, self.PRIVATE, self.K8S
        ):
            category = PlatformCategory.CLOUD
        elif self.value in (self.WEBSITE, ):
            category = PlatformCategory.WEB
        elif self.value in (self.CHATGPT, ):
            category = PlatformCategory.GPT
        return category


class SuMethod(str, Enum):
    SUDO = 'sudo'
    SU = 'su'
    ONLY_SUDO = 'only_sudo'
    ONLY_SU = 'only_su'
    ENABLE = 'enable'
    SUPER = 'super'
    SUPER_LEVEL = 'super_level'

    def __str__(self) -> str:
        return self.value


class AutomationMethod(str, Enum):
    # PING
    POSIX_PING = 'posix_ping'
    PING_BY_SSH = 'ping_by_ssh'
    PING_BY_TELNET = 'ping_by_telnet'
    PING_BY_RDP = 'ping_by_rdp'
    WIN_PING = 'win_ping'
    MYSQL_PING = 'mysql_ping'
    MONGODB_PING = 'mongodb_ping'
    POSTGRESQL_PING = 'ping_postgresql'
    ORACLE_PING = 'oracle_ping'
    SQLSERVER_PING = 'sqlserver_ping'
    # Gather facts
    GATHER_FACTS_POSIX = 'gather_facts_posix'
    GATHER_FACTS_WINDOWS = 'gather_facts_windows'
    # Gather account
    GATHER_ACCOUNTS_POSIX = 'gather_accounts_posix'
    GATHER_ACCOUNTS_WINDOWS = 'gather_accounts_windows'
    GATHER_ACCOUNTS_MONGODB = 'gather_accounts_mongodb'
    GATHER_ACCOUNTS_MYSQL = 'gather_accounts_mysql'
    GATHER_ACCOUNTS_POSTGRESQL = 'gather_accounts_postgresql'
    GATHER_ACCOUNTS_ORACLE = 'gather_accounts_oracle'
    # Verify account
    VERIFY_ACCOUNT_POSIX = 'verify_account_posix'
    VERIFY_ACCOUNT_BY_SSH = 'verify_account_by_ssh'
    VERIFY_ACCOUNT_BY_RDP = 'verify_account_by_rdp'
    VERIFY_ACCOUNT_WINDOWS = 'verify_account_windows'
    VERIFY_ACCOUNT_MONGODB = 'verify_account_mongodb'
    VERIFY_ACCOUNT_MYSQL = 'verify_account_mysql'
    VERIFY_ACCOUNT_POSTGRESQL = 'verify_account_postgresql'
    VERIFY_ACCOUNT_ORACLE = 'verify_account_oracle'
    VERIFY_ACCOUNT_SQLSERVER = 'verify_account_sqlserver'
    # Change account
    CHANGE_SECRET_POSIX = 'change_secret_posix'
    CHANGE_SECRET_BY_SSH = 'change_secret_by_ssh'
    CHANGE_SECRET_LOCAL_WINDOWS = 'change_secret_local_windows'
    CHANGE_SECRET_WINDOWS_RDP_VERIFY = 'change_secret_windows_rdp_verify'
    CHANGE_SECRET_MONGODB = 'change_secret_mongodb'
    CHANGE_SECRET_MYSQL = 'change_secret_mysql'
    CHANGE_SECRET_POSTGRESQL = 'change_secret_postgresql'
    CHANGE_SECRET_ORACLE = 'change_secret_oracle'
    CHANGE_SECRET_SQLSERVER = 'change_secret_sqlserver'
    # Push account
    PUSH_ACCOUNT_POSIX = 'push_account_posix'
    PUSH_ACCOUNT_LOCAL_WINDOWS = 'push_account_local_windows'
    PUSH_ACCOUNT_WINDOWS_RDP_VERIFY = 'push_account_windows_rdp_verify'
    PUSH_ACCOUNT_MONGODB = 'push_account_mongodb'
    PUSH_ACCOUNT_MYSQL = 'push_account_mysql'
    PUSH_ACCOUNT_POSTGRESQL = 'push_account_postgresql'
    PUSH_ACCOUNT_ORACLE = 'push_account_oracle'
    PUSH_ACCOUNT_SQLSERVER = 'push_account_sqlserver'

    def __str__(self) -> str:
        return self.value

    @classmethod
    def get_category(cls, method):
        category = ''
        if method in (
                cls.POSIX_PING, cls.PING_BY_SSH,
                cls.PING_BY_TELNET, cls.PING_BY_RDP,
                cls.WIN_PING, cls.MYSQL_PING,
                cls.MONGODB_PING, cls.POSTGRESQL_PING,
                cls.ORACLE_PING, cls.SQLSERVER_PING
        ):
            category = 'ping_method'
        elif method in (
            cls.GATHER_FACTS_POSIX, cls.GATHER_FACTS_WINDOWS
        ):
            category = 'gather_facts_method'
        elif method in (
            cls.GATHER_ACCOUNTS_POSIX, cls.GATHER_ACCOUNTS_WINDOWS,
            cls.GATHER_ACCOUNTS_MONGODB, cls.GATHER_ACCOUNTS_MYSQL,
            cls.GATHER_ACCOUNTS_POSTGRESQL, cls.GATHER_ACCOUNTS_ORACLE,
        ):
            category = 'gather_accounts_method'
        elif method in (
            cls.VERIFY_ACCOUNT_POSIX, cls.VERIFY_ACCOUNT_BY_SSH,
            cls.VERIFY_ACCOUNT_BY_RDP, cls.VERIFY_ACCOUNT_WINDOWS,
            cls.VERIFY_ACCOUNT_MONGODB, cls.VERIFY_ACCOUNT_MYSQL,
            cls.VERIFY_ACCOUNT_POSTGRESQL, cls.VERIFY_ACCOUNT_ORACLE,
            cls.VERIFY_ACCOUNT_SQLSERVER
        ):
            category = 'verify_account_method'
        elif method in (
            cls.CHANGE_SECRET_POSIX, cls.CHANGE_SECRET_BY_SSH,
            cls.CHANGE_SECRET_LOCAL_WINDOWS, cls.CHANGE_SECRET_WINDOWS_RDP_VERIFY,
            cls.CHANGE_SECRET_MONGODB, cls.CHANGE_SECRET_MYSQL,
            cls.CHANGE_SECRET_POSTGRESQL, cls.CHANGE_SECRET_ORACLE,
            cls.CHANGE_SECRET_SQLSERVER
        ):
            category = 'change_secret_method'
        elif method in (
            cls.PUSH_ACCOUNT_POSIX, cls.PUSH_ACCOUNT_LOCAL_WINDOWS,
            cls.PUSH_ACCOUNT_WINDOWS_RDP_VERIFY, cls.PUSH_ACCOUNT_MONGODB,
            cls.PUSH_ACCOUNT_MYSQL, cls.PUSH_ACCOUNT_POSTGRESQL,
            cls.PUSH_ACCOUNT_ORACLE, cls.PUSH_ACCOUNT_SQLSERVER
        ):
            category = 'push_account_method'
        return category


LINUX_AUTOMATION = {
    'ansible_config': {
        'ansible_connection': 'smart'
    },
    'ping_methods': [
        AutomationMethod.POSIX_PING,
        AutomationMethod.PING_BY_SSH,
        AutomationMethod.PING_BY_TELNET,
    ],
    'gather_facts_methods': [
        AutomationMethod.GATHER_FACTS_POSIX
    ],
    'gather_accounts_methods': [
        AutomationMethod.GATHER_ACCOUNTS_POSIX
    ],
    'verify_account_methods': [
        AutomationMethod.VERIFY_ACCOUNT_POSIX,
        AutomationMethod.VERIFY_ACCOUNT_BY_SSH,
    ],
    'change_secret_methods': [
        AutomationMethod.CHANGE_SECRET_POSIX,
        AutomationMethod.CHANGE_SECRET_BY_SSH,
    ],
    'push_account_methods': [
        AutomationMethod.PUSH_ACCOUNT_POSIX
    ]
}
WINDOWS_AUTOMATION = {
    'ansible_config': {
        'ansible_shell_type': 'cmd',
        'ansible_connection': 'smart'
    },
    'ping_methods': [
        AutomationMethod.PING_BY_RDP,
        AutomationMethod.WIN_PING,
        AutomationMethod.PING_BY_SSH,
        AutomationMethod.PING_BY_TELNET,
    ],
    'gather_facts_methods': [
        AutomationMethod.GATHER_FACTS_WINDOWS,
    ],
    'gather_accounts_methods': [
        AutomationMethod.GATHER_ACCOUNTS_WINDOWS
    ],
    'verify_account_methods': [
        AutomationMethod.VERIFY_ACCOUNT_BY_RDP,
        AutomationMethod.VERIFY_ACCOUNT_WINDOWS,
        AutomationMethod.VERIFY_ACCOUNT_BY_SSH
    ],
    'change_secret_methods': [
        AutomationMethod.CHANGE_SECRET_LOCAL_WINDOWS,
        AutomationMethod.CHANGE_SECRET_WINDOWS_RDP_VERIFY,
        AutomationMethod.CHANGE_SECRET_BY_SSH
    ],
    'push_account_methods': [
        AutomationMethod.PUSH_ACCOUNT_LOCAL_WINDOWS,
        AutomationMethod.PUSH_ACCOUNT_WINDOWS_RDP_VERIFY
    ]
}
UNIX_AUTOMATION = {
    'ansible_config': {
        'ansible_connection': 'smart'
    },
    'ping_methods': [
        AutomationMethod.POSIX_PING,
        AutomationMethod.PING_BY_SSH,
        AutomationMethod.PING_BY_TELNET
    ],
    'gather_facts_methods': [
        AutomationMethod.GATHER_FACTS_POSIX
    ],
    'gather_accounts_methods': [
        AutomationMethod.GATHER_ACCOUNTS_POSIX,
    ],
    'verify_account_methods': [
        AutomationMethod.VERIFY_ACCOUNT_POSIX,
        AutomationMethod.VERIFY_ACCOUNT_BY_SSH
    ],
    'change_secret_methods': [
        AutomationMethod.CHANGE_SECRET_POSIX,
        AutomationMethod.CHANGE_SECRET_BY_SSH
    ],
    'push_account_methods': [
        AutomationMethod.PUSH_ACCOUNT_POSIX
    ]
}
GENERAL_AUTOMATION = {
    'ansible_config': {
        'ansible_connection': 'local',
        'first_conn_delay_time': 0.5
    },
    'ping_methods': [
        AutomationMethod.PING_BY_SSH,
        AutomationMethod.PING_BY_TELNET
    ],
    'verify_account_methods': [
        AutomationMethod.VERIFY_ACCOUNT_BY_SSH
    ],
    'change_secret_methods': [
        AutomationMethod.CHANGE_SECRET_BY_SSH
    ]
}
SWITCH_AUTOMATION = GENERAL_AUTOMATION
ROUTER_AUTOMATION = GENERAL_AUTOMATION
FIREWALL_AUTOMATION = GENERAL_AUTOMATION
MYSQL_AUTOMATION = {
    'ansible_config': {
        'ansible_connection': 'local'
    },
    'ping_methods': [
        AutomationMethod.MYSQL_PING
    ],
    'gather_accounts_methods': [
        AutomationMethod.GATHER_ACCOUNTS_MYSQL
    ],
    'verify_account_methods': [
        AutomationMethod.VERIFY_ACCOUNT_MYSQL
    ],
    'change_secret_methods': [
        AutomationMethod.CHANGE_SECRET_MYSQL
    ],
    'push_account_methods': [
        AutomationMethod.PUSH_ACCOUNT_MYSQL
    ]
}
MARIADB_AUTOMATION = MYSQL_AUTOMATION
POSTGRESQL_AUTOMATION = {
    'ansible_config': {
        'ansible_connection': 'local'
    },
    'ping_methods': [
        AutomationMethod.POSTGRESQL_PING
    ],
    'gather_accounts_methods': [
        AutomationMethod.GATHER_ACCOUNTS_POSTGRESQL
    ],
    'verify_account_methods': [
        AutomationMethod.VERIFY_ACCOUNT_POSTGRESQL
    ],
    'change_secret_methods': [
        AutomationMethod.CHANGE_SECRET_POSTGRESQL
    ],
    'push_account_methods': [
        AutomationMethod.PUSH_ACCOUNT_POSTGRESQL
    ]
}
ORACLE_AUTOMATION = {
    'ansible_config': {
        'ansible_connection': 'local'
    },
    'ping_methods': [
        AutomationMethod.ORACLE_PING
    ],
    'gather_accounts_methods': [
        AutomationMethod.GATHER_ACCOUNTS_ORACLE
    ],
    'verify_account_methods': [
        AutomationMethod.VERIFY_ACCOUNT_ORACLE
    ],
    'change_secret_methods': [
        AutomationMethod.CHANGE_SECRET_ORACLE
    ],
    'push_account_methods': [
        AutomationMethod.PUSH_ACCOUNT_ORACLE
    ]
}
SQLSERVER_AUTOMATION = {
    'ansible_config': {
        'ansible_connection': 'local'
    },
    'ping_methods': [
        AutomationMethod.SQLSERVER_PING
    ],
    'gather_accounts_methods': [],
    'verify_account_methods': [
        AutomationMethod.VERIFY_ACCOUNT_SQLSERVER
    ],
    'change_secret_methods': [
        AutomationMethod.CHANGE_SECRET_SQLSERVER
    ],
    'push_account_methods': [
        AutomationMethod.PUSH_ACCOUNT_SQLSERVER
    ]
}
MONGODB_AUTOMATION = {
    'ansible_config': {
        'ansible_connection': 'local'
    },
    'ping_methods': [
        AutomationMethod.MONGODB_PING
    ],
    'gather_accounts_methods': [
        AutomationMethod.GATHER_ACCOUNTS_MONGODB
    ],
    'verify_account_methods': [
        AutomationMethod.VERIFY_ACCOUNT_MONGODB
    ],
    'change_secret_methods': [
        AutomationMethod.CHANGE_SECRET_MONGODB
    ],
    'push_account_methods': [
        AutomationMethod.PUSH_ACCOUNT_MONGODB
    ]
}


class CommandGroupType(str, Enum):
    COMMAND = 'command'
    REGEX = 'regex'
