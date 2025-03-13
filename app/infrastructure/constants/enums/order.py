from enum import Enum


class OrderStatusEnum(Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELED = "Canceled"


class OrderSourceEnum(Enum):
    EMAIL = "Email"
    PHONE = "Phone"
    WEBSITE = "Website"
    MOBILE_APP = "Mobile App"
    OTHER = "Other"
