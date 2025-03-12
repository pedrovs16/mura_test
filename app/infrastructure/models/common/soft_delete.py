from datetime import datetime

from sqlalchemy_easy_softdelete.mixin import generate_soft_delete_mixin_class


class SoftDeleteMixin(generate_soft_delete_mixin_class()):
    """
    allows models to have a soft delete with an auto generated deleted_at property with
    a delete() and undelete() method
    """

    deleted_at: datetime
