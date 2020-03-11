from typing import Union, List

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import View


class CacheTemplateTableItems(View):
    """
    View for caching table item choices to session.
    """

    separator: str = ','

    def post(self, request, *args, **kwargs):
        key, value_to_add = self.get_kwargs()
        exist_values = self.request.session.get(key)

        new_value = [value_to_add]
        if exist_values:
            exist_values = exist_values.split(self.separator)
            if value_to_add in exist_values:
                exist_values.remove(value_to_add)
                new_value = exist_values
            else:
                new_value += exist_values

        self.request.session[key] = self.separator.join(new_value)

        return self.get_response()

    def get_response(self) -> Union[HttpResponse, JsonResponse]:
        return HttpResponse('OK', status=200)

    def get_kwargs(self) -> tuple:
        return self.kwargs.get('key'), self.kwargs.get('value')


class FlushTemplateTableSelection(View):
    """
    View for flushing cached table item choices.
    """

    keys: List[str] = []
    success_url: str = ''

    def post(self, request, *args, **kwargs):
        for key in self.keys:
            self.request.session.pop(key, None)

        return self.get_response()

    def get_success_url(self) -> str:
        return self.success_url

    def get_response(self) -> Union[HttpResponse, JsonResponse]:
        return HttpResponseRedirect(self.get_success_url())
