from functools import wraps
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from djangotools.tools import get_first_kwarg


def OnlyAuthorAccess(ModelName):
    def OnlyAuthorAccessDecorator(originalFunc):
        @wraps(originalFunc)
        def wrapper(request, *args, **kwargs):
            instance = ModelName.objects.get(slug=kwargs[get_first_kwarg(kwargs)])
            if instance.author == request.user:
                return originalFunc(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return wrapper
    return OnlyAuthorAccessDecorator
