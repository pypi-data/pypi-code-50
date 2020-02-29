import sys

import django
from django.conf import settings

settings.configure(DEBUG=False,
                   ALLOWED_HOSTS=["*"],
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                       }
                   },
                   LDP_RDF_CONTEXT={
                       "@context": {
                           "@vocab": "http://happy-dev.fr/owl/#",
                           "foaf": "http://xmlns.com/foaf/0.1/",
                           "doap": "http://usefulinc.com/ns/doap#",
                           "ldp": "http://www.w3.org/ns/ldp#",
                           "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
                           "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
                           "xsd": "http://www.w3.org/2001/XMLSchema#",
                           "geo": "http://www.w3.org/2003/01/geo/wgs84_pos#",
                           "acl": "http://www.w3.org/ns/auth/acl#",
                           "name": "rdfs:label",
                           "website": "foaf:homepage",
                           "deadline": "xsd:dateTime",
                           "lat": "geo:lat",
                           "lng": "geo:long",
                           "jabberID": "foaf:jabberID",
                           "permissions": "acl:accessControl",
                           "mode": "acl:mode",
                           "view": "acl:Read",
                           "change": "acl:Write",
                           "add": "acl:Append",
                           "delete": "acl:Delete",
                           "control": "acl:Control"
                       }
                   },
                   AUTHENTICATION_BACKENDS=(
                       'django.contrib.auth.backends.ModelBackend', 'guardian.backends.ObjectPermissionBackend'),
                   ROOT_URLCONF='djangoldp.urls',
                   DJANGOLDP_PACKAGES=['djangoldp_activitypub.tests'],
                   MIDDLEWARE=[
                       'django.middleware.security.SecurityMiddleware',
                       'django.contrib.sessions.middleware.SessionMiddleware',
                       'django.middleware.common.CommonMiddleware',
                       'django.middleware.csrf.CsrfViewMiddleware',
                       'django.contrib.auth.middleware.AuthenticationMiddleware',
                       'django.contrib.messages.middleware.MessageMiddleware',
                       'django.middleware.clickjacking.XFrameOptionsMiddleware',
                       'djangoldp_activitypub.routing.middleware.HTTPHeaderRoutingMiddleware',
                   ],
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.admin',
                                   'guardian',
                                   'djangoldp',
                                   'djangoldp_activitypub',
                                   'djangoldp_activitypub.tests',
                                   ),
                   SITE_URL='http://happy-dev.fr',
                   BASE_URL='http://happy-dev.fr',
                   HTTP_HEADER_ROUTING_MIDDLEWARE_URLCONF_MAP={
                       'application/activity+json': 'djangoldp_activitypub.routing.urls',
                   }
                   )

django.setup()
from django.test.runner import DiscoverRunner

test_runner = DiscoverRunner(verbosity=1)

failures = test_runner.run_tests([
    'djangoldp_activitypub.tests.test_actors',
    'djangoldp_activitypub.tests.test_inbox',
    'djangoldp_activitypub.tests.test_follow',
    # 'djangoldp.tests.tests_temp'

])
if failures:
    sys.exit(failures)
