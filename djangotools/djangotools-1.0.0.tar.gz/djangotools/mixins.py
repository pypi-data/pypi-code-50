from django.core.exceptions import PermissionDenied
from djangotools.tools import get_first_kwarg


class OnlyAuthorAccess(object):
    def dispatch(self, request, *args, **kwargs):
        ModelName = self.model        
        instance = ModelName.objects.get(slug=kwargs[get_first_kwarg(kwargs)])
        if instance.author == request.user:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied
