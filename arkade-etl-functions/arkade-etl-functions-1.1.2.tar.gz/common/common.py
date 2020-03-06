import json
import requests
import os
from google.cloud import datastore
from google.cloud import storage
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(os.getcwd() + '/datastore/Arkade Storefront-193d74715b48.json', scopes=["https://www.googleapis.com/auth/cloud-platform"], )


def get_cwd():

    return print("Current working directory: {}".format(os.getcwd()))


def get_source_datastore(project, namespace):
    source_datastore = datastore.Client(
        project=project, namespace=namespace, credentials=credentials)

    return source_datastore


def get_storage_bucket():
    storage_client = storage.Client.from_service_account_json(
        os.getcwd() + '/datastore/Arkade Storefront-193d74715b48.json')
    bucket = storage_client.get_bucket('etl-reports')

    return bucket


def get_entities(project, namespace, entity_key, entity_offset=0, entity_limit=500):
    datastore_client = get_source_datastore(project, namespace)

    entities = list(datastore_client.query(kind=entity_key).fetch(
        offset=entity_offset, limit=entity_limit))

    return entities


def get_entity_mapper():
    with open(os.getcwd() + '/datastore/entityMapping.json') as f:
        entityMapper = json.load(f)

    return entityMapper


def copy_entity(project, entity, entity_key, target_namespace, update_object, reason=False):
    datastore_client = get_source_datastore(project, target_namespace)

    if reason:
        update_object['reason'] = reason

    # create the entity key to add the entity
    process_key = datastore_client.key(entity_key, entity['id'])
    process = datastore.Entity(key=process_key)

    process.update(update_object)

    # Move the entity from source to target namespace.
    try:
        datastore_client.put(process)
        print(
            "* Copied entity {} to {} namespace".format(entity['id'], target_namespace))
        return entity
    except requests.exceptions.RequestException as err:
        return "Request exception to move an entity" + repr(err)


def delete_entity(project, entity, entity_key, namespace):
    datastore_client = get_source_datastore(project, namespace)

    # get the entity key to delete the entity
    process_key = datastore_client.key(entity_key, entity['id'])

    # Delete the entity from source namespace.
    try:
        datastore_client.delete(process_key)
        print(
            "* Deleted entity {} from {} namespace".format(entity['id'], namespace))
        return entity
    except requests.exceptions.RequestException as err:
        return "Request exception to delete an entity" + repr(err)
