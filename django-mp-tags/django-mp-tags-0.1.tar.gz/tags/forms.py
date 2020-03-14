
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple

from modeltranslation.admin import TranslationStackedInline

from tags.models import Tag, TagGroup


class TagInline(TranslationStackedInline):

    model = Tag


class AddTagGroupsForm(forms.Form):

    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)

    tag_groups = forms.ModelMultipleChoiceField(
        queryset=TagGroup.objects.all(),
        widget=FilteredSelectMultiple(_('Tag groups'), True))
