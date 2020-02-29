import threading

from django.conf import settings

from djangoldp.models import Model
from djangoldp_activitypub import models
from djangoldp_activitypub.security import signing, keys
from .objects import *
from .verbs import *


class AP(object):

    @classmethod
    def uri(self, name, *args):
        domain = settings.BASE_URL
        return "{domain}/{name}/".format(domain=domain, name=name.strip('/'))

    @classmethod
    def create_activity(cls, activity):
        """
        Send an activity to the outbox
        :param activity: AP.Note() or custom object
        :param actor: ex: https://localhpst/users/2/
        :return:
        """
        actor = activity['actor']
        local_actor = AP.get_actor(actor)
        auth = signing.get_auth(local_actor.private_key, local_actor.private_key_id)
        obj = cls.dereference(actor)
        if not getattr(obj, "outbox", None):
            # XXX: log this
            return
        t = threading.Thread(target=cls.doOutboxPost, args=[obj.outbox, activity, auth])
        t.start()

    @classmethod
    def doOutboxPost(cls, outbox, activity, auth):
        response = requests.post(outbox,
                                 json=activity,
                                 headers={'Accept': 'application/activity+json',
                                          'Content-type': "application/activity+json"},
                                 auth=auth)
        return response

    @classmethod
    def note(cls, actor, instance):
        local_id = cls.uri(Model.resource(actor))
        id = cls.uri(Model.resource(instance))
        return {
            "@context": "https://www.w3.org/ns/activitystreams",
            "id": id,
            "type": "Note",
            "actor": local_id,
            "content": instance.content()
        }

    @classmethod
    def accept(cls, follower):
        remote_actor = cls.dereference(follower.remote_id)
        local_actor = AP.get_actor(follower.local_id)
        auth = signing.get_auth(local_actor.private_key, local_actor.private_key_id)

        response = requests.post(remote_actor.inbox,
                                 json={"@context": "https://www.w3.org/ns/activitystreams",
                                       "type": "Accept",
                                       "id": "https://social.lemee.co/@jb#undo/stuff/4",
                                       "actor": follower.local_id,
                                       "object": {
                                           "id": follower.aid,
                                           "type": "Follow",
                                           "actor": follower.remote_id,
                                           "object": follower.local_id,
                                       }},
                                 headers={'Accept': 'application/activity+json',
                                          'Content-type': "application/activity+json"},
                                 auth=auth)

        if response.ok:
            follower.confirmed = True
            follower.save()

    @classmethod
    def get_actor(cls, actor_id):
        if not models.Actor.objects.filter(actor_id=actor_id).exists():
            private_key, public_key = keys.get_key_pair(2048)
            models.Actor.objects.create(actor_id=actor_id, public_key=public_key, private_key=private_key)

        return models.Actor.objects.get(actor_id=actor_id)

    @classmethod
    def dereference(cls, ap_id):
        res = requests.get(ap_id, headers={'Accept': 'application/activity+json'})
        if res.status_code != 200:
            raise Exception("Failed to dereference {0}".format(ap_id))

        return as_activitystream(json.loads(res.content))

    @classmethod
    def deliver(cls, activity):
        audience = activity.get_audience()
        activity = activity.strip_audience()
        audience = cls.get_final_audience(audience)
        for ap_id in audience:
            cls.deliver_to(ap_id, activity)

    @classmethod
    def deliver_to(cls, ap_id, activity):
        obj = cls.dereference(ap_id)
        if not getattr(obj, "inbox", None):
            # XXX: log this
            return
        local_actor = AP.get_actor(activity.actor)

        auth = signing.get_auth(local_actor.private_key, local_actor.private_key_id)

        res = requests.post(obj.inbox, json=activity.to_json(context=True),
                            headers={'Accept': 'application/activity+json',
                                     'Content-type': "application/activity+json"}, auth=auth)
        if res.status_code != 200:
            msg = "Failed to deliver activity {0} to {1}"
            msg = msg.format(activity.type, obj.inbox)
            raise Exception(msg)

    @classmethod
    def get_final_audience(cls, audience):
        final_audience = []
        for ap_id in audience:
            obj = cls.dereference(ap_id)
            if isinstance(obj, Collection):
                for item in obj.items:
                    if hasattr(item, 'id'):
                        final_audience.append(item.id)
                    elif isinstance(item, str):
                        final_audience.append(item)
            elif isinstance(obj, Actor):
                final_audience.append(obj.id)
        return set(final_audience)
