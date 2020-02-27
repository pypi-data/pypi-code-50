from django.db import models


class DQA(models.Model):

    target = models.CharField(verbose_name="质量评估对象",
                              max_length=255, unique=True)
    total = models.IntegerField(verbose_name="数据总数")
    verfied_count = models.IntegerField(verbose_name="已校验/条")
    completed = models.IntegerField(verbose_name="完整度=1")
    almost_completed = models.IntegerField(verbose_name="完整度>=0.8")
    avg_completed = models.FloatField(verbose_name="平均完整度")
    riched_low = models.IntegerField(verbose_name="丰富度 >=0.5")
    riched = models.IntegerField(verbose_name="丰富度 >=0.8")
    avg_riched = models.FloatField(verbose_name="平均丰富度")
    coverage = models.FloatField(verbose_name="业务需求覆盖率")
    description = models.TextField(verbose_name="详细说明")
    update_time = models.DateTimeField(verbose_name="最后评估时间", auto_now=True)

    class Meta:
        abstract = True
