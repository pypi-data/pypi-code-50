from dworm.abc import MedicineBaseModel, MetaVerify, MetaDA
from django.db import models


class AbcMiddleMedicine(MetaVerify, MetaDA, MedicineBaseModel):
    """中间库药品数据模型
    """

    # 加入一个勘误的字段
    erratum = models.TextField(verbose_name="勘误反馈", blank=True, null=True)

    class Meta(MedicineBaseModel.Meta):
        abstract = True

    def compute_completion(self):
        """计算基础信息完整度及丰富度
        """
        # 计算数据完整度
        empty_key = 0
        for key in self.REQUIRED_KEYS:
            value = self.__dict__.get(key, None)
            if not value:
                empty_key += 1

        completion = 1 - empty_key/len(self.REQUIRED_KEYS)

        self.data_completion = round(completion, 2)

        if self.data_completion == 1:
            self.verify(None, True)

        else:
            self.verify(None, False)

        # 计算数据丰富度
        empty_option = 0
        for option in self.OPTIONAL_KEYS:
            value = self.__dict__.get(option, None)
            if not value:
                empty_option += 1

        richness = 1 - empty_option/len(self.OPTIONAL_KEYS)

        self.data_richness = round(richness, 2)
