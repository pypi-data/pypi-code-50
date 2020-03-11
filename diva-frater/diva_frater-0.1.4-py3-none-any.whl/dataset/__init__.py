from frater.dataset import dataset_factory
from .diva import diva_activities, diva_objects
from .something_something import something_something

dataset_factory.register_item(diva_activities.name, diva_activities)
dataset_factory.register_item(diva_objects.name, diva_objects)
dataset_factory.register_item(something_something.name, something_something)
