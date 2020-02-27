from datetime import timedelta
import re
from django.conf import settings

from django.core import signing
from django.core.signing import TimestampSigner
from django.http import HttpResponse, HttpResponseNotFound

from .models import FeatureOption
from django.core.cache import cache


class TesterMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

        # One-time configuration and initialization.
        # raise MiddlewareNotUsed

    def __call__(self, request):

        # Code to be executed for each request before
        # the view (and later middleware) are called.

        signer = TimestampSigner()
        request.session['features'] = []
        if not request.path.startswith('/admin/'):

            fo = cache.get('featureoptions')

            if fo is None:
                fo = [{'name': f.name, 'urls_re': [re.compile(u.regex) for u in f.urls.all()]}
                      for f in FeatureOption.objects.filter(active=True).all()]
                cache.set('featureoptions', fo, 3600)
                print(fo)

            if settings.PRIVATE_URL_RE:
                fo.append({'name': 'site-settings', 'urls_re': [settings.PRIVATE_URL_RE]})

            for f in fo:
                block = True
                if f['name'] in request.COOKIES:
                    value = request.COOKIES[f['name']]
                    try:
                        value = signer.unsign(value, max_age=timedelta(days=2))
                        block = False
                        request.session['features'].append(f['name'])
                    except signing.BadSignature:
                        block = True

                if 'staff' in request.COOKIES:
                    try:
                        signer.unsign(
                            request.COOKIES['staff'], max_age=timedelta(days=2))
                        block = False
                    except signing.BadSignature:
                        block = True

                if block and not request.user.is_staff:
                    for u in f['urls_re']:
                        if u.match(request.path):
                            return HttpResponseNotFound(f'<h1>Not Found {request.path}</h1>')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        if hasattr(request, 'user') and request.user.is_staff:
            response.set_cookie('staff', signer.sign('staff'), max_age=72000)

        return response
