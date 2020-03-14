
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from tags.models import TagGroup
from tags.forms import TagInline


@admin.register(TagGroup)
class TagGroupAdmin(admin.ModelAdmin):

    list_per_page = 100
    list_display = ['name', 'tags_count_tag']
    search_fields = ['name']
    inlines = [TagInline]

    def tags_count_tag(self, obj):
        return obj.tags.count()

    tags_count_tag.short_description = _('Tags count')
