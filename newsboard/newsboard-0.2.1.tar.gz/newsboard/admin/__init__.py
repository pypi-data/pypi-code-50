from django.contrib import admin
from dj_web_rich_object.models import Tag
from newsboard.admin import modeladmins
from newsboard import models


admin.site.register(models.Stream, modeladmins.StreamAdmin)
admin.site.register(models.Post, modeladmins.PostAdmin)
admin.site.unregister(Tag)
admin.site.register(models.Tag, modeladmins.TagAdmin)
admin.site.register(models.Profile, modeladmins.ProfileAdmin)
