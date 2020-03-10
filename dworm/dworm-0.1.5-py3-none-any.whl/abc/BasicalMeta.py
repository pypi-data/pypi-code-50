from django.db import models


class OldMetaModel(models.Model):
    """兼容旧的表
    """
    data_source = models.TextField(verbose_name="数据来源", null=True, blank=True)
    download_time = models.DateTimeField(verbose_name="数据更新时间", auto_now=True)
    data_completion = models.FloatField(
        verbose_name="数据完整度", default=0, null=True, editable=False)

    class Meta:
        abstract = True


class BaseMetaModel(models.Model):
    """基础元数据描述
    """
    data_source = models.TextField(verbose_name="数据来源", null=True,  blank=True)
    update_time = models.DateTimeField(verbose_name="数据更新时间", auto_now=True)
    data_completion = models.FloatField(
        verbose_name="数据完整度", default=0, null=True,  blank=True)
    data_richness = models.FloatField(
        verbose_name="数据丰富度", default=0, null=True,  blank=True)
    verified = models.BooleanField(
        verbose_name="已核对", default=False,  blank=True)
    verified_by = models.CharField(
        verbose_name="核对人员", max_length=10, null=True,  blank=True)
    verified_time = models.DateTimeField(
        verbose_name="核对时间", auto_now=True, null=True,  blank=True)

    class Meta:
        abstract = True
