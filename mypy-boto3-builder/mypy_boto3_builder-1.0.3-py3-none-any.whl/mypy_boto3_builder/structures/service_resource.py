"""
Boto3 ServiceResource.
"""
from dataclasses import dataclass, field
from typing import List, Set, Optional

from boto3.resources.base import ServiceResource as Boto3ServiceResource

from mypy_boto3_builder.service_name import ServiceName, ServiceNameCatalog
from mypy_boto3_builder.import_helpers.import_string import ImportString
from mypy_boto3_builder.type_annotations.fake_annotation import FakeAnnotation
from mypy_boto3_builder.type_annotations.external_import import ExternalImport
from mypy_boto3_builder.structures.class_record import ClassRecord
from mypy_boto3_builder.structures.collection import Collection
from mypy_boto3_builder.structures.resource import Resource


@dataclass
class ServiceResource(ClassRecord):
    """
    Boto3 ServiceResource.
    """

    name: str = "ServiceResource"
    alias_name: str = "ServiceResource"
    service_name: ServiceName = ServiceNameCatalog.ec2
    boto3_service_resource: Optional[Boto3ServiceResource] = None
    collections: List[Collection] = field(default_factory=lambda: [])
    sub_resources: List[Resource] = field(default_factory=lambda: [])
    bases: List[FakeAnnotation] = field(
        default_factory=lambda: [
            ExternalImport(
                source=ImportString("boto3", "resources", "base"),
                name="ServiceResource",
                alias="Boto3ServiceResource",
            )
        ]
    )

    def __hash__(self) -> int:
        return hash(self.service_name)

    def get_types(self) -> Set[FakeAnnotation]:
        types = super().get_types()
        for collection in self.collections:
            types.update(collection.get_types())
        for sub_resource in self.sub_resources:
            types.update(sub_resource.get_types())

        return types

    def get_all_names(self) -> List[str]:
        result = [self.name]
        for resource in self.sub_resources:
            result.append(resource.name)
        for collection in self.get_collections():
            result.append(collection.name)
        return result

    def get_collections(self) -> List[Collection]:
        collection_names = [i.name for i in self.collections]
        result: List[Collection] = []
        result.extend(self.collections)
        for resource in self.sub_resources:
            for collection in resource.collections:
                if collection.name in collection_names:
                    raise ValueError(f"Conflicting collections: {collection.name}")
                collection_names.append(collection.name)
                result.append(collection)

        return result

    def get_sub_resources(self) -> List[Resource]:
        """
        Get sub-resource in safe order.

        Returns:
            A list of sub resources.
        """
        result: List[Resource] = []
        all_names: Set[str] = {i.name for i in self.sub_resources}
        added_names: Set[str] = set()
        sub_resources = list(self.sub_resources)
        max_tries = 200
        try_count = 0
        while sub_resources:
            sub_resource = sub_resources[0]
            internal_imports = sub_resource.get_internal_imports()
            internal_import_names = {i.name for i in internal_imports} & all_names
            if internal_import_names.issubset(added_names):
                result.append(sub_resource)
                added_names.add(sub_resource.name)
                sub_resources = sub_resources[1:]
                continue

            try_count += 1
            if try_count > max_tries:
                break
            sub_resources = sub_resources[1:] + [sub_resource]

        for sub_resource in sub_resources:
            internal_imports = sub_resource.get_internal_imports()
            for internal_import in internal_imports:
                internal_import.stringify = True

            result.append(sub_resource)

        return result
