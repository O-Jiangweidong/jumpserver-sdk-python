from enum import Enum


class Source(str, Enum):
    LOCAL = 'local'
    LDAP = 'ldap'
    LDAP_HA = 'ldap_ha'
    OPENID = 'openid'
    RADIUS = 'radius'
    CAS = 'cas'
    SAML2 = 'saml2'
    OAUTH2 = 'oauth2'
    WECOM = 'wecom'
    DINGTALK = 'dingtalk'
    FEISHU = 'feishu'
    LARK = 'lark'
    SLACK = 'slack'
    CUSTOM = 'custom'

    def __str__(self) -> str:
        return self.value


class MFALevel(str, Enum):
    DISABLED = '0'
    ENABLED = '1'
    FORCE_ENABLED = '2'

    def __str__(self) -> str:
        return self.value
