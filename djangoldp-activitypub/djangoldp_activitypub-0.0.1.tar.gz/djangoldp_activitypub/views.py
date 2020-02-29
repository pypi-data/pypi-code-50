import json

from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import GenericViewSet

from djangoldp.models import Model
from djangoldp.views import NoCSRFAuthentication
from djangoldp_activitypub import activities
from djangoldp_activitypub.activities import as_activitystream, AP
from djangoldp_activitypub.activities.errors import ASDecodeError
from djangoldp_activitypub.models import Following, Follower, Activity


def noop(*args, **kwargs):
    pass


class ActivityPubRenderer(JSONRenderer):
    media_type = 'application/activity+json'


class ActivityPubView(GenericViewSet):
    renderer_classes = [ActivityPubRenderer]
    authentication_classes = (NoCSRFAuthentication,)

    def uri(self, name, *args):
        domain = settings.BASE_URL
        return "{domain}/{name}/".format(domain=domain, name=name.strip('/'))

    def dispatch(self, request, *args, **kwargs):
        response = super(GenericViewSet, self).dispatch(request, *args, **kwargs)
        return response

    def is_container(self, **kwargs):
        container = kwargs['container']
        model, id = Model.resolve(container)
        return 'id' not in kwargs

    def get_actor_or_404(self, **kwargs):
        container = kwargs['container']
        model, id = Model.resolve(container)
        id = kwargs['id']
        args = {Model.slug_field(model): id}
        return get_object_or_404(model, **args)

    def get_actor_id_or_404(self, **kwargs):
        if self.is_container(**kwargs):
            return self.uri(kwargs['container'])
        else:
            actor = self.get_actor_or_404(**kwargs)
            return self.__actor_id__(actor)

    def __actor_id__(self, actor):
        return "{base_url}{path}".format(base_url=settings.BASE_URL, path=Model.resource_id(actor))


class ActorView(ActivityPubView):

    def get(self, request, **kwargs):
        container = kwargs['container']

        if not self.is_container(**kwargs):
            id = kwargs['id']
            actor = self.get_actor_or_404(**kwargs)

            if isinstance(actor, get_user_model()):
                json = activities.Person(
                    **self.to_activity_stream("{}/{}".format(container, id), actor.__str__(),
                                              actor.__str__())).to_json(context=True)
            else:
                json = activities.Group(
                    **self.to_activity_stream("{}/{}".format(container, id), actor.__str__(),
                                              actor.__str__())).to_json(context=True)
        else:
            json = activities.Service(**self.to_activity_stream(container, container, container)).to_json(
                context=True)

        return JsonResponse(json)

    def to_activity_stream(self, container, name, preferredUsername):
        actor_id = self.uri(container)
        actor = AP.get_actor(actor_id)
        activity = {
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                "https://w3id.org/security/v1",
            ],
            "id": actor.actor_id,
            "name": name,
            "preferredUsername": preferredUsername,
            "following": self.uri("{}/{}".format(container, "following")),
            "followers": self.uri("{}/{}".format(container, "followers")),
            "outbox": self.uri("{}/{}".format(container, "outbox")),
            "inbox": self.uri("{}/{}".format(container, "inbox")),
            "publicKey": {
                "id": actor.private_key_id,
                "owner": actor.actor_id,
                "publicKeyPem": actor.public_key,
            },
        }
        return activity


class FollowingView(ActivityPubView):

    def list(self, request, **kwargs):
        return JsonResponse(activities.OrderedCollection(
            Following.objects.filter(
                local_id=self.get_actor_id_or_404(**kwargs),
                accepted=True).all()).to_json(context=True))


class FollowersView(ActivityPubView):

    def list(self, request, **kwargs):
        return JsonResponse(activities.OrderedCollection(
            Follower.objects.filter(
                local_id=self.get_actor_id_or_404(**kwargs),
                confirmed=True).all()).to_json(context=True))


class InboxView(ActivityPubView):
    '''
    You can POST to someone's inbox to send them a message (server-to-server / federation only... this is federation!)
    You can GET from your inbox to read your latest messages (client-to-server; this is like reading your social network stream)
    '''

    def list(self, request, **kwargs):
        local_id = "{}inbox/".format(self.get_actor_id_or_404(**kwargs))
        objects = Activity.objects.filter(
            local_id=local_id).order_by('-created_at').all()
        collection = activities.OrderedCollection(objects)
        return JsonResponse(collection.to_json(context=True))

    def post(self, request, **kwargs):
        local_id = "{}inbox/".format(self.get_actor_id_or_404(**kwargs))

        payload = request.body.decode("utf-8")
        try:
            activity = json.loads(payload, object_hook=as_activitystream)
            activity.validate()
        except ASDecodeError:
            return HttpResponseNotAllowed()

        if activity.type == "Follow":
            self.handle_follow(activity, **kwargs)
        if activity.type == "Undo":
            self.handle_undo(activity, **kwargs)

        payload = bytes(json.dumps(activity.to_json()), "utf-8")
        obj = Activity.objects.create(local_id=local_id, payload=payload)
        obj.aid = self.uri(Model.resource(obj))
        obj.save()
        response = HttpResponse(status=200)
        return response

    def handle_follow(self, activity, **kwargs):
        followed_id = self.get_actor_id_or_404(**kwargs)

        if followed_id == activity.object:
            return Follower.objects.create(aid=activity.id, local_id=followed_id, remote_id=activity.actor)

    def handle_undo(self, activity, **kwargs):
        actor_id = self.get_actor_id_or_404(**kwargs)
        if actor_id == activity.object.object:
            return Follower.objects.filter(local_id=actor_id, remote_id=activity.object.actor).delete()


class OutboxView(ActivityPubView):
    '''
     You can POST to your outbox to send messages to the world (client-to-server)
     You can GET from someone's outbox to see what messages they've posted (or at least the ones you're authorized to see). (client-to-server and/or server-to-server)
    '''

    def list(self, request, **kwargs):
        local_id = "{}outbox/".format(self.get_actor_id_or_404(**kwargs))
        objects = Activity.objects.filter(
            local_id=local_id).order_by('-created_at').all()
        collection = activities.OrderedCollection(objects)
        return JsonResponse(collection.to_json(context=True))

    def post(self, request, **kwargs):
        local_id = self.get_actor_id_or_404(**kwargs)
        payload = request.body.decode("utf-8")
        activity = json.loads(payload, object_hook=as_activitystream)

        if activity.type == "Note":
            obj = activity
            activity = activities.Create(
                to="{}followers/".format(local_id),
                actor=local_id,
                object=obj
            )
            obj.attributedTo = local_id

        activity.validate()

        if activity.type == "Create":
            if activity.object.type != "Note":
                raise Exception("Sorry, you can only create Notes objects")

            content = activity.object.content
            # note = Note.objects.create(content=content, local_id=local_id)

            payload = bytes(json.dumps(activity.to_json()), "utf-8")
            obj = Activity.objects.create(local_id=local_id, payload=payload)
            obj.aid = self.uri(Model.resource(obj))
            obj.save()
            # note.aid = obj.aid
            # note.save()
            AP.deliver(activity)

            return HttpResponseRedirect(obj.id)

        raise Exception("Invalid Request")

