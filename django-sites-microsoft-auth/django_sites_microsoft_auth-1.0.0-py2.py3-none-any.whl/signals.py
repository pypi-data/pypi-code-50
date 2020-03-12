from django.contrib.sites.models import Site
from django.db.models.signals import post_save
from django.dispatch import receiver

from sites_microsoft_auth.models import SiteConfiguration


@receiver(post_save, sender=Site)
def create_site_config(sender, instance, **kwargs):
    SiteConfiguration.objects.get_or_create(site=instance)
