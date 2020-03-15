from django import forms
from dj_web_rich_object.admin import forms as wro_forms
from newsboard import models


class PostAdminForm(wro_forms.WebRichObjectAdminForm):
    class Meta(wro_forms.WebRichObjectAdminForm.Meta):
        model = models.Post


class PostAdminAddForm(wro_forms.WebRichObjectAdminAddForm):
    url = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'vLargeTextField'})
    )
    streams = forms.ModelMultipleChoiceField(
        queryset=models.Stream.objects.all(),
        required=False,
    )

    class Meta:
        model = models.Post
        fields = ('url', 'streams')

    def save_m2m(self):
        self.wro.streams.add(*self.cleaned_data['streams'])


class TagParentAdminForm(forms.ModelForm):
    parent = forms.ModelChoiceField(
        required=False,
        queryset=models.Tag.objects
            .filter(is_hidden=False)
            .order_by('name'),
    )
    action = forms.CharField(
        initial='set_parent',
        widget=forms.HiddenInput,
    )
    index = forms.CharField(
        initial='0',
        widget=forms.HiddenInput,
    )
    select_across = forms.CharField(
        initial='0',
        widget=forms.HiddenInput,
    )
    _selected_action = forms.ModelMultipleChoiceField(
        queryset=models.Tag.objects.all(),
        widget=forms.MultipleHiddenInput,
    )
    post = forms.CharField(
        initial='yes',
        widget=forms.HiddenInput,
    )

    class Meta:
        model = models.Tag
        fields = (
            'action',
            'parent',
            'index',
            'select_across',
            '_selected_action',
            'post',
        )
