# -*- coding: utf-8 -*-

import logging
import pprint
import random
import time

from datetime import datetime
from google.protobuf.json_format import MessageToDict

from spaceone.core import config
from spaceone.core import queue
from spaceone.core.error import *
from spaceone.core.manager import BaseManager
from spaceone.inventory.lib import rule_matcher
from spaceone.inventory.model.region_model import Region
from spaceone.inventory.model.zone_model import Zone
from spaceone.inventory.model.collector_model import Collector, Scheduler
from spaceone.inventory.model.job_model import Job


_LOGGER = logging.getLogger(__name__)

RESOURCE_MAP = {
    'SERVER': 'ServerManager',
    'NETWORK': 'NetworkManager',
    'NETWORK_POLICY': 'NetworkPolicyManager',
    'SUBNET': 'SubnetManager',
    'CLOUD_SERVICE': 'CloudServiceManager',
    'CLOUD_SERVICE_TYPE': 'CloudServiceTypeManager'
}

SERVICE_MAP = {
    'SERVER': 'ServerService',
    'NETWORK': 'NetworkService',
    'NETWORK_POLICY': 'NetworkService',
    'SUBNET': 'NetworkService',
    'CLOUD_SERVICE': 'CloudServiceService',
    'CLOUD_SERVICE_TYPE': 'CloudServiceTypeService'
}

##################################################
# TODO: split collector as directory
# 
# This is too heavy code, split as directory
# which has seperate functionality
##################################################

class CollectorManager(BaseManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.collector_model: Collector = self.locator.get_model('Collector')
        self.scheduler_model: Scheduler = self.locator.get_model('Scheduler')

    def create_collector(self, params):
        """
        Args: params
          - name
          - plugin_info
          - state
          - priority
          - tags
          - domain_id
        """
        def _rollback(collector_vo):
            _LOGGER.info(f'[ROLLBACK] Delete collector : {collector_vo.name} ({collector_vo.collector_id})')
            collector_vo.delete()

        # Create DB first, for easy manipulation
        collector_vo: Collector = self.collector_model.create(params)
        self.transaction.add_rollback(_rollback, collector_vo)

        domain_id = params['domain_id']
        # Verify Plugin
        # 1. get Endpoint
        # 2. Call verify
        # 3. update plugin options
        if 'plugin_info' in params:
            # get all credentials
            plugin_info = params['plugin_info']
            credentials_list = self._get_credentials(plugin_info, domain_id)
            _LOGGER.debug('[create_collector] cred_list: %s' % credentials_list)
            _LOGGER.debug('[create_collector] cred_list size: %s' % len(credentials_list))
            for cred_id in credentials_list:
                credentials = self._issue_credentials(cred_id, domain_id)
                updated_option = self._get_updated_options(collector_vo.plugin_info, credentials, domain_id)
                plugin_info.update({'options':updated_option})
                collector_vo = self.update_collector_by_vo(collector_vo, {'plugin_info': plugin_info})
        else:
            _LOGGER.warn("[create_collector] Plugin_info is not defined!")
        return collector_vo

    def verify_plugin(self, collector_id, credential_id, domain_id):

        updated_option = self._get_updated_options(collector_vo.plugin_info, domain_id)
        collector_vo = self.update_collector_by_vo(collector_vo, {'options':updated_option})
        return collector_vo


    def delete_collector(self, collector_id, domain_id):
        collector_vo:Collector = self.collector_model.get(collector_id=collector_id, domain_id=domain_id)
        collector_vo.delete()

    def delete_collector_by_vo(self, collector_vo):
        collector_vo.delete()

    def get_collector(self, collector_id, domain_id):
        collector_vo:Collector = self.collector_model.get(collector_id=collector_id, domain_id=domain_id)
        return collector_vo

    def exist_collector(self, collector_id, domain_id):
        """ Easy to check resource
        Returns:
            (True|False, VO)
        """
        try:
            collector_vo:Collector = self.collector_model.get(collector_id=collector_id, domain_id=domain_id)
            return (True, collector_vo)
        except ERROR_NOT_FOUND:
            return (False, None)
        except Exception as e:
            raise ERROR_UNKNOWN()

    def update_collector_by_vo(self, collector_vo, params):
        """ Update collector
        Get collector_vo, then update with this
        """
        return collector_vo.update(params)

    def enable_collector(self, collector_id, domain_id):
        collector_vo:Collector = self.collector_model.get(collector_id=collector_id, domain_id=domain_id)
        return collector_vo.update({'state':'ENABLED'})

    def disable_collector(self, collector_id, domain_id):
        collector_vo:Collector = self.collector_model.get(collector_id=collector_id, domain_id=domain_id)
        return collector_vo.update({'state':'DISABLED'})

    def list_collectors(self, query):
        return self.collector_model.query(**query)

    ##########################################################
    # collect
    #
    # links: https://pyengine.atlassian.net/wiki/spaces/CLOUD/pages/682459145/3.+Collector+Rule+Management
    #
    ##########################################################
    def collect(self, params):
        """
        Args:
            params
                - collector_id
                - filter
                - credential_id
                - collect_mode
                - domain_id
        """
        def _rollback(collector_vo):
            _LOGGER.info(f'[ROLLBACK] Delete collector : ({collector_vo.collector_id})')
            collector_vo.delete()

        collector_id = params['collector_id']
        domain_id = params['domain_id']

        if 'collect_mode' in params:
            collect_mode = params['collect_mode']
        else:
            collect_mode = 'ALL'

        # TODO: QUEUE name ?
        queue_name = 'collector_q'
        _LOGGER.debug(f'[collect] queue: {queue}')

        # Create Job DB
        params['collector'] = self.get_collector(collector_id, domain_id)
        params = self._check_filter(params)
        self.job_model: Job = self.locator.get_model('Job')
        job_vo = self.job_model.create(params)
        self.transaction.add_rollback(_rollback, job_vo)

        # patch job_id
        job_id = job_vo.job_id

        # get collector_info
        collector_info = self.get_collector(collector_id, domain_id)

        #################################
        # 1. get matched credential list
        #################################
        cred_id = params.get('credential_id', None)
        filters = params.get('filters', None)

        cred_list = self._matched_credentials(collector_info.plugin_info, domain_id, cred_id, filters)

        ######################
        # Manager initialize #
        ######################
        manager = {}
        service = {}
        resource_ids = []
        ###################################
        # 2. foreach call collector plugin
        ###################################
        # Create Collect Plugin Connector
        connector = self.locator.get_connector('CollectorPluginConnector')
        for cred in cred_list:
            # get endpoint
            plugin_info = collector_info.plugin_info
            endpoint = self._get_endpoint(plugin_info, domain_id)
            _LOGGER.debug('[collect] endpoint: %s' % endpoint)
            connector.initialize(endpoint)

            # call grpc method (unary -> stream)
            options = plugin_info.options
            # TEST: 
            filter_format = options.get('filter_format', [])
            _LOGGER.debug(f'[collect] options.filter_format: {filter_format}')

            ################################################################
            # 1. Check filter
            # based on params['filter'], make new filter for collector
            # filter_format
            ################################################################
            connector_filter = self._get_collector_filter(filters, filter_format)
            _LOGGER.debug(f'[collect] connector_filter: {connector_filter}')
            
            # retrieve credential content based on credential_id (=cred)
            cred_data = self._issue_credentials(cred, domain_id)

            ################################################################
            # 2. collect info
            ################################################################
            results = connector.collect(options, cred_data, connector_filter )
            _LOGGER.debug('[collect] generator: %s' % results)

            # update meta
            self.transaction.set_meta('job_id', job_id)
            self.transaction.set_meta('collector_id', collector_id)

            for res in results:
                try:
                    _LOGGER.debug('[collect] resource_type: %s' % res.resource_type)
                    resource = MessageToDict(res, preserving_proto_field_name=True)
                    data = resource['resource']
                    # Add domain_id at resource
                    data['domain_id'] = domain_id

                    ########################################################
                    # 3. Replace Reference Data
                    ########################################################
                    _LOGGER.debug(f'[collect] 3. Replace Reference Data: {resource}')
                    #res_type = resource['resource_type'].upper()
                    res_type = res.resource_type

                    # Get proper manager
                    if res_type not in manager:
                        mgr = self.locator.get_manager(RESOURCE_MAP[res_type])
                        manager[res_type] = mgr
                    else:
                        mgr = manager[res_type]

                    # Get proper service
                    if res_type not in service:
                        svc = self.locator.get_service(SERVICE_MAP[res_type], metadata=self.transaction.meta)
                        service[res_type] = svc
                    else:
                        svc = service[res_type]

                    match_rules = resource.get('match_rules', {})
                    #########################################################
                    # 4. check exist Resource (Create / Update)
                    #########################################################
                    _LOGGER.debug(f'[collect] 4. Create / Update')
                    res_info, total_count = self.query_with_match_rules(data, match_rules, domain_id, mgr)
                    _LOGGER.debug(f'[collect] matched resource count = {total_count}')
                    res_id = None

                    # resource_vo and total_count = 1 -> found
                    if total_count == 0:
                        # Create
                        _LOGGER.debug('[collect] No matched. Create resource.')
                        #res_id = mgr.create_by_collector(data, collector_id, 'NEW')
                        res_msg = svc.create(data)


                        # TODO: push to Queue
                    elif total_count > 1:
                        # Ambiguous
                        _LOGGER.debug(f'[collect] Cannot determine. Too many resources matched. (count={total_count})')
                    elif total_count == 1 and len(res_info) == 1:
                        # Update
                        _LOGGER.debug('[collect] Matched. Update resource.')
                        # is_exist => VO
                        #res_id = mgr.update_by_collector(data, vo[0], collector_id, 'NEW')
                        data.update(res_info[0])
                        res_msg = svc.update(data)

                        # TODO: push to Queue

                except Exception as e:
                    # fail to identify resource
                    _LOGGER.warning(e)

        stat = {
                'state': 'SUCCESS',
                'collected_resources': resource_ids,
                'collect_mode': collect_mode
                }

        _LOGGER.debug(f'[collect] {stat}')
        job_vo = job_vo.update_collected_at(stat)

        # Update Collector
        self._update_collected_time(collector_id, datetime.utcnow(), domain_id)

        return job_vo

    ######################
    # Schedule
    ######################
    def add_schedule(self, params):
        """ Add schedule into DB

        Args:
            params:
                - domain_id
                - name
                - schedule
                - collector
                - collector_id
        """
        params = self._check_filter(params)

        def _rollback(scheduler_vo):
            _LOGGER.info(f'[ROLLBACK] Delete schedule : {scheduler_vo.collector_id}')
            scheduler_vo.delete()

        # Create DB first, for easy manipulation
        scheduler_vo: Scheduler = self.scheduler_model.create(params)
        self.transaction.add_rollback(_rollback, scheduler_vo)
        return scheduler_vo

    def list_schedulers(self, query):
        """ list schedules by query

        Args:
            params(dict)  
            
            example: {'filter': {'k': 'schedule.hour', 'v': 3, 'o': 'eq'}}

        Return: Collector
            collector model
        """
        return self.scheduler_model.query(**query)

    def update_scheduler(self, params):
        params = self._check_filter(params)

        scheduler_vo = self._get_scheduler(params['scheduler_id'], params['domain_id'])
        return self._update_scheduler_by_vo(params, scheduler_vo)

    def delete_scheduler(self, scheduler_id, domain_id):
        _LOGGER.debug(f'[delete_scheduler] scheduler_id: {scheduler_id}, domain_id: {domain_id}')
        scheduler_vo = self.scheduler_model.get(scheduler_id=scheduler_id, domain_id=domain_id)
        scheduler_vo.delete()

    def _get_scheduler(self, scheduler_id, domain_id):
        return self.scheduler_model.get(scheduler_id=scheduler_id, domain_id=domain_id)

    def _update_scheduler_by_vo(self, params, scheduler_vo):
        params = self._check_filter(params)
        def _rollback(old_data):
            _LOGGER.info(f'[ROLLBACK] Revert Scheduler Data : {old_data["scheduler_id"]}')
            scheduler_vo.update(old_data)

        self.transaction.add_rollback(_rollback, scheduler_vo.to_dict())
        return scheduler_vo.update(params)

    def delete_schedulers_by_collector_id(self, collector_id, domain_id):
        """ Delete all schedules related with collector
        """
        query = {
            'filter': [
                    {'k': 'collector_id', 'v': collector_id, 'o': 'eq'},
                    {'k': 'domain_id', 'v': domain_id, 'o': 'eq'}
            ]
        }
        scheduler_vos, total_count = self.list_schedulers(query)
        _LOGGER.debug(f'[delete_schedulers_by_collector_id] found: {total_count}')
        for scheduler_vo in scheduler_vos:
            _LOGGER.debug(f'[delete_schedulers_by_collector_id] delete scheduler: {scheduler_vo.scheduler_id}')
            self.delete_scheduler(scheduler_vo.scheduler_id, domain_id)


    ######################
    # Internal
    ######################
    def _check_filter(self, params):
        """ Schedule request may have filter
        Change filter -> filters, since mongodb does not support filter as member key
        """
        if 'filter' in params:
            params['filters'] = params['filter']
            del params['filter']
        return params


    def _get_updated_options(self, plugin_info, credentials, domain_id):
        """ Contact plugin, then get updated options
        
        Args:
            plugin_info: (vo object)
            credentials: (selected credential)
            domain_id

        Return: options(dict)
        """
        endpoint = self._get_endpoint(plugin_info, domain_id)
        connector = self.locator.get_connector('CollectorPluginConnector')
        connector.initialize(endpoint)

        options = plugin_info.options

        _LOGGER.debug('[_get_updated_options] old options: %s' % options)
        new_options = connector.verify(options, credentials)            # json type
        options.update(new_options['options'])
        _LOGGER.debug('[_get_updated_options] new options: %s' % options)
        return options

    def _get_endpoint(self, plugin_vo, domain_id):
        """ get endpoint from plugin_vo
        
        Args:
            plugin_vo (object)
                - plugin_id
                - version
                - options
                - credential_id
                - credential_group_id
            domain_id

        """
        # Call Plugin Service
        plugin_id = plugin_vo.plugin_id
        version = plugin_vo.version

        plugin_connector = self.locator.get_connector('PluginConnector')
        # TODO: label match
        endpoint = plugin_connector.get_plugin_endpoint(plugin_id, version, domain_id)
        return endpoint

    def _matched_credentials(self, plugin_info, domain_id, credential_id=None, filters=None):
        """ Get matched credential list
        filer: {'zone_id': 'zone-xxxxx'}

        Returns: matched list of credential_id
        """
#        cred_list = []
#        # plugin.credential_id
#        if plugin_info.credential_id != None:
#            cred_list.append(plugin_info.credential_id)
#        # plugin.credential_group_id
#        if plugin_info.credential_group_id != None:
#            cred_list = self._get_credentials_from_group(plugin_info.credential_group_id, domain_id)
#
        cred_list = self._get_credentials(plugin_info, domain_id)
        # as parameter
        if credential_id:
            cred_list.append(credential_id)
        matched_cred_list = []
        _LOGGER.debug('[_matched_credentials] cred_list: %s' % cred_list)
        # cred_id vs. filter
        for cred_id in cred_list:
            if self._match_filter(cred_id, filters, domain_id) == True:
                matched_cred_list.append(cred_id)
        _LOGGER.debug('[_matched_credentials] matched cred: %s' % matched_cred_list)
        return matched_cred_list

    def _match_filter(self, A, B, domain_id):
        """ determine A and B
        
        Args:
            A: credential_id
            B: filter(dict)
               ex) {'region_id':'region-xxx', 'zone_id':'zone-yyyy'}

        TODO: 
         - what is type of paramter
         - what is the definition of match

        Returns: True/False
        """
        _LOGGER.debug(f'[_match_filter] filters for cred: {B}')
        if B == None or B == {}:
            return True
        # B may be region_id | zone_id | pool_id

        #################
        # Credential(A)
        # X1: region_id
        # Y1: zone_id
        # Z1: pool_id
        ################
        cred_A = self._issue_credentials(A, domain_id)
        if 'region_id' in cred_A:
            X1 = cred_A['region_id']
            if 'zone_id' in cred_A:
                Y1 = cred_A['zone_id']
                if 'pool_id' in cred_A:
                    Z1 = cred_A['pool_id']
                else:
                    Z1 = None
            else:
                Y1 = None
                Z1 = None
        else:
            X1 = None
            Y1 = None
            Z1 = None
        ################
        # Filter(B)
        # X2: region_id
        # Y2: zone_id
        # Z2: pool_id
        ################
        if 'region_id' in B:
            X2 = B['region_id']
            if 'zone_id' in B:
                Y2 = B['zone_id']
                if 'pool_id' in B:
                    Z2 = B['pool_id']
                else:
                    Z2 = None
            else:
                Y2 = None
                Z2 = None
        else:
            X2 = None
            Y2 = None
            Z2 = None

        # X1 always exist
        _LOGGER.debug('[_match_filter] region_id:(%s vs. %s)' % (X1, X2))
        _LOGGER.debug('[_match_filter] zone_id:  (%s vs. %s)' % (Y1, Y2))
        _LOGGER.debug('[_match_filter] pool_id:  (%s vs. %s)' % (Z1, Z2))

        if X2 == None and Y2 == None and Z2 == None:
            return True

        if X1 != None and X2 != None and X1 != X2:
            _LOGGER.debug('[_match_filter] False at Zone')
            return False

        if Y1 != None and Y2 != None and Y1 != Y2:
            _LOGGER.debug('[_match_filter] False at Region')
            return False

        if Z1 != None and Z2 != Zone and Z1 != Z2:
            _LOGGER.debug('[_match_filter] False at Pool')
            return False

        _LOGGER.debug('[_match_filter] Matched: True')
        return True

    def _get_all_credentials(self, plugin_info, domain_id):
        """ Get credential_id for verify
        
        Return: credential_id
        """
        try:
            cred_id = plugin_info.credential_id
            if cred_id:
                return self._issue_credentials(cred_id, domain_id)
            # credential_group_id
            cred_group_id = plugin_info.credential_group_id
            creds = self._get_credentials_from_group(cred_group_id, domain_id)
            cred_id = random.choice(creds)
            return self._issue_credentials(cred_id, domain_id)
        except Exception as e:
            _LOGGER.error("[_get_all_credentials] Failed to retrieve credential from plugin_info")
            _LOGGER.debug(e)
            # TODO: ?
            return None

    def _update_collected_time(self, collector_id, timestamp, domain_id):
        """ Update last_updated_time of collector
        """
        collector_vo = self.get_collector(collector_id, domain_id)
        params = {'last_collected_at': timestamp}
        self.update_collector_by_vo(collector_vo, params)


    ###############################
    # filter
    ###############################
    def _get_collector_filter(self, filters, filter_format):
        """ Create new filters for Collect plugin's parameter
            filter_format(filters) -> new_filter

        Args:
            filter_format(list): filter_format from plugin.options.filter_format or None
            filters(dict): filters from Client request

        Returns:
            new_filter: new filters for Plugin(Collector) query

        Example:
            filter_format:
                'filter_format': [
                    {'key':'region_id', 'name':'Region', 'type':'str', 'resource_type': 'SERVER', 'change_key': ['data.compute.instance_id', 'instance_id']},
                    {'key':'zone_id', 'name':'Zone', 'type':'str', 'resource_type': 'SERVER', 'change_key': ['data.compute.instance_id', 'instance_id']},
                    {'key':'pool_id', 'name':'Pool', 'type':'str', 'resource_type': 'SERVER', 'change_key': ['data.compute.instance_id', 'instance_id']},
                    {'key':'server_id', 'name':'Server', 'type':'list', 'resource_type': 'SERVER', 'object_key': 'uuid', 'change_key': ['data.compute.instance_id', 'instance_id']},
                    {'key':'instance_id', 'name':'Instance ID', 'type':'list', 'resource_type': 'CUSTOM'},
                ]

            filters:
                {
                    'region_id': 'region-xxxxx',
                    'zone_id': 'zone-yyyyy',
                    'instance_id': ['i-zzzz', ...]]            # CUSTOM resource type
                }

            new_filter:
                {
                    'instance_id': ['i-123', 'i-2222', ...]
                }
        """
        if filters == None:
            return {}

        _dic = {}

        # TODO: check_filter_format, such as resource_type
        for item in filter_format:
            _dic[item['key']] = item

        # Returned filter = result
        result = {}

        _flt_dic = {}
        """
        'region_id': [{'k': 'region_id', 'v': 'region-xxx', 'o': 'eq'}]
        'server_id': [{'k': 'server_id', 'v': 'server-yyyy', 'o': 'eq'} ....]
        ...
        """
        custom_keys = []
        # Foreach filter, we will find matched resource list
        for k,v in filters.items():
            # k : region_id
            filter_element = _dic.get(k, None)
            _LOGGER.debug(f'[_get_collector_filter] filter_element: {filter_element}')
            if _dic[k]['resource_type'] == 'CUSTOM':
                # DO NOT save CUSTOM key at _flt_dic
                custom_keys.append(k)
                continue

            # list of new_filter[key]
            v_list = _flt_dic.get(k, [])
            if filter_element:
                # Ask to manager, is there any matched resource
                query = self._make_query_for_manager(k, v, filter_element)
                if isinstance(query, list) == False:
                    _LOGGER.error("LOGIC ERROR, _make_query_for_manager does not return list value: {query}")
                else:
                    v_list.extend(query)
            _flt_dic[k] = v_list

        # Make query per Resource
        query_per_res = {}
        """
        'SERVER': {
            'filter': [{'k': 'region_id', 'v': 'region-xxxx', 'o': 'eq'}], 
            'filter_or': [{'k': 'server_id', 'v': 'server-yyyy', 'o': 'eq'}, ...]
            }
        """
        for k, query in _flt_dic.items():
            res_type = _dic[k]['resource_type']
            query_string = query_per_res.get(res_type, {'key': k, 'filter': [], 'filter_or': []})
            if len(query) == 1:
                query_string['filter'].extend(query)
            elif len(query) > 1:
                query_string['filter_or'].extend(query)
            else:
                _LOGGER.debug(f'[_get_collector_filter] wrong query: {query}')
            query_per_res[res_type] = query_string

        # Search Resource by Resource's Manager
        _LOGGER.debug(f'[_get_collector_filter] query_per_res: {query_per_res}')
        for res_type, query in query_per_res.items():
            """ Example
            query: {'key': 'zone_id', 
                    'filter': [
                            {'k': 'zone_id', 'v': 'zone-d710c1cb0ea7', 'o': 'eq'}, 
                            {'k': 'region_id', 'v': 'region-85445849c20c', 'o': 'eq'}, 
                            {'k': 'pool_id', 'v': 'pool-a1f35b107bb4', 'o': 'eq'}], 
                    'filter_or': []}
            """
            _LOGGER.debug(f'[_get_collector_filter] query: {query}')
            try:
                mgr = self.locator.get_manager(RESOURCE_MAP[res_type])
            except Exception as e:
                _LOGGER.error('################## NOTICE to Developer (bug) ###################################')
                _LOGGER.error(f'[_get_collector_filter] Not found manager based on resource_type: {res_type}')
                _LOGGER.error(e)
                continue

            flt_elt = _dic[query['key']]
            change_key = flt_elt['change_key']
            del query['key']

            # Ask to manager
            try:
                results, count = mgr.query_resources(query, vo=True)
            except Exception as e:
                _LOGGER.error('################## NOTICE to Developer (bug) #######################################')
                _LOGGER.error(f'{res_type} Manager has bug for query_resources functions')
                _LOGGER.error(e)
                results = []

            value_list = []
            for res in results:
                changed_value = self._get_value_from_vo(res, change_key[0])
                if changed_value:
                    value_list.append(changed_value)
                else:
                    _LOGGER.debug(f'Check Resource {res}')
                
            # Make new query
            if len(value_list) > 0:
                result.update({change_key[1]: value_list})
     
        for custom_key in custom_keys:
            _LOGGER.debug(f'[_get_collector_filter] append custom_key: {custom_key}')
            values = filters[custom_key]
            if type(values) is not type([]):
                values = [values]
            v = result.get(custom_key, [])
            v.extend(values)
            result[custom_key] = v

        return result

    def _get_value_from_vo(self, vo, key):
        """
        Get value from VO which location is key
        
        Args:
            vo: Value Object
            key(str): location of value (ex. data.compute.instance_id)

        Returns:
            value
        """
        _LOGGER.debug(f'[_get_value_from_vo] find {key} at data')
        # Change to Dictionary
        # find at dictionary
        vo_dict = vo.to_dict()
        key_items = key.split('.')
        if 'data' in vo_dict:
            res = vo_dict['data']
            for idx in key_items[1:]:
                if idx in res:
                    res = res[idx]
            return res
        _LOGGER.debug('################## NOTICE to Developer (may be Plugin Bug) #######################')
        _LOGGER.debug(f'[_get_value_from_vo] key: {key}, data: {vo_dict}')
        _LOGGER.warning(f'[_get_value_from_vo] change_key: {key}, scope is not data')

    def _make_query_for_manager(self, key, value, filter_element):
        """
        Args:
            key(str): key for query
            value: query value of element (str, int, bool, float, list)
            filter_element(dict): one element for filter_format

        Returns:
            query_statement (list, since there are list type)

        Example)
            value: region-xxxxx
            filter_element: {'key':'region_id', 'name':'Region', 'type':'str', 'resource_type': 'SERVER', 'change_key': ['data.compute.instance_id', 'instance_id']}
        """
        query_list = []

        f_type = filter_element['type']
        if f_type == 'list':
            values = value
        else:
            values = [value]
        for val in values:
            query_list.append({'k': key, 'v': val, 'o': 'eq'})

        return query_list

        
    ###############################
    # Credential/CredentialGroup
    ###############################
    def _issue_credentials(self, credential_id, domain_id):
        """ Return secret data
        """
        connector = self.locator.get_connector('SecretConnector')
        cred = connector.issue_credentials(credential_id, domain_id)
        _LOGGER.debug('[_issue_credentials] cred: %s' % cred)
        return cred.secret

    def _get_credentials_from_group(self, credential_group_id, domain_id):
        """ Return list of credential_id
        """
        connector = self.locator.get_connector('SecretConnector')
        cred_group_info = connector.get_credential_group(credential_group_id, domain_id)
        #return cred_group_info.credentials
        result = []
        # credential_group_id, find credentials
        cred_grp_id = cred_group_info.credential_group_id

        creds_info = self._get_credentials_by_cred_grp_id(cred_grp_id, domain_id)
        for cred in creds_info.results:
            result.append(cred.credential_id)
        return result

    def _get_credentials(self, plugin_info, domain_id):
        """ Return list of crednetial_ids

        Args:
            plugin_info(dict)

        """
        cred_id_list = []
        if 'credential_id' in plugin_info:
            cred_id_list.append(plugin_info['credential_id'])
        if 'credential_group_id' in plugin_info:
            creds = self._get_credentials_by_cred_grp_id(plugin_info['credential_group_id'], domain_id)
            for cred in creds.results:
                cred_id_list.append(cred.credential_id)

        return cred_id_list

    def _get_credentials_by_cred_grp_id(self, cred_grp_id, domain_id):
        connector = self.locator.get_connector('SecretConnector')
        return connector.list_credentials_by_cred_grp_id(cred_grp_id, domain_id) 

    ################################
    # Queue
    ################################
#    def _create_command(self, result):
#        command = {
#            'timestamp': time.time(),
#            'request': {
#                'api_class': api_class,
#                'method': method,
#                'params': {}
#                'metadata': self.transaction.get_meta()
#                }
#            }
#        return command

    def query_with_match_rules(self, resource, match_rules, domain_id, mgr):
        """ match resource based on match_rules

        Args:
            resource: ResourceInfo(Json) from collector plugin
            match_rules:
                ex) {1:['data.vm.vm_id'], 2:['zone_id', 'data.ip_addresses']}
        
        Return:
            resource_id : resource_id for resource update (ex. {'server_id': 'server-xxxxxx'})
            True: can not determine resources (ambiguous)
            False: no matched
        """

        found_resource = None
        total_count = 0

        match_rules = rule_matcher.dict_key_int_parser(match_rules)

        match_order = match_rules.keys()

        for order in sorted(match_order):
            query = rule_matcher.make_query(order, match_rules, resource, domain_id)
            _LOGGER.debug(f'[query_with_match_rules] query generated: {query}')
            found_resource, total_count = mgr.query_resources(query)
            if found_resource and total_count == 1:
                return found_resource, total_count

        return found_resource, total_count

           
