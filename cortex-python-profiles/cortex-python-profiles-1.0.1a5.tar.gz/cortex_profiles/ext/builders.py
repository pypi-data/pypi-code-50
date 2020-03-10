"""
Copyright 2019 Cognitive Scale, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import math
import sys
import time
import traceback
from abc import ABC, abstractmethod
from itertools import chain, tee
from pprint import pformat
from typing import Any, Callable
from typing import List, Optional, cast, Iterable, Tuple, Iterator
from urllib.parse import urlparse

import arrow
import attr
import deprecation
import pydash
from cortex.client import Client as CortexClient
from cortex.utils import decode_JWT, get_logger
from pymongo import MongoClient
from pymongo.errors import BulkWriteError

from cortex_common.types import EntityEvent, ProfileAttributeType, ProfileSchema, ProfileAttributeSchema, \
    ProfileTagSchema, ProfileFacetSchema, ProfileTaxonomySchema, EntityRelationshipEvent, ObservedProfileAttribute
from cortex_common.utils import chunk_iterable
from cortex_profiles.build.attributes.utils.etl_utils import turn_attribute_into_entity_event, \
    turn_entity_event_into_attribute
from cortex_profiles.ext import clients
from cortex_profiles.ext.casting import cast_ee_into_attr_value_according_to_schema
from cortex_profiles.ext.rest import ProfilesRestClient

log = get_logger(__name__)

__all__ = [
    "ProfilesBuilder",
    "BulkProfilesBuilder",
    "ProfileSchemaBuilder",
]


# def default_db_uri(self) -> str:
#     """
#     # The URI configured ... may be the cluster specific URI ...
#     # The URI users connect to ... may be different ... maybe I shouldn't provide a default for now ... since this
#     # will only work if the db is externalized ...
#     # Also different tenants all use the same db ...
#     :return:
#     """
#     config = self._profiles_client._get("graph/_/config").json()
#     return base64decode_string(config.get(base64encode_string('mongo.graphUri'), ''))


class AbstractProfilesBuilder(ABC):

    def __init__(self, profiles_client: [ProfilesRestClient, CortexClient],
                 schema_id: Optional[str] = None, casting: bool = True):
        if isinstance(profiles_client, CortexClient):
            profiles_client = ProfilesRestClient.from_cortex_client(profiles_client)
        # Refreshing the client to ensure that there is a valid jwt token!
        self._profiles_client: ProfilesRestClient = profiles_client.refresh_client()
        self._schemaId = schema_id
        self._schema = profiles_client.describeSchema(schema_id)
        if casting and not self._schema:
            error_msg = "Schema could not be retrieved and casting is enabled. Schema is required for casting."
            log.error(error_msg)
            raise ValueError(f"Failed to Instantiate Profile Builder. {error_msg}")
        self._casting_enabled = casting and self._schema
        if self._schema is not None:
            self._attrs_in_schema = self._schema.attributes_in_schema()
            self._mapping_of_attrs_in_schema = self._schema.mapping_of_attributes_in_schema()

    @abstractmethod
    def with_events(self, *args, **kwargs):
        pass

    @abstractmethod
    def with_attributes(self, *args, **kwargs):
        pass

    @abstractmethod
    def build(self):
        pass

    def keep_event(self, ee: [EntityEvent, EntityRelationshipEvent]) -> bool:
        # If casting is disabled ... save everything ...
        if not self._casting_enabled:
            return True
        if ee.entityType == self._schema.profileType and ee.event in self._attrs_in_schema:
            return True
        return False

    def cast_event(self, ee: [EntityEvent, EntityRelationshipEvent]) -> Tuple[Optional[EntityEvent], Optional[str]]:
        if not self._casting_enabled:
            return ee
        attribute_value = cast_ee_into_attr_value_according_to_schema(
            ee=ee, attr_schema=self._mapping_of_attrs_in_schema[ee.event]
        )
        if attribute_value is None:
            return None, f"Failed to cast Entity Event {ee} according to schema {self._schemaId}"
        return ee.with_attribute_value(attribute_value), None

    def cast_events(self, events: Iterable[EntityEvent]) -> Iterator[Tuple[Optional[EntityEvent], Optional[str]]]:
        return (self.cast_event(ee) for ee in events)

    def stream_valid_events(self,
                            stream_of_casted_events: Iterator[Tuple[Optional[EntityEvent], Optional[str]]]
                            ) -> Iterator[EntityEvent]:
        return (
            ee
            for (ee, error) in stream_of_casted_events
            if error is None and self.keep_event(ee)
        )

    def stream_errors(self,
                      stream_of_casted_events: Iterator[Tuple[Optional[EntityEvent], Optional[str]]]
                      ) -> Iterator[str]:
        return (
            (
                error if error is not None
                else f"Event[{ee}] for ProfileType[{ee.entityType}] not found in Schema[{self._schemaId}]"
            )
            for (ee, error) in stream_of_casted_events
            if (error is not None) or (not self.keep_event(ee))
        )


def timed_mongo_bulk_load(collection, *args, precision=6, **kwargs):
    ts = time.time()
    result = None
    exception = None
    exception_details = None
    try:
        result = collection.insert_many(*args, **kwargs)
    except BulkWriteError as bwe:
        exception = sys.exc_info()
        exception_details = pformat(bwe.details)
    te = time.time()
    return (f'%2.{precision}f' % (te - ts), result, exception, exception_details)


class BulkProfilesBuilder(AbstractProfilesBuilder):

    def __init__(self, cortex_client: CortexClient, schemaId: Optional[str] = None, db_uri: Optional[str] = None):
        """
        - [ ] Todo ... add param of schemaId:Optional[str] to enable validation against schema before saving events
        :param cortex_client:
        :param db_uri:
        """
        super().__init__(cortex_client, schemaId)
        # Database Stuff (explicitly referencing mongo for now ... will eventually decouple)
        self._db_uri = db_uri
        self._mongo_client: MongoClient = MongoClient(db_uri)
        self._mongo_db = urlparse(db_uri).path[1:]

        # Initializing Builder State ...
        self._events: List[Iterator[EntityEvent]] = []
        self._invalid_events: List[Iterator[str]] = []
        self._attributes: List[Iterator[ProfileAttributeType]] = []

    def _extract_tenant_id(self):
        return decode_JWT(
            self._profiles_client._serviceconnector.token, verify=False
        ).get("tenant")

    def _get_collection(self, collection):
        return self._mongo_client[self._mongo_db][collection]

    def ee_overrides(self, tenant_id, version):
        return {
            "_environmentId": "cortex/default",
            "_tenantId": tenant_id,
            "meta": {
                "bulk_inserted_at": version
            }
        }

    def attr_overrides(self, tenant_id, version):
        return {
            "tenantId": tenant_id,
            "seq": version,
            "environmentId": "cortex/default",
            "createdAt": arrow.utcnow().datetime,
        }

    def with_events(self, event_chunk: Iterable[EntityEvent], **ee_to_attr_convertor_kwargs):
        """
        Appends the provided events to the list of events that will be used to build profiles.

        At this level ... we need to know what the attribute type is {inferred, observed, ...}
            ... currently the graph service assumes that entity events lead to observed attributes ...
        :param event_chunk:
        :return:
        """
        casted_events = (self.cast_event(ee) for ee in event_chunk)
        event_chunk_for_events, event_chunk_for_attrs, event_chunk_for_invalid_events = tee(casted_events, 3)
        # Add chunk of raw events to save ...
        self._events.append(self.stream_valid_events(event_chunk_for_events))
        # Add chunk of invalid events
        self._invalid_events.append(self.stream_errors(event_chunk_for_invalid_events))
        # Add chunk of attributes to save ...
        self.with_attributes(
            turn_entity_event_into_attribute(
                e,
                **pydash.defaults(
                    ee_to_attr_convertor_kwargs,
                    {
                        "attributeType": ObservedProfileAttribute
                    }
                )
            )
            for e in self.stream_valid_events(event_chunk_for_attrs)
        )
        return self

    def with_attributes(self, attribute_chunk: Iterable[ProfileAttributeType]):
        """
        Converts the provided attributes into a list of events and appends them to the list of events that will be
        used to build profiles.
        :param attribute_chunk:
        :return:
        """
        self._attributes.append(attribute_chunk)
        return self

    def _format_chunk_response(self, items_in_chunk, chunk_index,
                               chunk_insert_duration, chunk_insert_response, chunk_insert_exception,
                               chunk_insert_exception_details, chunk_completion_time, verbose):
        response = {
            "chunk_number": chunk_index + 1,
            "total_items_in_chunk": len(items_in_chunk),
            "time_taken_to_insert_chunk": chunk_insert_duration,
            "insert_finished_at": str(chunk_completion_time),
            "exception_occurred": chunk_insert_exception is not None,
        }
        if verbose:
            if chunk_insert_exception is None:
                response["insert_response_inserted_ids"] = [str(y) for y in chunk_insert_response.inserted_ids]
                response["insert_response_acknowledged"] = chunk_insert_response.acknowledged
            # If an exception happened ... add traceback
            else:
                response["exception_traceback"] = traceback.print_exception(
                    *chunk_insert_exception
                )
                response["exception_type"] = chunk_insert_exception[0]
                response["exception_value"] = str(chunk_insert_exception[1])
                response["exception_details"] = str(chunk_insert_exception_details)
        return response

    def bulk_insert_chunk(self, chunk_index:int, document_chunk:List, processing_seq:int, collection:Any,
                          override_func:Callable, chunk_name_in_logs:str, profile_id_field:str,
                          total_items_processed:int, total_processing_time:float,
                          verbose:bool) -> Tuple[set, List, int, int]:

        loaded_attrs_in_chunk = [
            pydash.merge({}, dict(a), override_func(self._extract_tenant_id(), processing_seq))
            for a in document_chunk
        ]
        (duration, bi_response, bi_exception, bi_exception_details) = timed_mongo_bulk_load(
            collection, loaded_attrs_in_chunk, ordered=False
        )
        resp = self._format_chunk_response(
            items_in_chunk=loaded_attrs_in_chunk, chunk_index=chunk_index, chunk_insert_duration=duration,
            chunk_insert_response=bi_response, chunk_insert_exception=bi_exception,
            chunk_insert_exception_details=bi_exception_details,
            chunk_completion_time=arrow.utcnow().datetime, verbose=verbose
        )
        total_items_processed += resp['total_items_in_chunk']
        total_processing_time += float(resp['time_taken_to_insert_chunk'])
        insert_responses = resp
        a, b, c, d = (
            resp['total_items_in_chunk'], total_items_processed,
            resp['time_taken_to_insert_chunk'], total_processing_time
        )
        log.info(
            f"Inserted {a:,d} {chunk_name_in_logs} in {c} seconds. {b:,d} so far in {d:2.4f} seconds"
        )
        profile_ids_to_flush = set([
            pydash.get(attr, profile_id_field)
            for attr in loaded_attrs_in_chunk
        ])
        return profile_ids_to_flush, insert_responses, total_items_processed, total_processing_time

    def build(self, verbose=False, chunk_size=10_000) -> Tuple[List,List]:
        """
        Saves attributes to profiles in bulk, one chunk at a time.
        (Optionally) Saves profile building events in bulk ...
        * It is the responsibility of the invoker to ensure that all chunks were properly inserted and retry as needed.
        * This method does not assert that all the chunks get saved fully;
            It does however return status of the bulk save for each chunk.
        * This method logs progress as chunks are incrementally saved ...

        For reference's sake ...:
        >>> arrow.utcnow().datetime                   # datetime(2020, 2, 17, 16, 37, 25, 350303, tzinfo=tzutc())
        >>> arrow.utcnow().datetime.timestamp()       # 1581957467.937602
        >>> arrow.utcnow().datetime.timestamp()*1000  # 1581957467937.602
        :return: the resulting responses from the bulk output
        """
        # The version of attributes is based on the time this method was invoked
        seq = math.floor(arrow.utcnow().datetime.timestamp() * 1000)

        # Interleave Attribute and Event Chunks so that the iterators tees dont get out of sync ...
        attribute_stream = chain(*self._attributes)
        event_stream = chain(*self._events)
        invalid_event_stream = chain(*self._invalid_events)

        attribute_insert_responses, total_attrs_processed, total_attrs_processing_time = [], 0, 0
        event_insert_responses, total_events_processed, total_events_processing_time = [], 0, 0

        (next_attr_chunk, next_event_chunk, next_invalid_event_chunk) = (
            next(enumerate(chunk_iterable(attribute_stream, chunk_size)), []),
            next(enumerate(chunk_iterable(event_stream, chunk_size)), []),
            next(enumerate(chunk_iterable(invalid_event_stream, chunk_size)), []),
        )
        while next_attr_chunk or next_event_chunk or next_invalid_event_chunk:
            profile_ids_to_flush = set([])
            # Insert Each Chunk of attributes
            if next_attr_chunk:
                (
                    new_profile_ids,
                    new_insert_records,
                    total_attrs_processed,
                    total_attrs_processing_time
                ) = self.bulk_insert_chunk(
                    chunk_index=next_attr_chunk[0], document_chunk=next_attr_chunk[1],
                    override_func = self.attr_overrides, processing_seq=seq,
                    collection=self._get_collection("attributes"),
                    chunk_name_in_logs="Attributes  ", profile_id_field = "profileId",
                    total_items_processed=total_attrs_processed,
                    total_processing_time=total_attrs_processing_time,
                    verbose=verbose
                )
                profile_ids_to_flush = profile_ids_to_flush.union(new_profile_ids)
                attribute_insert_responses.append(new_insert_records)
            # Insert Each Chunk of Events ...
            if next_event_chunk:
                (
                    new_profile_ids,
                    new_insert_records,
                    total_events_processed,
                    total_events_processing_time
                ) = self.bulk_insert_chunk(
                    chunk_index=next_event_chunk[0], document_chunk=next_event_chunk[1],
                    override_func=self.ee_overrides, processing_seq=seq,
                    collection=self._get_collection("entity-events"),
                    chunk_name_in_logs="EntityEvents", profile_id_field="entityId",
                    total_items_processed=total_events_processed,
                    total_processing_time=total_events_processing_time,
                    verbose=verbose
                )
                profile_ids_to_flush = profile_ids_to_flush.union(new_profile_ids)
                event_insert_responses.append(new_insert_records)
            # Invalidate Cache for profiles
            if next_invalid_event_chunk:
                (invalid_event_chunk_index, invalid_event_chunk) = next_invalid_event_chunk
                for error_message in invalid_event_chunk:
                    log.error(error_message)
            # Flush cache ...
            log.info(self._profiles_client.delete_cache_for_specific_profiles(list(profile_ids_to_flush)))
            # Move on to next chunks
            (next_attr_chunk, next_event_chunk, next_invalid_event_chunk) = (
                next(enumerate(chunk_iterable(attribute_stream, chunk_size)), []) if next_attr_chunk else None,
                next(enumerate(chunk_iterable(event_stream, chunk_size)), []) if next_event_chunk else None,
                (
                    next(enumerate(chunk_iterable(invalid_event_stream, chunk_size)), [])
                    if next_invalid_event_chunk else None
                )
            )

        return (seq, attribute_insert_responses, event_insert_responses)


class ProfilesBuilder(AbstractProfilesBuilder):

    """
    A builder utility to aid in programmatic creation of Cortex Profiles.
    Not meant to be directly instantiated by users of the sdk.
    """

    def __init__(self, profiles_client: ProfilesRestClient, schemaId: Optional[str] = None):
        """
        :param profiles_client:
        :param schemaId:
        """
        super().__init__(profiles_client, schemaId)
        self._events: List[EntityEvent] = []

    def with_events(self, events: List[EntityEvent]) -> 'ProfilesBuilder':
        """
        Appends the provided events to the list of events that will be used to build profiles.
        :param events:
        :return:
        """
        casted_events = list(self.cast_events(events))
        errors = self.stream_errors(casted_events)
        for error in errors:
            log.error(error)
        valid_events = list(self.stream_valid_events(casted_events))
        self._events.extend(valid_events)
        return self

    @deprecation.deprecated(deprecated_in='6.0.1b1', details='Use with_events instead.')
    def with_attributes(self, attributes: List[ProfileAttributeType]) -> 'ProfilesBuilder':
        """
        Converts the provided attributes into a list of events and appends them to the list of events that will be
        used to build profiles.
        :param attributes:
        :return:
        """
        self._events.extend([
            turn_attribute_into_entity_event(a, defaultEntityType=self._schemaId)
            for a in attributes
        ])
        return self

    def build(self) -> List[str]:
        """
        Pushes profile building events and returns the response from the building process ...
        :return: the resulting Connection
        """
        # return Profile.get_profile(self._profileId, self._schemaId, self._profiles_client)
        return self._profiles_client.pushEvents(self._events)


class ProfileSchemaBuilder(object):

    """
    A builder utility to aid in programmatic creation of Schemas for Cortex Profiles.
    Not meant to be directly instantiated by users of the sdk.
    """

    def __init__(self, schema:ProfileSchema, profiles_client:ProfilesRestClient):
        """
        Initializes the builder from the profile schema type ...
        :param schema:
        :return:
        """
        self._schema = schema
        self._profiles_client = profiles_client

    def name(self, name:str) -> 'ProfileSchemaBuilder':
        """
        Sets the name of the schema ...
        :param name:
        :return:
        """
        self._schema = attr.evolve(self._schema, name=name)
        return self

    def title(self, title:str) -> 'ProfileSchemaBuilder':
        """
        Sets the title of the schema ...
        :param title:
        :return:
        """
        self._schema = attr.evolve(self._schema, title=title)
        return self

    def profileType(self, profileType:str) -> 'ProfileSchemaBuilder':
        """
        Sets the profileType of the schema ...
        :param profileType:
        :return:
        """
        self._schema = attr.evolve(self._schema, profileType=profileType)
        return self

    def description(self, description:str) -> 'ProfileSchemaBuilder':
        """
        Sets the description of the schema ...
        :param description:
        :return:
        """
        self._schema = attr.evolve(self._schema, description=description)
        return self

    def facets(self, facets:List[ProfileFacetSchema]) -> 'ProfileSchemaBuilder':
        """
        Sets the facets of the schema ...
        :param facets:
        :return:
        """
        self._schema = attr.evolve(self._schema, facets=facets)
        return self

    def taxonomy(self, taxonomy:List[ProfileTaxonomySchema]) -> 'ProfileSchemaBuilder':
        """
        Sets the taxonomy of the schema ...
        :param taxonomy:
        :return:
        """
        self._schema = attr.evolve(self._schema, taxonomy=taxonomy)
        return self

    def attributes(self, attributes:List[ProfileAttributeSchema]) -> 'ProfileSchemaBuilder':
        """
        Sets the attributes of the schema ...
        :param attributes:
        :return:
        """
        self._schema = attr.evolve(self._schema, attributes=attributes)
        return self

    def attributeTags(self, attributeTags:List[ProfileTagSchema]) -> 'ProfileSchemaBuilder':
        """
        Sets the attributeTags of the schema ...
        :param attributeTags:
        :return:
        """
        self._schema = attr.evolve(self._schema, attributeTags=attributeTags)
        return self

    def build(self) -> clients.ProfileSchema:
        """
        Builds and saves a new Profile Schema using the properties configured on the builder
        :return:
        """
        # Push Schema ...
        self._profiles_client.pushSchema(self._schema)
        # Get latest schema ...
        return clients.ProfileSchema.get_schema(
            cast(str, self._schema.name), self._profiles_client)


if __name__ == '__main__':
    pass
    # log.info(bulk_profile_builder.build(verbose=True))
    # Test to iteratively insert a million attributes!
    # Sum up all the times at the end!