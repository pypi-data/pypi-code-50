import inspect

from ppm_telegram_bot_client import models
from ppm_telegram_bot_client.api_client import ApiClient, AsyncApis, SyncApis  # noqa F401

for model in inspect.getmembers(models, inspect.isclass):
    if model[1].__module__ == "ppm_telegram_bot_client.models":
        model_class = model[1]
        model_class.update_forward_refs()
