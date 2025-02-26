from ..common import Instance


class ActivityInstance(Instance):
    TYPE = 'Activity'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr content: 日志内容
        :attr detail_url: 操作日志对应地址
        :attr r_type: 日志来源类型（O -> 操作日志、S -> 会话日志、L -> 登陆日志、T -> 任务日志）
        :attr timestamp: 时间
        """
        self.id: str = ''
        self.content: str = ''
        self.detail_url: str = ''
        self.r_type: str = ''
        self.timestamp: str = ''
        super().__init__(**kwargs)

    @property
    def display(self):
        return self.content
