from enum import Enum


class UserLoginACLAction(str, Enum):
    REJECT = 'reject'
    ACCEPT = 'accept'
    REVIEW = 'review'
    NOTICE = 'notice'


UserLoginACLAction(UserLoginACLAction.REJECT)
