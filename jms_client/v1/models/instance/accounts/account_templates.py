from typing import List

from ..common import Instance


class AccountTemplateInstance(Instance):
    TYPE = 'AccountTemplate'

    def __init__(self, **kwargs):
        """
        :attr id: ID
        :attr name: 名称
        :attr username: 用户名
        :attr comment: 备注
        :attr auto_push: 是否自动推送
        :attr privileged: 特权账号
        :attr password_rules: 密码规则
        :attr platforms: 平台列表
        :attr push_params: 推送参数
        :attr secret_strategy: 密码策略
        :attr secret_type: 密码类型
        :attr is_active: 是否激活
        :attr created_by: 创建者
        :attr date_created: 创建日期
        :attr data_updated: 更新日期
        :attr org_id: 组织 ID
        :attr org_name: 组织名称
        :attr labels: 标签
        :attr su_from: 切换自（从其他账号切换到该账号下）
        """
        self.id: str = ''
        self.name: str = ''
        self.username: str = ''
        self.comment: str = ''
        self.auto_push: bool = False
        self.privileged: bool = False
        self.password_rules: dict = {}
        self.platforms: List = []
        self.push_params: dict = {}
        self.secret_strategy: dict = {}
        self.secret_type: dict = {}
        self.is_active: bool = True
        self.created_by: str = ''
        self.date_created: str = ''
        self.data_updated: str = ''
        self.org_id: str = ''
        self.org_name: str = ''
        self.labels: List = []
        self.su_from: str = ''
        super().__init__(**kwargs)

    @property
    def display(self):
        return f'{self.name}({self.username})'
