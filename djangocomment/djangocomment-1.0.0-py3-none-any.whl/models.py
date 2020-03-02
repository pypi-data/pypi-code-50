from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from djangocomment.managers import CommentModelManager


# Create your comment models here.
class CommentModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    content = models.TextField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    objects = CommentModelManager()

    def __str__(self):
        return f"App Name: {self.content_type} - Object ID: {self.object_id} - Author Name: {self.author}"
