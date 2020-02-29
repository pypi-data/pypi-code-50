from django.db import models
from django.utils.datetime_safe import date

from djangoldp.models import Model


class Skill(Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    obligatoire = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, null=True, unique=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def recent_jobs(self):
        return self.joboffer_set.filter(date__gte=date.today())

    class Meta:
        anonymous_perms = ['view']
        authenticated_perms = ['inherit', 'add']
        owner_perms = ['inherit', 'change', 'delete', 'control']
        serializer_fields = ["@id", "title", "recent_jobs"]
        lookup_field = 'slug'


class JobOffer(Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def recent_skills(self):
        return self.skills.filter(date__gte=date.today())

    class Meta:
        anonymous_perms = ['view']
        authenticated_perms = ['inherit', 'change', 'add']
        owner_perms = ['inherit', 'delete', 'control']
        nested_fields = ["skills"]
        serializer_fields = ["@id", "title", "skills", "recent_skills"]
        container_path = "job-offers/"
        lookup_field = 'slug'
