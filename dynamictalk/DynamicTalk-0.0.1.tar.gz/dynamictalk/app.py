import copy
import json
from typing import List, Tuple, Any, Optional, Dict

import xmltodict
import zeep
from netsuite.client import NetSuite

from . import types, sub_types, util


class DynamicTalk:

    def __init__(self, client: NetSuite = None):
        self.client = client

    #TODO: add all object types
    def _get_object_sub_type(self, object_name:str) -> str:
        '''returns the object_sub_type based on which object sub type list the object name is in
        '''
        last4 = object_name[-4:]
        name = object_name[:-4] if last4 == 'Item' else object_name
        if name in sub_types.SALES:
            return 'sales'
        elif name in sub_types.RELATIONSHIPS:
            return 'relationships'
        elif name in sub_types.PURCHASES:
            return 'purchases'
        elif name in sub_types.ACCOUNTING:
            return 'accounting'
        elif name in sub_types.COMMON:
            return 'common'
        elif name in sub_types.CORE:
            return 'core'
        else:
            raise Exception(f'unable to determine the object sub type (self.object_sub_type) based on the object name: {object_name}')

    #TODO: add all object types
    def _get_object_type(self, object_sub_type:str) -> str:
        '''returns the object_type based on which _object_type property list object_sub_type is in
        '''
        if object_sub_type in types.TRANSACTIONS:
            return 'transactions'
        elif object_sub_type in types.LISTS:
            return 'lists'
        elif object_sub_type in types.PLATFORM:
            return 'platform'
        else:
            raise Exception(f'unable to determine the object type (self.object_type) based on the object sub type: {object_sub_type}')

    def return_object_types(self, object_name:str) -> Tuple[str, str]:
        '''returns the object sub type and type based on the objects name
        '''
        object_sub_type = self._get_object_sub_type(object_name)
        object_type = self._get_object_type(object_sub_type)
        return object_sub_type, object_type

    def _get_prefix(self, object_name:str) -> str: #e.g. ns0
        '''gets the correct namespace abbreviation for an object based on the object name
        '''
        object_sub_type, object_type = self.return_object_types(object_name)
        namespace = self.client._get_namespace(object_sub_type, object_type)
        namespaces = self.client.client.wsdl.types.prefix_map.items()
        return [key for (key,value) in namespaces if value == namespace][0]

    def get_type(self, object_name:str) -> zeep.xsd.ComplexType:
        '''returns the correct zeep structure from the wsdl based on the object name
        '''
        object_name = util.capitalize_first_letter(object_name)
        location = f'{self._get_prefix(object_name)}:{object_name}'
        return self.client.client.get_type(location)

    #TODO: add all custom field types
    def _get_custom_field_struct(self, type_name) -> Any:
        '''takes the custom field type name returned in the get custom field call and returns the appropriate zeep structure for it
        '''
        string = ['_eMailAddress', '_freeFormText', '_hyperlink', '_longText', '_document', '_textArea']
        long = []
        double = ['_decimalNumber', '_integerNumber', '_percent']
        boolean = ['_checkBox']
        date = ['_datetime', '_date']
        select = ['_currency', '_listRecord']
        multi = ['_multipleSelect']
        if type_name in string:
            return self.client.Core.StringCustomFieldRef()
        elif type_name in long:
            return self.client.Core.LongCustomFieldRef()
        elif type_name in double:
            return self.client.Core.DoubleCustomFieldRef()
        elif type_name in boolean:
            return self.client.Core.BooleanCustomFieldRef()
        elif type_name in date:
            return self.client.Core.DateCustomFieldRef()
        elif type_name in select:
            cust_ref = self.client.Core.SelectCustomFieldRef()
            cust_ref.value = self.client.Core.ListOrRecordRef()
            return cust_ref
        elif type_name in multi:
            multi_ref = self.client.Core.MultiSelectCustomFieldRef()
            multi_ref.value = [self.client.Core.ListOrRecordRef()]
            return multi_ref
        else:
            raise Exception(f'There is no custom field structure specified for {type_name}')

    def _get_customization_type(self, cust_field_list_type) -> Any:
        '''makes a call to Netsuite and returns all of the custom fields for a certain custom field list type
        '''
        customization_type = self.client.Core.CustomizationType()
        customization_type.getCustomizationType = self.client.CoreTypes.GetCustomizationType(cust_field_list_type)
        return self.client.request('getCustomizationId', customization_type, False)['body']['getCustomizationIdResult']['customizationRefList']['customizationRef']

    #TODO: add all custom field types
    def _get_custom_field_list(self, object_name:str) -> str:
        '''returns the name of the appropriate custom field list based on the name of the object the custom field list is for
        '''
        __, object_type = self.return_object_types(object_name)
        if object_type == 'transactions':
            if 'item' in object_name.lower():
                return 'transactionColumnCustomField'
            else:
                return 'transactionBodyCustomField'
        elif object_type == 'lists':
            return 'entityCustomField'
        elif object_type == 'platform':
            return 'otherCustomField'
        else:
            raise Exception(f'{object_name} is not mapped')
    
    def _build_custom_field_struct(self, custom_field_data:dict) -> Any:
        '''returns the appropriate custom field structure populated with its identifiers based on the custom field info returned by the get call for a customization type
        '''
        record = custom_field_data['record']
        structure = self._get_custom_field_struct(record['setupCustom:fieldType'])
        structure.scriptId = record['setupCustom:scriptId']
        structure.name = record['setupCustom:label']
        structure.internalId = record['@internalId']
        return structure

    def _build_custom_field_list_struct(self, custom_fields_data) -> List[Any]:
        '''returns a list of zeep structured custom fields with identifiers based on the custom field data passed in from a get/getList call for a customization type
        '''
        custom_field = []
        #the response with the custom field data from Netsuite will be a list if there is more than one custom field, but a dictionary if there is only one custom field. This identifies what the case is and converts the data depending
        if type(custom_fields_data) == list:
            for field in custom_fields_data:
                custom_field.append(self._build_custom_field_struct(field))
        else:
            custom_field.append(self._build_custom_field_struct(custom_fields_data))
        return custom_field

    def _view_custom_field_list(self, object_name:str) -> Any:
        '''returns the built out zeep custom field list with correct custom field type sturctures based on the object that the custm list is for
        '''
        cust_field_list_type = self._get_custom_field_list(object_name)
        if cust_field_list_type:
            custom_field_list = self.client.Core.CustomFieldList()
            internal_ids = []
            cust_fields = self._get_customization_type(cust_field_list_type)
            for field in cust_fields:
                cust_field_ref = self.client.Core.RecordRef(
                                    internalId=field['internalId'],
                                    type=cust_field_list_type
                                    )
                internal_ids.append(cust_field_ref)
            #the netsuite wsdl for this request is incorrect, so the setting to return the raw response has to be enabled and the raw response has to be parsed
            with self.client.client.settings(raw_response=True):
                xml_custom_field_info = self.client.request('getList', internal_ids).content
            dict_custom_field_info = json.loads(json.dumps(xmltodict.parse(xml_custom_field_info)))
            custom_field_info = dict_custom_field_info['soapenv:Envelope']['soapenv:Body']['getListResponse']['readResponseList']['readResponse']
            custom_field = self._build_custom_field_list_struct(custom_field_info)
            custom_field_list.customField = custom_field
            return custom_field_list
        else:
            raise Exception(f'not able to find a custom field list type from object name: {object_name}')

    def _view_object(self, zeep_structure) -> Optional[List[Any]]:
        '''returns the entire built out zeep strucutre for an object with all sub objects and custom field lists
        '''
        try:
            zeep_object = zeep_structure()
        except Exception as e:
            if 'Simple types expect only a single value argument' in str(e):
                return None
            else:
                raise
        for element in zeep_structure.elements:
            value = None
            if element[1].name == 'customFieldList':
                value = self._view_custom_field_list(zeep_structure.name)
            else:
                value = self._view_object(self.client.client.get_type(element[1].type.qname))
            if type(zeep_object[element[0]]) == list:
                #if the list value is structured put the structure in a list else set the value to an empty list
                if value:
                    value = [value]
                else: 
                    value = []
            zeep_object[element[0]] = value
        return zeep_object

    def _convert_custom_field_list_to_zeep(self,
                                           custom_field_data:dict,
                                           zeep_custom_field_list
                                           ) -> List[Any]:
        custom_field_list = []
        for key, value in custom_field_data.items():
            if value != None:
                custom_field_struct = next((cf for cf in zeep_custom_field_list if cf['scriptId'].find(key) > -1), None)
                if custom_field_struct:
                    if custom_field_struct.value:
                        #if it is a multi select field
                        if type(custom_field_struct.value) == list:
                            custom_field_value_struct = custom_field_struct.value.pop(0)
                            if type(value) == list:
                                for item in value:
                                    struct = copy.deepcopy(custom_field_value_struct)
                                    struct.internalId = item
                                    custom_field_struct.value.append(struct)
                            else:
                                custom_field_value_struct.internalId = value
                                custom_field_struct.value.append(custom_field_value_struct)
                        else:
                            custom_field_struct.value.internalId = value
                    else:
                        custom_field_struct.value = value
                    custom_field_list.append(custom_field_struct)
        return custom_field_list

    @util.memoize_ignore_self
    def _get_custom_field_list_struct(self, cust_field_list_type: str) -> List[dict]:
        internal_ids = []
        cust_fields = self._get_customization_type(cust_field_list_type)
        for field in cust_fields:
            cust_field_ref = self.client.Core.RecordRef(
                                internalId=field['internalId'],
                                type=cust_field_list_type
                                )
            internal_ids.append(cust_field_ref)
        #the netsuite wsdl for this request is incorrect, so the setting to return the raw response has to be enabled and the raw response has to be parsed
        with self.client.client.settings(raw_response=True):
            xml_custom_field_info = self.client.request('getList', internal_ids).content
        dict_custom_field_info = json.loads(json.dumps(xmltodict.parse(xml_custom_field_info)))
        custom_field_info = dict_custom_field_info['soapenv:Envelope']['soapenv:Body']['getListResponse']['readResponseList']['readResponse']
        return self._build_custom_field_list_struct(custom_field_info)

    def _build_custom_field_list(self, object_name:str, data:dict) -> List[Any]:
        cust_field_list_type = self._get_custom_field_list(object_name)
        if cust_field_list_type:
            custom_field_list = self.client.Core.CustomFieldList()
            custom_field_list_struct = self._get_custom_field_list_struct(cust_field_list_type)
            custom_field_list.customField = self._convert_custom_field_list_to_zeep(data, custom_field_list_struct)
            return custom_field_list
        else:
            raise Exception(f'not able to find a custom field list type from object name: {object_name}')

    def _build_component(self, component, data, zeep_structure) -> Any:
        el = component[1]
        value = data.get(str(el.name))
        if value != None:
            print(value)
            print(el.name)
            if el.name == 'customFieldList':
                #the custom field list has a sub structure that contains the actual list called customField. If that key is present ignore it as it will be added in automatically.
                if type(value) == dict and value.get('customField'):
                    value = value['customField']
                value = self._build_custom_field_list(zeep_structure.name, value)
            elif type(value) == dict:
                value = self._build_object(self.client.client.get_type(el.type.qname), data[el.name])
            elif type(value) == list:
                ind_lst = el.name.find('List')
                if ind_lst > 0:
                    structure = self.client.client.get_type(el.type.qname)
                    list_sub_object_name = el.name[:ind_lst]
                    value = structure()
                    item_struct = self.client.client.get_type(structure.elements[0][1].type.qname)
                else:
                    item_struct = self.client.client.get_type(el.type.qname)
                items = []
                for item in data[el.name]:
                    struct_value = self._build_object(item_struct, item)
                    items.append(struct_value if struct_value else item)
                #netsuite lists have a sub structure that the list lives in. It has the same name as the list, but without the 'List' at the end. e.g. 'itemList': {'item': []}. This gets the name of that sub structure.
                if ind_lst > 0:
                    value[list_sub_object_name] = items
                else:
                    value = items
            else:
                struct_value = self._build_object(self.client.client.get_type(el.type.qname), {'internalId':value})
                value = struct_value if struct_value else value
            return value
        return None

    def _build_object(self, zeep_structure, data) -> Optional[Any]:
        try:
            zeep_object = zeep_structure()
        except Exception as e:
            if 'Simple types expect only a single value argument' in str(e):
                return None
            else:
                raise
        zeep_components = zeep_structure.elements + zeep_structure.attributes
        for component in zeep_components:
            zeep_object[component[0]] = self._build_component(component, data, zeep_structure)
        return zeep_object

    def view(self, object_name: str) -> Any:
        zeep_structure = self.get_type(object_name)
        return self._view_object(zeep_structure)

    def build(self, object_name: str, data: dict) -> Any:
        zeep_structure = self.get_type(object_name)
        return self._build_object(zeep_structure, data) 
