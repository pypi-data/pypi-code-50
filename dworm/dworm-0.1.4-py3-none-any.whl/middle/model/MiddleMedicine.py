from dworm.meta import MedicineBaseModel, MEDICINE_UNIQUE_CONSTRAINTS
from django.db import models


class MiddleMedicine(MedicineBaseModel):
    """药品数据中间库
    """
    pass

    class Meta(MedicineBaseModel.Meta):
        app_label = "middle"
        db_table = "medicine_base"
        verbose_name = "基础药品数据库"
        verbose_name_plural = "基础药品数据库"
        constraints = MEDICINE_UNIQUE_CONSTRAINTS
