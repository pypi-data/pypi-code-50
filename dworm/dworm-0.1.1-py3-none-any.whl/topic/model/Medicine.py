from dworm.abc import MedicineBaseModel
from django.db import models


class AbcTopicMedicine(MedicineBaseModel):
    """药品主题数据模型
    """
    pass
    # 当主题库的数据存在问题的时候，可以将其关闭
    disable = models.BooleanField(verbose_name="是否禁用", default=False)

    class Meta:
        abstract = True
