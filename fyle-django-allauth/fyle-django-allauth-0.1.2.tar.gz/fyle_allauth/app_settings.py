from django.conf import settings

# Base URL for Fyle application
BASE_URL = getattr(settings, 'FYLE_BASE_URL', 'https://app.fyle.in')
