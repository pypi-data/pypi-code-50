from frater.dataset import dataset_factory
from .diva import diva_activities, diva_objects
from .something_something import something_something

dataset_factory.register_item(diva_activities, diva_activities.name)
dataset_factory.register_item(diva_objects, diva_objects.name)
dataset_factory.register_item(something_something, something_something.name)
