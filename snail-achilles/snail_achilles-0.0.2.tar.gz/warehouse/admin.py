from django.contrib import admin
from .models import Project, Model, ModelFile


class ModelInline(admin.StackedInline):
    model = Model
    extra = 1


class ModelFileInline(admin.StackedInline):
    model = ModelFile
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_per_page = 100

    list_display = (
        "id",
        "name",
        "slug",
        "create_user",
        "create_time",
        "update_user",
        "update_time",
    )

    list_filter = (
        "create_user",
        "create_time",
        "update_time",
    )

    inlines = (ModelInline,)


class ModelAdmin(admin.ModelAdmin):
    list_per_page = 100

    list_display = (
        "id",
        "name",
        "slug",
        "create_user",
        "create_time",
        "update_user",
        "update_time",
    )

    list_filter = (
        "project",
        "create_user",
        "create_time",
        "update_time",
    )
    inlines = (ModelFileInline,)


class ModelFileAdmin(admin.ModelAdmin):
    list_per_page = 100

    list_display = (
        "id",
        "model_file",
        "version",
        "create_user",
        "create_time",
        "update_user",
        "update_time",
    )

    list_filter = (
        "model_file__project",
        "model_file",
        "suffix",
        "create_user",
        "create_time",
        "update_time",
    )


admin.site.site_header = "Achilles"
admin.site.site_title = "Achilles"

admin.site.register(Project, ProjectAdmin)

admin.site.register(Model, ModelAdmin)

admin.site.register(ModelFile, ModelFileAdmin)
