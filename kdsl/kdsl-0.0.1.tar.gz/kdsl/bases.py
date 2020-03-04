import yaml
import sys


def ensure_dict(value):
    if isinstance(value, K8sObjectBase):
        return value.__asdict__()

    if isinstance(value, dict):
        return {k: ensure_dict(v) for k,v in value.items()}

    if isinstance(value, list):
        return [ensure_dict(x) for x in value]

    return value


class K8sObjectBase:
    def __asdict__(self):
        ret = {}

        for a in self.__attrs_attrs__:
            if (yaml_name := a.metadata['yaml_name']) is not None:
                if (value := getattr(self, a.name)) is not None:
                    ret[yaml_name] = ensure_dict(value)

        return ret


class K8sResourceBase(K8sObjectBase):
    def __asdict__(self):
        return {
            'apiVersion': self.apiVersion,
            'kind': self.kind,
            'metadata': {  # name is required
                x: value
                for x in ['name', 'namespace', 'labels', 'annotations']
                if (value := getattr(self, x)) is not None
            },
            **super().__asdict__(),
        }


def render_to_stdout(objs):
    yaml.safe_dump_all(ensure_dict(objs), stream=sys.stdout)
