from typing import List

from ..common import Instance


class UserGroupInstance(Instance):
    TYPE = 'UserGroup'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr name: 名称
        :attr comment: 备注
        :attr org_id: 组织 ID
        :attr org_name: 组织名称
        :attr created_by: 创建者
        :attr date_created: 创建时间
        :attr labels: 标签
        :attr users_amount: 关联的用户数量
        """
        self.id: str = ''
        self.name: str = ''
        self.comment: str = ''
        self.org_id: str = ''
        self.org_name: str = ''
        self.created_by: str = ''
        self.date_created: str = ''
        self.labels: List = []
        self.users_amount: int = 0
        super().__init__(**kwargs)
