from django.db import models


class AbcDqa(models.Model):

    target = models.CharField(verbose_name="质量评估对象",
                              max_length=255, unique=True)
    total = models.IntegerField(verbose_name="数据总数", default=0)
    verfied_count = models.IntegerField(verbose_name="已校验/条", default=0)
    completed = models.IntegerField(verbose_name="完整度=1", default=0)
    almost_completed = models.IntegerField(verbose_name="完整度>=0.8", default=0)
    avg_completed = models.FloatField(verbose_name="平均完整度", default=0)
    riched_low = models.IntegerField(verbose_name="丰富度 >=0.5", default=0)
    riched = models.IntegerField(verbose_name="丰富度 >=0.8", default=0)
    avg_riched = models.FloatField(verbose_name="平均丰富度", default=0)
    coverage = models.FloatField(verbose_name="业务需求覆盖率", default=0)
    description = models.TextField(verbose_name="质量评估报告")
    update_time = models.DateTimeField(verbose_name="最后评估时间", auto_now=True)
    db = models.CharField(verbose_name="对象所在数据库", max_length=255, null=True)
    table = models.CharField(verbose_name="对象所在数据表", max_length=255, null=True)

    class Meta:
        abstract = True
