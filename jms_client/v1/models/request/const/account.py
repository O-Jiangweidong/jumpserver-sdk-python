from enum import Enum


class SecretType(str, Enum):
    PASSWORD = 'password'
    SSH_KET = 'ssh_key'
    ACCESS_KEY = 'access_key'
    TOKEN = 'token'
    API_KEY = 'api_key'


class Source(str, Enum):
    LOCAL = 'local'
    COLLECTED = 'collected'
    TEMPLATE = 'template'


class OnInvalidType(str, Enum):
    SKIP = 'skip'
    UPDATE = 'update'
    ERROR = 'error'
