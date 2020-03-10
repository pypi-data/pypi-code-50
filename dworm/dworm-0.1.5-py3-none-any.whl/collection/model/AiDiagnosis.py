from django.db import models
from dworm.abc import OldMetaModel as BaseMetaModel


class AbcAidDiseases(BaseMetaModel):
    """智能问诊涉及到的疾病
    """
    symptom = models.TextField(verbose_name="疾病症状", null=True)

    class Meta:
        abstract = True
        constraints = (models.UniqueConstraint(
            fields=["symptom"], name="aid_diseases_unique"),)


class AbcAidCheck(BaseMetaModel):
    """智能问诊涉及到的检查项
    """
    name = models.CharField(
        verbose_name="检查项名称", max_length=255, null=True)

    class Meta:
        abstract = True
        constraints = (models.UniqueConstraint(
            fields=["name"], name="aid_check_unique"),)


class AbcAidMedRequired(BaseMetaModel):
    """智能问诊需要的药品
    """
    name = models.CharField(verbose_name="药品名称", max_length=255, null=True)
    related_id = models.TextField(verbose_name="相关药品ID", null=True)

    class Meta:
        abstract = True
        constraints = (models.UniqueConstraint(
            fields=["name"], name="aid_medicine_required_unique"),)


class AbcAidPrescription(BaseMetaModel):
    """智能问诊诊断书
    """
    symptom = models.CharField(verbose_name="疾病症状", max_length=255, null=True)
    check = models.CharField(
        verbose_name="辅助检查项", max_length=255, null=True)
    medicines = models.TextField(verbose_name="治疗药品", null=True)

    class Meta:
        abstract = True
        constraints = (models.UniqueConstraint(
            fields=["symptom"], name="aid_prescription_unique"), )
