
from django.contrib import admin
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _

from tags.forms import AddTagGroupsForm


def add_tag_groups(modeladmin, request, queryset):

    data = request.POST

    if 'apply' in data:
        form = AddTagGroupsForm(data)

        if form.is_valid():

            tag_groups = form.cleaned_data['tag_groups']

            for instance in queryset:
                instance.tag_groups.add(*list(tag_groups))

            return redirect(request.get_full_path())
    else:
        initial = {
            '_selected_action': data.getlist(admin.ACTION_CHECKBOX_NAME)
        }
        form = AddTagGroupsForm(initial=initial)

    context = {
        'items': queryset,
        'form': form,
        'action_name': 'add_tag_groups'
    }

    return render(request, 'tags/add_tag_groups_action.html', context)

add_tag_groups.short_description = _('Add tags')
