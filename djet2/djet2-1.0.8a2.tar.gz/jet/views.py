import json

from dal_select2.views import Select2QuerySetView
from django.utils.http import urlencode
from django.views.decorators.http import require_POST

from jet.forms import AddBookmarkForm, ModelLookupForm, RemoveBookmarkForm, ToggleApplicationPinForm
from jet.models import Bookmark
from jet.utils import JsonResponse


@require_POST
def add_bookmark_view(request):
    result = {'error': False}
    form = AddBookmarkForm(request, request.POST)

    if form.is_valid():
        bookmark = form.save()
        result.update({
            'id': bookmark.pk,
            'title': bookmark.title,
            'url': bookmark.url
        })
    else:
        result['error'] = True

    return JsonResponse(result)


@require_POST
def remove_bookmark_view(request):
    result = {'error': False}

    try:
        instance = Bookmark.objects.get(pk=request.POST.get('id'))
        form = RemoveBookmarkForm(request, request.POST, instance=instance)

        if form.is_valid():
            form.save()
        else:
            result['error'] = True
    except Bookmark.DoesNotExist:
        result['error'] = True

    return JsonResponse(result)


@require_POST
def toggle_application_pin_view(request):
    result = {'error': False}
    form = ToggleApplicationPinForm(request, request.POST)

    if form.is_valid():
        pinned = form.save()
        result['pinned'] = pinned
    else:
        result['error'] = True

    return JsonResponse(result)


class ModelLookupView(Select2QuerySetView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.form = None

    def get_queryset(self):
        self.form = ModelLookupForm(self.request, self.request.GET)
        if self.form.is_valid():
            return self.form.get_queryset()
        else:
            return self.form.model_cls.objects.none()

    def get_results(self, context):
        if self.form and hasattr(self.form, 'cleaned_data'):
            form = self.form
        else:
            form = ModelLookupForm(self.request, self.request.GET)
            if not form.is_valid():
                return []
        out = [
            {
                'id': self.get_result_value(obj),
                'text': self.get_result_label(obj),
            }
            for obj in context['object_list']
        ]
        lookup_kwarg = form.cleaned_data['lookup_kwarg']
        params = form.cleaned_data['lookup_params']
        if lookup_kwarg and params:
            params = json.loads(params)
            for obj in out:
                p = params.copy()
                p[lookup_kwarg] = obj['id']
                obj['url'] = '?%s' % urlencode(sorted(p.items()))
        return out


model_lookup_view = ModelLookupView.as_view()
