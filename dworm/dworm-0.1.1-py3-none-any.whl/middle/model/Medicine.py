from dworm.abc import MedicineBaseModel, MEDICINE_UNIQUE_CONSTRAINTS
from django.db import models


class AbcMiddleMedicine(MedicineBaseModel):
    """药品数据中间库
    """

    erratum = models.TextField(verbose_name="勘误反馈", blank=True, null=True)

    class Meta(MedicineBaseModel.Meta):
        abstract = True
        # app_label = "middle"
        # db_table = "medicine_base"
        # verbose_name = "基础药品数据库"
        # verbose_name_plural = "基础药品数据库"
        constraints = MEDICINE_UNIQUE_CONSTRAINTS
