from aiohttp import web
from secure_aiohttp.defaults import CSP_DEFAULT
from secure_aiohttp.utils import csp_builder
from secure_aiohttp.exceptions import CSRFtokenError



def security_middleware(xss='default'):
    """Middleware that includes handling of XSS via CSP and SCRF

    Parameters:
        xss(str/dict/None): If not specified than default CSP is enabled.
            Accepts either 'default'/'secure' as string as predifined set of CSP rules,
            or dict with custom rules. Example can be found in documentation.
            You can also pass None to deactivate xss at all.

    Returns:
        @web.middlware wrapped middleware

    """
    @web.middleware
    async def return_middleware(request, handler):
        if xss:
            # if xss - string -> looking in predifined data. Else -> this should be custom dict.
            csp_dict = CSP_DEFAULT.get(str(xss)) or xss
            csp_string = csp_builder(csp_dict)
            request.headers['Content-Security-Policy'] = csp_string

        return await handler(request)

    return return_middleware
