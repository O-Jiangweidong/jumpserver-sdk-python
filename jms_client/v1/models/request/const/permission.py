from enum import Enum


class ACLAction(str, Enum):
    REJECT = 'reject'
    ACCEPT = 'accept'
    REVIEW = 'review'
    NOTICE = 'notice'
