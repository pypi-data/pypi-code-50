from dworm.abc import MedicineBaseModel, MetaVerify
from django.db import models


class AbcTopicMedicine(MetaVerify, MedicineBaseModel):
    """药品主题数据模型
    """
    pass
    # 当主题库的数据存在问题的时候，可以将其关闭
    disable = models.BooleanField(
        verbose_name="禁用此条数据", default=False, help_text="当此条数据由于某种原因需要暂停提供时可以点击此选项")

    class Meta:
        abstract = True