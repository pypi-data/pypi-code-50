from dworm.topic.model import AbcTopicMedicine


class TopicMedicine(AbcTopicMedicine):
    """药品主题表
    """
    pass

    class Meta(AbcTopicMedicine.Meta):
        app_label = 'topic'
        db_table = 'medicine'
        verbose_name = "药品"
        verbose_name_plural = "药品"
