

class Settings:
    DEBUG = True
    CONSOLE_LOG_LEVEL = 'LOG'
    USE_LOGURU = True


local_settings = Settings()


# Support Django settings
try:
    from django.conf import settings
except Exception:
    settings = local_settings  # type: ignore
else:
    # Django might be installed, but django settings module might not be set
    try:
        log_level = settings.CONSOLE_LOG_LEVEL
    except Exception:
        settings = local_settings  # type: ignore
