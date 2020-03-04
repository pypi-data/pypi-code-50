from dworm.board.model import AbcDqa


class DqaModel(AbcDqa):


    class Meta(AbcDqa.Meta):
        app_label = "board"
        db_table = "dqa"
        verbose_name = "数据质量评估"
        verbose_name_plural = "数据质量评估"
