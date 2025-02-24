from jms_client.v1.models.instance.assets import PlatformInstance
from ..const import (
    PlatformType, SuMethod, AutomationMethod,
    LINUX_AUTOMATION, WINDOWS_AUTOMATION, UNIX_AUTOMATION,
    GENERAL_AUTOMATION, SWITCH_AUTOMATION, ROUTER_AUTOMATION,
    FIREWALL_AUTOMATION, MYSQL_AUTOMATION, MARIADB_AUTOMATION,
    POSTGRESQL_AUTOMATION, ORACLE_AUTOMATION, SQLSERVER_AUTOMATION,
    MONGODB_AUTOMATION,
)
from ..common import Request, ProtocolParam
from ..mixins import (
    ExtraRequestMixin, WithIDMixin, CreateMixin,
    UpdateMixin, DeleteMixin,
)


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


class DetailPlatformRequest(WithIDMixin, BasePlatformRequest):
    """
    获取平台详情
    """


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
    CreateUpdatePlatformParamsMixin, UpdateMixin, BasePlatformRequest
):
    """ 更新 网域 """


class DeletePlatformRequest(DeleteMixin, BasePlatformRequest):
    """ 删除指定 ID 的平台 """
