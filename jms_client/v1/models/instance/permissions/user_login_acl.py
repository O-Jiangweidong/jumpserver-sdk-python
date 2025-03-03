from typing import List

from ..common import Instance


class UserLoginACLInstance(Instance):
    TYPE = 'UserLoginACL'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr name: 名称
        :attr comment: 备注
        :attr is_active: 是否激活
        :attr created_by: 创建者
        :attr date_created: 创建日期
        :attr date_updated: 更新日期
        :attr org_id: 组织 ID
        :attr priority: 优先级
        :attr reviewers: 接收人
        :attr rules: 条件
        :attr users: 受控制的用户
        """
        self.id: str = ''
        self.name: str = ''
        self.comment: str = ''
        self.is_active: bool = True
        self.created_by: str = ''
        self.date_created: str = ''
        self.date_updated: str = ''
        self.org_id: str = ''
        self.priority: int = 0
        self.reviewers: List = []
        self.rules: List = []
        self.users: List = []
        super().__init__(**kwargs)
