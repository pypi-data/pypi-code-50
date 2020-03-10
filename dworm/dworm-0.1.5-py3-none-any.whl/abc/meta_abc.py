from django.db import models
import datetime


class MetaBasical(models.Model):
    data_source = models.TextField(verbose_name="数据来源", null=True,  blank=True)
    update_time = models.DateTimeField(verbose_name="数据更新时间", auto_now=True)

    class Meta:
        abstract = True


class MetaVerify(models.Model):
    AUTO_VERIFY_TAG = "自动更新程序【执行条件 完整度=1】"

    verified = models.BooleanField(
        verbose_name="已核对", default=False,  blank=True)
    verified_by = models.CharField(
        verbose_name="核对人员/方式", max_length=255, null=True,  blank=True)
    verified_time = models.DateTimeField(
        verbose_name="核对时间", auto_now_add=True, null=True,  blank=True)

    def verify(self, by: str = None, result: bool = None):
        """审核
        // TODO: 这里审核逻辑略乱，先自动审核开着，后面再仔细研究
        """
        by = by or self.AUTO_VERIFY_TAG
        if result is None:
            pass
        else:
            self.verified = result

        if not (self.verified_by and (not self.verified_by == self.AUTO_VERIFY_TAG)):
            self.verified_by = self.AUTO_VERIFY_TAG

        self.verified_time = datetime.datetime.now()

    class Meta:
        abstract = True


class MetaDA(models.Model):
    """采集库和中间库中为了评判数据质量
    """
    data_completion = models.FloatField(
        verbose_name="数据完整度", default=0, null=True,  blank=True)
    data_richness = models.FloatField(
        verbose_name="数据丰富度", default=0, null=True,  blank=True)

    class Meta:
        abstract = True


class OldMetaModel(models.Model):
    """兼容旧的采集库表
    """
    data_source = models.TextField(verbose_name="数据来源", null=True,  blank=True)
    update_time = models.DateTimeField(verbose_name="数据更新时间", auto_now=True)
    data_completion = models.FloatField(
        verbose_name="数据完整度", default=0, null=True, editable=False)

    class Meta:
        abstract = True
