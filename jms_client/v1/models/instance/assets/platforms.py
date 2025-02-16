from ..common import Instance


class PlatformInstance(Instance):
    TYPE = 'Platform'

    def __init__(self,  **kwargs):
        """
        :attr id: ID
        :attr name: 名称
        :attr internal: 是否内置
        :attr type: 类型
        :attr category: 类别
        :attr charset: 编码
        :attr labels: 标签
        :attr protocols: 支持的协议
        :attr comment: 备注
        :attr create_by: 创建者
        :attr updated_by: 更新者
        :attr custom_fields: 自定义字段
        :attr domain_enabled: 是否开启网域
        :attr su_enabled: 是否支持切换用户
        :attr su_method: 切换用户方法
        :attr date_created: 创建时间
        :attr date_updated: 更新时间
        :attr automation: 自动化配置
        """
        self.id: str = ''
        self.name: str = ''
        self.comment: str = ''
        self.internal: bool = False
        self.type: dict = {}
        self.category: dict = {}
        self.charset: dict = {}
        self.labels: list = []
        self.protocols: list = []
        self.create_by: str = ''
        self.updated_by: str = ''
        self.custom_fields: dict = {}
        self.domain_enabled: bool = False
        self.su_enabled: bool = False
        self.su_method: str = ''
        self.date_created: str = ''
        self.date_updated: str = ''
        self.automation: dict = {}
        super().__init__(**kwargs)
