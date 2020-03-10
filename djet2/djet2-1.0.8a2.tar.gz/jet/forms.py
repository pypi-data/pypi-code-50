import logging
import operator
from functools import reduce

from django import forms
from django.apps.registry import apps
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db.models import Q

from jet.models import Bookmark, PinnedApplication
from jet.utils import user_is_authenticated


logger = logging.getLogger(__name__)


class AddBookmarkForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(AddBookmarkForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Bookmark
        fields = ['url', 'title']

    def clean(self):
        data = super(AddBookmarkForm, self).clean()
        if not user_is_authenticated(self.request.user) or not self.request.user.is_staff:
            raise ValidationError('error')
        if not self.request.user.has_perm('jet.change_bookmark'):
            raise ValidationError('error')
        return data

    def save(self, commit=True):
        self.instance.user = self.request.user.pk
        return super(AddBookmarkForm, self).save(commit)


class RemoveBookmarkForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(RemoveBookmarkForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Bookmark
        fields = []

    def clean(self):
        data = super(RemoveBookmarkForm, self).clean()
        if not user_is_authenticated(self.request.user) or not self.request.user.is_staff:
            raise ValidationError('error')
        if self.instance.user != self.request.user.pk:
            raise ValidationError('error')
        return data

    def save(self, commit=True):
        if commit:
            self.instance.delete()


class ToggleApplicationPinForm(forms.ModelForm):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(ToggleApplicationPinForm, self).__init__(*args, **kwargs)

    class Meta:
        model = PinnedApplication
        fields = ['app_label']

    def clean(self):
        data = super(ToggleApplicationPinForm, self).clean()
        if not user_is_authenticated(self.request.user) or not self.request.user.is_staff:
            raise ValidationError('error')
        return data

    def save(self, commit=True):
        if commit:
            try:
                pinned_app = PinnedApplication.objects.get(
                    app_label=self.cleaned_data['app_label'],
                    user=self.request.user.pk
                )
                pinned_app.delete()
                return False
            except PinnedApplication.DoesNotExist:
                PinnedApplication.objects.create(
                    app_label=self.cleaned_data['app_label'],
                    user=self.request.user.pk
                )
                return True


class ModelLookupForm(forms.Form):
    app_label = forms.CharField()
    model = forms.CharField()
    q = forms.CharField(required=False)
    page = forms.IntegerField(required=False)
    page_size = forms.IntegerField(required=False, min_value=1, max_value=1000)
    object_id = forms.IntegerField(required=False)
    lookup_kwarg = forms.CharField(required=False)
    lookup_params = forms.CharField(required=False)
    model_cls = None

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(ModelLookupForm, self).__init__(*args, **kwargs)

    def clean(self):
        data = super(ModelLookupForm, self).clean()

        if not user_is_authenticated(self.request.user) or not self.request.user.is_staff:
            raise ValidationError('error')

        try:
            self.model_cls = apps.get_model(data['app_label'], data['model'])
        except Exception as e:
            logger.debug(e)
            raise ValidationError('error')

        content_type = ContentType.objects.get_for_model(self.model_cls)
        permission = Permission.objects.filter(content_type=content_type, codename__startswith='change_').get()

        if not self.request.user.has_perm('{}.{}'.format(data['app_label'], permission.codename)):
            raise ValidationError('error')

        return data

    def get_queryset(self):
        qs = self.model_cls.objects.all()
        if self.cleaned_data['q']:
            if getattr(self.model_cls, 'autocomplete_search_fields', None):
                search_fields = self.model_cls.autocomplete_search_fields()
                filter_data = [Q((field + '__icontains', self.cleaned_data['q'])) for field in search_fields]
                qs = qs.filter(reduce(operator.or_, filter_data)).distinct()
            else:
                qs = qs.none()
        return qs
