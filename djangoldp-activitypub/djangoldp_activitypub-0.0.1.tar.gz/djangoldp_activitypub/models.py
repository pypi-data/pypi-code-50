import json

from django.db.models import URLField, BooleanField, BinaryField, DateField, TextField, CharField

from djangoldp.models import Model


class Follower(Model):
    aid = URLField()
    local_id = URLField()
    remote_id = URLField()
    confirmed = BooleanField(default=False)

    def to_activitystream(self):
        return {
            'type': 'Link',
            'link': self.remote_id,
        }


class Following(Model):
    aid = URLField()
    local_id = URLField()
    remote_id = URLField()
    accepted = BooleanField(default=False)

    def to_activitystream(self):
        return {
            'type': 'Link',
            'link': self.remote_id,
        }


class Activity(Model):
    aid = URLField(null=True)
    local_id = URLField()  # /inbox ou /outbox full url
    payload = BinaryField()
    created_at = DateField(auto_now_add=True)

    class Meta:
        container_path = "activities"

    def to_activitystream(self):
        payload = self.payload.decode("utf-8")
        data = json.loads(payload)
        return data


class Actor(Model):
    actor_id = URLField(unique=True)
    public_key = TextField(max_length=5000, null=True, blank=True)
    private_key = TextField(max_length=5000, null=True, blank=True)

    @property
    def private_key_id(self):
        return "{}#main-key".format(self.actor_id)
