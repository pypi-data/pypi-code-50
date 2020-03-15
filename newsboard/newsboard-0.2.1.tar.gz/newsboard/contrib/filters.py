from django import forms
from django.db import models as dj_models

import django_filters
from django_filters import views as filters_views

from newsboard import views
from newsboard import models

STREAMS = models.Stream.objects\
    .order_by('name')
TAGS = models.Tag.objects\
    .exclude(is_hidden=True)\
    .order_by('name')


class PostFilterSet(django_filters.FilterSet):
    streams = django_filters.filters.ModelMultipleChoiceFilter(
        field_name='streams__name',
        to_field_name='name',
        queryset=STREAMS,
        widget=forms.SelectMultiple(
            attrs={
                'data-width': '40%',
                'data-height': '30px',
                'data-placeholder': 'Select stream(s)',
            }
        )
    )
    tags = django_filters.filters.ModelMultipleChoiceFilter(
        method='filter_tags',
        queryset=TAGS,
        widget=forms.SelectMultiple(
            attrs={
                'data-width': '40%',
                'data-height': '30px',
                'data-placeholder': 'Select tag(s)',
            }
        )
    )

    class Meta:
        model = models.Post
        fields = ['streams', 'tags']

    def filter_tags(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(
            dj_models.Q(tags__in=value) | dj_models.Q(tags__parent__in=value)
        )


class PostFilterView(views.PostListMixin, filters_views.FilterView):
    filterset_class = PostFilterSet
