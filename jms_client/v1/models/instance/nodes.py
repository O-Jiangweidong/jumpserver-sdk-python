from .common import Instance


class NodeInstance(Instance):
    TYPE = 'Node'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr name:名称
        :attr key: 键
        :attr value: 节点名称
        :attr full_value: 全量节点名称
        :attr org_id: 组织 ID
        :attr org_name: 组织名称
        """
        self.id: str = ''
        self.name: str = ''
        self.key: str = ''
        self.value: str = ''
        self.full_value: str = ''
        self.org_id: str = ''
        self.org_name: str = ''
        super().__init__(**kwargs)
