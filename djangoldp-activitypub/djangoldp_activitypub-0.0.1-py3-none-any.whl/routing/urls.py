from importlib import import_module

from django.conf import settings
from django.conf.urls import url

from djangoldp.models import Model
from djangoldp_activitypub.views import ActorView, FollowingView, FollowersView, InboxView, OutboxView


def __clean_path(path):
    if path.startswith("/"):
        path = path[1:]
    if not path.endswith("/"):
        path = "{}/".format(path)
    return path


urlpatterns = [
    url(r'^(?P<container>[0-9A-Za-z_\-]+)/(?P<id>[0-9A-Za-z_\-]+)/following/', FollowingView.as_view({'get': 'list'}),
        name="following"),
    url(r'^(?P<container>[0-9A-Za-z_\-]+)/following/', FollowingView.as_view({'get': 'list'}),
        name="following"),
    url(r'^(?P<container>[0-9A-Za-z_\-]+)/(?P<id>[0-9A-Za-z_\-]+)/followers/', FollowersView.as_view({'get': 'list'}),
        name="followers"),
    url(r'^(?P<container>[0-9A-Za-z_\-]+)/followers/', FollowersView.as_view({'get': 'list'}),
        name="followers"),
    url(r'^(?P<container>[0-9A-Za-z_\-]+)/inbox/', InboxView.as_view({'get': 'list', 'post': 'post'}),
        name="service_inbox"),
    url(r'^(?P<container>[0-9A-Za-z_\-]+)/(?P<id>[0-9A-Za-z_\-]+)/inbox/', InboxView.as_view({'get': 'list', 'post': 'post'}),
        name="obj_inbox"),
    url(r'^(?P<container>[0-9A-Za-z_\-]+)/outbox/', OutboxView.as_view({'get': 'list', 'post': 'post'}),
        name="service_inbox"),
    url(r'^(?P<container>[0-9A-Za-z_\-]+)/(?P<id>[0-9A-Za-z_\-]+)/outbox/', OutboxView.as_view({'get': 'list', 'post': 'post'}),
        name="obj_inbox"),
    url(r'^(?P<container>[0-9A-Za-z_\-]+)/(?P<id>[0-9A-Za-z_\-]+)/', ActorView.as_view({'get': 'get'}),
        name="ap_group"),
    url(r'^(?P<container>[0-9A-Za-z_\-]+)/', ActorView.as_view({'get': 'get'}), name="ap_service"),
]

for package in settings.DJANGOLDP_PACKAGES:
    try:
        import_module('{}.models'.format(package))
    except ModuleNotFoundError:
        pass

model_classes = {cls.__name__: cls for cls in Model.__subclasses__()}

for class_name in model_classes:
    model_class = model_classes[class_name]
    path = __clean_path(model_class.get_container_path())
