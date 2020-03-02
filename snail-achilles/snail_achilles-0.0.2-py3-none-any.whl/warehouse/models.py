from django.db import models
from django.utils.translation import ugettext_lazy as _
from .utils import gen_model_file_name, model_upload_to
from ckeditor.fields import RichTextField


class Project(models.Model):
    name = models.CharField(verbose_name=_("项目名称"), max_length=255, unique=True)
    slug = models.CharField(
        verbose_name=_("slug"),
        max_length=255,
        unique=True,
        help_text="英文无空格，用以生产模型最后的URL, URL的生产规则为f'AI_{project_slug}_{model_slug}_{version}.{suffix}'"
    )
    note = RichTextField(verbose_name=_("项目备注"), blank=True)

    create_user = models.ForeignKey(
        "auth.User",
        related_name="created_projects",
        on_delete=models.SET_NULL,
        verbose_name=_("添加人"),
        help_text=_("默认为当前登录用户"),
        blank=True,
        null=True,
    )
    create_time = models.DateTimeField(_("创建时间"), auto_now_add=True)

    update_user = models.ForeignKey(
        "auth.User",
        related_name="updated_projects",
        on_delete=models.SET_NULL,
        verbose_name=_("更新人"),
        help_text=_("默认为当前登录用户"),
        blank=True,
        null=True,
    )
    update_time = models.DateTimeField(_("更新时间"), auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = verbose_name = _("项目")


class Model(models.Model):
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, verbose_name="对应项目", null=True)

    name = models.CharField(verbose_name=_("模型名称"), max_length=255, unique=True)
    slug = models.CharField(
        verbose_name=_("slug"),
        max_length=255,
        unique=True,
        help_text="英文无空格，用以生产模型最后的URL, URL的生产规则为f'AI_{project_slug}_{model_slug}_{version}.{suffix}'"
    )

    note = RichTextField(verbose_name=_("模型备注"), blank=True)

    create_user = models.ForeignKey(
        "auth.User",
        related_name="created_model_files",
        on_delete=models.SET_NULL,
        verbose_name=_("添加人"),
        help_text=_("默认为当前登录用户"),
        blank=True,
        null=True,
    )
    create_time = models.DateTimeField(_("创建时间"), auto_now_add=True)

    update_user = models.ForeignKey(
        "auth.User",
        related_name="updated_model_files",
        on_delete=models.SET_NULL,
        verbose_name=_("更新人"),
        help_text=_("默认为当前登录用户"),
        blank=True,
        null=True,
    )
    update_time = models.DateTimeField(_("更新时间"), auto_now=True)

    class Meta:
        verbose_name_plural = verbose_name = _("模型")

    def __str__(self):
        return f"{self.project.name}_{self.name}"


class ModelFile(models.Model):
    model_file = models.ForeignKey(Model, on_delete=models.CASCADE, verbose_name="对应模型文件")

    version = models.CharField(verbose_name=_("模型版本"), max_length=255)
    note = RichTextField(verbose_name=_("模型备注"), blank=True)
    suffix = models.CharField(
        verbose_name=_("模型后缀"),
        max_length=255,
        default="model",
        help_text=_("最后生成模型名称的后缀，如果遇到特殊框架需指定文件名后缀的可用。")
    )
    file = models.FileField(
        verbose_name=_("文件选择"),
        upload_to=model_upload_to,
        help_text="URL的生产规则为f'AI_{project_slug}_{model_slug}_{version}.{suffix}'"
    )

    create_user = models.ForeignKey(
        "auth.User",
        related_name="created_model_versions",
        on_delete=models.SET_NULL,
        verbose_name=_("添加人"),
        help_text=_("默认为当前登录用户"),
        blank=True,
        null=True,
    )
    create_time = models.DateTimeField(_("创建时间"), auto_now_add=True)

    update_user = models.ForeignKey(
        "auth.User",
        related_name="updated_model_versions",
        on_delete=models.SET_NULL,
        verbose_name=_("更新人"),
        help_text=_("默认为当前登录用户"),
        blank=True,
        null=True,
    )
    update_time = models.DateTimeField(_("更新时间"), auto_now=True)

    class Meta:
        verbose_name_plural = verbose_name = _("模型文件")

    def __str__(self):
        return self.version

    def gen_model_file_name(self):
        return gen_model_file_name(
            self.model_file.project.slug,
            self.model_file.slug,
            self.version,
            self.suffix
        )
