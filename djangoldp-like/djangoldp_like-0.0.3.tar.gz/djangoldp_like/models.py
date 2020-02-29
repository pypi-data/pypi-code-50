from django.db import models
from djangoldp.fields import IdURLField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.utils import timezone

class Like(models.Model):
    sender = IdURLField(max_length=300)
    receiver_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    receiver_object_id = models.PositiveIntegerField()
    receiver = GenericForeignKey(
        ct_field="receiver_content_type",
        fk_field="receiver_object_id"
    )
    timestamp = models.DateTimeField(default=timezone.now)

    # Please refer to Django documentation
    class Meta:
        serializer_fields = ['sender']
        container_path = 'likes/'
        rdf_type = 'coopstarter:like'
      
        anonymous_perms = ['view']
        authenticated_perms = ['inherit', 'add']
        owner_perms = ['inherit', 'change', 'control', 'delete']
        # unique_together = ['sender', 'receiver_content_type', 'receiver_object_id']

    def __str__(self):
        return self.sender