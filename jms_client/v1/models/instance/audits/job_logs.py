from ..common import Instance


class JobLogInstance(Instance):
    TYPE = 'JobLog'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr creator_name: 创建者
        :attr date_created: 创建时间
        :attr date_start: 开始时间
        :attr date_finished: 完成时间
        :attr is_finished: 是否完成
        :attr is_success: 是否成功
        :attr job_type: 作业类型
        :attr material: 作业内容
        :attr org_id: 组织 ID
        :attr org_name: 组织名称
        :attr task_id: 任务 ID
        :attr time_cost: 任务耗时
        """
        self.id: str = ''
        self.creator_name: str = ''
        self.date_created: str = ''
        self.date_start: str = ''
        self.date_finished: str = ''
        self.is_finished: bool = False
        self.is_success: bool = False
        self.job_type: str = ''
        self.material: str = ''
        self.org_id: str = ''
        self.org_name: str = ''
        self.task_id: str = ''
        self.time_cost: float = 0.0
        super().__init__(**kwargs)

    @property
    def display(self):
        return f'{self.material}({self.creator_name})'
