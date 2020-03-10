# -*- coding: utf-8 -*-
import logging
import functools
from datetime import datetime
from _collections import defaultdict

from spaceone.core.manager import BaseManager
from spaceone.inventory.manager import CollectorManager
from spaceone.inventory.error import *

_METADATA_KEYS = ['details', 'sub_data']
_LOGGER = logging.getLogger(__name__)


class CollectionDataManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update_history = {}
        self.collector_priority = {}
        self.collector_mgr: CollectorManager = self.locator.get_manager('CollectorManager')

    def update_pinned_keys(self, keys, collection_info):
        update_keys = self._get_all_update_keys(collection_info.update_history)

        for key in keys:
            if key not in update_keys:
                raise ERROR_NOT_ALLOW_PINNING_KEYS(key=key)

        return {
            'state': collection_info.state,
            'collectors': collection_info.collectors,
            'update_history': collection_info.update_history,
            'pinned_keys': keys
        }

    @staticmethod
    def exclude_data_by_pinned_keys(resource_data, collection_info):
        for key in collection_info.pinned_keys:
            if key.startswith('data.'):
                sub_key = key.split('.')[1]

                if sub_key in resource_data.get('data', {}):
                    del resource_data['data'][sub_key]
            else:
                if key in resource_data:
                    del resource_data[key]

        return resource_data

    def create_new_history(self, resource_data, domain_id, collector_id, **kwargs):
        exclude_keys = kwargs.get('exclude_keys', []) + ['metadata']

        if collector_id:
            self.collector_mgr.get_collector(collector_id, domain_id)
            all_collectors = [collector_id]
            state = 'ACTIVE'
        else:
            collector_id = 'MANUAL'
            all_collectors = []
            state = 'MANUAL'

        self._create_update_data_history(resource_data, collector_id, exclude_keys)

        collection_info = {
            'state': state,
            'collectors': all_collectors,
            'update_history': self._make_update_history()
        }

        return collection_info

    def exclude_data_by_history(self, resource_data, domain_id, collection_info, collector_id, **kwargs):
        exclude_keys = kwargs.get('exclude_keys', []) + ['metadata']
        current_collectors = collection_info.collectors

        if collector_id:
            new_collector_vo = self.collector_mgr.get_collector(collector_id, domain_id)
            all_collectors = list(set(current_collectors + [collector_id]))
            state = 'ACTIVE'
            priority = new_collector_vo.priority
        else:
            collector_id = 'MANUAL'
            all_collectors = current_collectors
            state = collection_info.state
            priority = 0

        self._get_collector_priority(current_collectors)
        self._load_update_history(collection_info.update_history)
        excluded_resource_data = self._compare_data(resource_data,
                                                    collector_id,
                                                    priority,
                                                    exclude_keys)

        excluded_resource_data['collection_info'] = {
            'state': state,
            'collectors': all_collectors,
            'update_history': self._make_update_history(),
            'pinned_keys': collection_info.pinned_keys
        }

        return excluded_resource_data

    @staticmethod
    def merge_data(old_data, new_data):
        merged_data = old_data.copy()
        merged_data.update(new_data)
        return merged_data

    @staticmethod
    def merge_metadata(old_metadata, new_metadata):
        metadata = {}
        """
        result = defaultdict(dict)
        for sequence in (l1, l2):
            for dictionary in sequence:
                result[dictionary['id']].update(dictionary)
        for dictionary in result.values():
            dictionary.pop('id')
        """
        for meta_key in _METADATA_KEYS:
            meta_values = defaultdict(dict)
            for sequence in (old_metadata.get(meta_key, []), new_metadata.get(meta_key, [])):
                for meta_value in sequence:
                    meta_values[meta_value['name']].update(meta_value)

            metadata[meta_key] = meta_values.values()
            # for key, items in new_metadata.items():
        #     for item in items:
        #         metadata[key].append(item)

        return metadata

    @staticmethod
    def _exclude_metadata_item(items, collector_id):
        changed_items = []
        for item in items:
            if item.get('updated_by') != collector_id:
                changed_items.append(item)

        return changed_items

    @staticmethod
    def _get_all_update_keys(update_history):
        update_keys = []
        for update_info in update_history:
            update_keys.append(update_info.key)

        return update_keys

    def _create_update_data_history(self, resource_data, collector_id, exclude_keys):
        updated_at = datetime.utcnow().timestamp()

        for key, value in resource_data.items():
            if key == 'data':
                self._set_data_history(value, exclude_keys, collector_id, updated_at)
            elif key == 'metadata':
                self._set_metadata_history(value, collector_id, updated_at)
            else:
                self._set_field_data_history(key, exclude_keys, collector_id, updated_at)

    def _set_data_history(self, value, exclude_keys, collector_id, updated_at):
        for sub_key in value.keys():
            if f'data.{sub_key}' not in exclude_keys:
                self.update_history[f'data.{sub_key}'] = {
                    'updated_by': collector_id,
                    'updated_at': updated_at
                }

    def _set_metadata_history(self, value, collector_id, updated_at):
        for meta_key, meta_values in value.items():
            self._check_metadata_item(meta_key, meta_values)
            for meta_value in meta_values:
                if 'name' in meta_value:
                    self.update_history[f'metadata.{meta_key}.{meta_value["name"].strip()}'] = {
                        'updated_by': collector_id,
                        'updated_at': updated_at
                    }

    def _set_field_data_history(self, key, exclude_keys, collector_id, updated_at):
        if key not in exclude_keys:
            self.update_history[key] = {
                'updated_by': collector_id,
                'updated_at': updated_at
            }

    @staticmethod
    def _check_metadata_item(key, values):
        if key not in _METADATA_KEYS:
            raise ERROR_INVALID_METADATA_KEY()

        if not isinstance(values, list):
            raise ERROR_METADATA_LIST_VALUE_TYPE(key=key)

    def _get_collector_priority(self, collectors):
        query = {
            'only': ['collector_id', 'priority'],
            'filter': [{
                'k': 'collector_id',
                'v': collectors,
                'o': 'in'
            }]
        }

        collector_vos, total_count = self.collector_mgr.list_collectors(query)

        for collector_vo in collector_vos:
            self.collector_priority[collector_vo.collector_id] = collector_vo.priority

    def _load_update_history(self, current_update_history):
        for history_info in current_update_history:
            self.update_history[history_info.key] = {
                'priority': self.collector_priority.get(history_info.updated_by, 100),
                'updated_by': history_info.updated_by,
                'updated_at': history_info.updated_at
            }

    def _compare_data(self, resource_data, collector_id, priority, exclude_keys):
        updated_at = datetime.utcnow().timestamp()
        changed_data = {}

        for key, value in resource_data.items():
            if key == 'data':
                changed_data['data'] = self._check_data_priority(value, exclude_keys,
                                                                 collector_id, priority,
                                                                 updated_at)
            elif key == 'metadata':
                changed_data['metadata'] = self._check_metadata_priority(value, collector_id,
                                                                         priority, updated_at)
            else:
                is_data_remove = self._check_field_data_priority(key, collector_id,
                                                                 priority, updated_at)
                if not is_data_remove:
                    changed_data[key] = value

        return changed_data

    def _check_priority(self, key, priority):
        if key in self.update_history and self.update_history[key]['priority'] < priority:
            return True
        else:
            return False

    def _check_data_priority(self, data, exclude_keys, collector_id, priority, updated_at):
        changed_data = {}
        for sub_key, sub_value in data.items():
            key = f'data.{sub_key}'
            if key in exclude_keys:
                changed_data[sub_key] = sub_value
            else:
                if not self._check_priority(key, priority):
                    changed_data[sub_key] = sub_value

                    self.update_history[key] = {
                        'updated_by': collector_id,
                        'updated_at': updated_at
                    }

        return changed_data

    def _check_metadata_priority(self, metadata, collector_id, priority, updated_at):
        changed_metadata = {}
        for meta_key, meta_values in metadata.items():
            self._check_metadata_item(meta_key, meta_values)
            changed_metadata[meta_key] = []
            for value in meta_values:
                if 'name' in value:
                    key = f'metadata.{meta_key}.{value["name"].strip()}'
                    if not self._check_priority(key, priority):
                        changed_metadata[meta_key].append(value)

                        self.update_history[key] = {
                            'updated_by': collector_id,
                            'updated_at': updated_at
                        }

        return changed_metadata

    def _check_field_data_priority(self, key, collector_id, priority, updated_at):
        if self._check_priority(key, priority):
            return True
        else:
            self.update_history[key] = {
                'updated_by': collector_id,
                'updated_at': updated_at
            }
            return False

    def _make_update_history(self):
        update_history = []

        for key, value in self.update_history.items():
            update_history.append({
                'key': key,
                'updated_by': value['updated_by'],
                'updated_at': value['updated_at']
            })

        return update_history
