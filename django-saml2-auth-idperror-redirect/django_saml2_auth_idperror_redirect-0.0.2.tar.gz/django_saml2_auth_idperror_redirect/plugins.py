from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from django_saml2_auth.plugins import IdpErrorPlugin


class RedirectSignoutHandler(IdpErrorPlugin):
    KEY = 'REDIRECT'

    @classmethod
    def error(cls, request, reason=None):
        """Logs the user out of the local system and redirects them to the REDIRECT URL in the SAML Metadata"""
        url = settings.SAML2_AUTH.get('IDP_ERROR_REDIRECT_URL')
        if url is None:
            view = settings.SAML2_AUTH.get('IDP_ERROR_REDIRECT_VIEW')
            if view is not None:
                url = reverse(view)
        if url is None:
            raise ValueError("Must provide valid IDP_ERROR_REDIRECT_VIEW or IDP_ERROR_REDIRECT_URL")
        if settings.SAML2_AUTH.get('IDP_ERROR_REDIRECT_NEXT') is True:
            url = '{}{}{}'.format(
                url,
                '&' if '?' in url else '?',
                'next={}'.format(request.path),
            )
        return HttpResponseRedirect(url)
