from typing import Optional, Dict


RegistryInstances = Dict[object, Dict[Optional[str], object]]


class RegistryError(Exception):
    pass


class RegistryInstanceRegisteredError(RegistryError):
    pass


class RegistryInstanceNotFoundError(RegistryError):
    pass


class Registry:
    def __init__(self):
        self.instances: RegistryInstances = {}

    def add(self, instance: object, name: Optional[str]=None):
        instance_class = instance.__class__
        instance_name = getattr(instance, 'name', None) if name is None else name

        if instance_class not in self.instances:
            self.instances[instance_class] = {}

        if instance_name in self.instances[instance_class]:
            raise RegistryInstanceRegisteredError(f'Instance with given class and name already registered (class: {instance_class.__name__}, name: {instance_name})')

        self.instances[instance_class][instance_name] = instance

    def get(self, instance_class: object, name: Optional[str]=None) -> object:
        try:
            instances = self.instances[instance_class]

            if name is None:
                return instances[list(instances.keys())[0]]

            return instances[name]

        except KeyError:
            raise RegistryInstanceNotFoundError(f'Instance not found (class: {instance_class.__name__}, name: {name})')
