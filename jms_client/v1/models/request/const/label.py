from enum import Enum


class ResourceType(str, Enum):
    USER = 'user'
    USER_GROUP = 'usergroup'
    ASSET = 'asset'
    DOMAIN = 'domain'
    PLATFORM = 'platform'
    PERMISSION = 'assetpermission'
    ACCOUNT = 'account'
    ACCOUNT_TEMPLATE = 'accounttemplate'
