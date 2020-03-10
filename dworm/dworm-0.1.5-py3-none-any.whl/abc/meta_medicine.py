from dworm.abc.meta_abc import MetaBasical, MetaVerify
from django.db import models
import uuid


class MedicineBaseModel(MetaBasical):
    """基础药品信息描述 
    基础字段 不可或缺: 名规厂号剂类码功图书
    """
    REQUIRED_KEYS = ('name', 'abbreviation', 'spec', 'spec_min',
                     'preparation', 'pack_unit', 'manufacture',
                     'approval_number', 'barcode', 'ro', 'img',
                     'function', 'manual', 'brand')
    OPTIONAL_KEYS = ('storage', 'origin', 'tag')

    # mid为药品唯一ID, 名称和mid是两个唯一的非空，必填字段
    mid = models.UUIDField(verbose_name="药品ID",
                           default=uuid.uuid4, editable=False)

    name = models.CharField(verbose_name="通用名称", max_length=255, blank=False)

    abbreviation = models.CharField(
        verbose_name="首字母缩写", max_length=255, null=True, blank=True)
    spec = models.CharField(
        verbose_name="规格", max_length=255, null=True, blank=True)

    # 最小规格理论上是可计算的, 可以由spec生成
    spec_min = models.CharField(
        verbose_name="最小规格", max_length=255, null=True, blank=True)

    preparation = models.CharField(
        verbose_name="剂型", max_length=255, null=True, blank=True)
    pack_unit = models.CharField(
        verbose_name="包装单位", max_length=255, null=True, blank=True)
    manufacture = models.CharField(
        verbose_name="生产厂家", max_length=255, null=True, blank=True)
    approval_number = models.CharField(
        verbose_name="批准文号", max_length=255, null=True, blank=True)
    barcode = models.CharField(
        verbose_name="条形码", max_length=255, null=True, blank=True)
    # 处方与非处方分类
    ro = models.CharField(verbose_name="处方级别", max_length=64, default='尚不明确',
                          choices=(('处方', '处方'), ('非处方', '非处方'),
                                   ('甲类非处方', '甲类非处方'),
                                   ('乙类非处方', '乙类非处方'), ('尚不明确', '尚不明确')), null=True)
    # 药品图片多张以换行分隔
    img = models.TextField(verbose_name="图片",
                           help_text="多张图片以换行符分隔", null=True, blank=True)
    function = models.TextField(verbose_name="功能主治", null=True, blank=True)

    # 说明书存json
    manual = models.TextField(
        verbose_name="说明书", help_text="以json键值对的形式录入", null=True, blank=True)

    brand = models.CharField(
        verbose_name="品牌", max_length=255, null=True, blank=True)
    storage = models.CharField(
        verbose_name="贮藏", max_length=255, null=True, blank=True)
    origin = models.CharField(
        verbose_name="产地", max_length=255, null=True, blank=True)

    # 药品的分类标签, 用逗号分隔
    tag = models.TextField(verbose_name="标签", null=True, blank=True)

    # 商品名称字段在主题定义中已被移除!
    # 商品名称往往是 通用名称+品牌名称 的组合, 或者 奇怪的自定义名字
    prod_name = models.CharField(
        verbose_name="商品名称", max_length=255, null=True, blank=True)

    def serialization(self):
        """定义序列化实现方法
        """
        pass

    def before_save(self):
        """在保存前触发的钩子
        """
        pass

    def after_save(self):
        """在保存之后触发的钩子
        """
        pass

    def save(self):
        """重写父类的save动作，
        加入几个存储触发的钩子
        """
        self.before_save()
        super().save()
        self.after_save()

    class Meta:
        abstract = True
