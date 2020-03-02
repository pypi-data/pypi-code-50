CSP_DEFAULT = {
    'default': {
        'block-all-mixed-content': None
        'connect-src': 'self'
        'default-src': 'none'
        'img-src': 'self'
        'script-src': 'self'
        'style-src': 'self'
    }
}

"""
XSS CSP examples:

unsafe:

script-src 'unsafe-inline' 'unsafe-eval' 'self' data: https://www.google.com http://www.google-analytics.com/gtm/js  https://*.gstatic.com/feedback/ https://ajax.googleapis.com;
style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://www.google.com;
default-src 'self' * 127.0.0.1 https://[2a00:79e0:1b:2:b466:5fd9:dc72:f00e]/foobar;
img-src https: data:;
child-src data:;
foobar-src 'foobar';
report-uri http://csp.example.com;

safe:

script-src 'strict-dynamic' 'nonce-rAnd0m123' 'unsafe-inline' http: https:;
object-src 'none';
base-uri 'none';
require-trusted-types-for 'script';
report-uri https://csp.example.com;


"""
