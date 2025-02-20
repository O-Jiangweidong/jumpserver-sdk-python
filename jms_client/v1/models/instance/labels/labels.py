from ..common import Instance


class LabelInstance(Instance):
    TYPE = 'Label'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr name: 名称
        :attr value: 值
        :attr comment: 备注
        :attr org_id: 组织 ID
        :attr org_name: 组织名称
        :attr date_created: 创建时间
        :attr date_updated: 创建时间
        :attr res_count: 资源关联数量
        """
        self.id: str = ''
        self.name: str = ''
        self.value: str = ''
        self.comment: str = ''
        self.org_id: str = ''
        self.org_name: str = ''
        self.date_created: str = ''
        self.date_updated: str = ''
        self.res_count: int = 0
        super().__init__(**kwargs)

    @property
    def display(self):
        return f'{self.name}:{self.value}'
