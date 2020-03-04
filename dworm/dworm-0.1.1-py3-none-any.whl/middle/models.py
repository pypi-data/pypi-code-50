from dworm.middle.model import AbcMiddleMedicine


class MiddleMedicine(AbcMiddleMedicine):
    """中间库 药品表
    """
    pass

    class Meta(AbcMiddleMedicine.Meta):
        app_label = 'middle'
        db_table = 'medicine_base'
        verbose_name = "药品"
        verbose_name_plural = "药品"
