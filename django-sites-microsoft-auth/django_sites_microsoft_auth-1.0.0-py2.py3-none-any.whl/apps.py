from django.apps import AppConfig


class MicrosoftAuthConfig(AppConfig):
    name = "sites_microsoft_auth"
    verbose_name = "Microsoft Auth"

    def ready(self):
        import sites_microsoft_auth.signals
