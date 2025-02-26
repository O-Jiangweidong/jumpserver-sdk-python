from jms_client.v1.models.instance.audits import ActivityInstance
from ..common import Request


class DescribeResourceActivitiesRequest(Request):
    """ 获取指定资源的活动记录，30 条 """
    URL = 'audits/activities/'
    InstanceClass = ActivityInstance

    def __init__(
            self,
            resource_id: str = '',
            **kwargs
    ):
        """
        :param resource_id: 资源 ID
        :param kwargs: 其他参数
        """
        super().__init__(resource_id=resource_id, **kwargs)
