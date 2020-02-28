import unittest
import os
import json
from typing import Dict, Any

from schemaparser import SchemaParser
from converter import SchemaConverter, Class, Command, ClassType, Attribute


class TestConverterForClasses(unittest.TestCase):
    def test_class_with_primitives(self):
        REQUIRED_FILES = ['APITypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        schema_folder = os.path.join(script_path, 'APICommandJSONSchema', 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)
        self.assertTrue(converter.classes)
        self.assertFalse(converter.commands)

        PUBLISHERSETID_CLASS: Class = converter.classes[converter.classes.index('PublisherSetId')]
        self.assertEqual(PUBLISHERSETID_CLASS.name, 'PublisherSetId')
        self.assertEqual(PUBLISHERSETID_CLASS.description, 'The identifier of a publisher set.')
        self.assertEqual(PUBLISHERSETID_CLASS.class_type, ClassType.NORMAL)
        self.assertIsNone(PUBLISHERSETID_CLASS.title)
        self.assertIsNone(PUBLISHERSETID_CLASS.default)
        self.assertEqual(PUBLISHERSETID_CLASS.additional_properties, False)
        self.assertTrue(PUBLISHERSETID_CLASS.attributes)
        
        FIRST_ATTRIBUTE = PUBLISHERSETID_CLASS.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE.name, 'type')
        self.assertEqual(FIRST_ATTRIBUTE.description, 'Type of the navigator item tree.')
        self.assertEqual(FIRST_ATTRIBUTE.type, 'str')
        self.assertEqual(FIRST_ATTRIBUTE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE.min_length)
        self.assertIsNone(FIRST_ATTRIBUTE.max_length)
        self.assertIsNone(FIRST_ATTRIBUTE.pattern)
        self.assertTrue(FIRST_ATTRIBUTE.values)
        self.assertEqual(len(FIRST_ATTRIBUTE.values), 1)
        self.assertIn('PublisherSets', FIRST_ATTRIBUTE.values)

        SECOND_ATTRIBUTE = PUBLISHERSETID_CLASS.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE.name, 'name')
        self.assertEqual(SECOND_ATTRIBUTE.description, 'Name of the publisher set.')
        self.assertEqual(SECOND_ATTRIBUTE.type, 'str')
        self.assertEqual(SECOND_ATTRIBUTE.required, True)
        self.assertIsNone(SECOND_ATTRIBUTE.min_length)
        self.assertIsNone(SECOND_ATTRIBUTE.max_length)
        self.assertIsNone(SECOND_ATTRIBUTE.pattern)
        self.assertIsNone(SECOND_ATTRIBUTE.values)


    def test_class_with_array(self):
        REQUIRED_FILES = ['APITypes.json', 'APIPropertyTypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        schema_folder = os.path.join(script_path, 'APICommandJSONSchema', 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)
        self.assertTrue(converter.classes)
        self.assertFalse(converter.commands)

        PUBLISHERSETID_CLASS: Class = converter.classes[converter.classes.index('UserDefinedPropertyUserId')]
        self.assertEqual(PUBLISHERSETID_CLASS.name, 'UserDefinedPropertyUserId')
        self.assertEqual(PUBLISHERSETID_CLASS.description, 'An object which uniquely identifies a User-Defined Property by its name in human-readable form.')
        self.assertEqual(PUBLISHERSETID_CLASS.class_type, ClassType.NORMAL)
        self.assertIsNone(PUBLISHERSETID_CLASS.title)
        self.assertIsNone(PUBLISHERSETID_CLASS.default)
        self.assertEqual(PUBLISHERSETID_CLASS.additional_properties, False)
        self.assertTrue(PUBLISHERSETID_CLASS.attributes)
        
        FIRST_ATTRIBUTE = PUBLISHERSETID_CLASS.attributes[0]
        self.assertEqual(FIRST_ATTRIBUTE.name, 'type')
        self.assertIsNone(FIRST_ATTRIBUTE.description)
        self.assertEqual(FIRST_ATTRIBUTE.type, 'str')
        self.assertEqual(FIRST_ATTRIBUTE.required, True)
        self.assertIsNone(FIRST_ATTRIBUTE.min_length)
        self.assertIsNone(FIRST_ATTRIBUTE.max_length)
        self.assertIsNone(FIRST_ATTRIBUTE.pattern)
        self.assertTrue(FIRST_ATTRIBUTE.values)
        self.assertEqual(len(FIRST_ATTRIBUTE.values), 1)
        self.assertIn('UserDefined', FIRST_ATTRIBUTE.values)

        SECOND_ATTRIBUTE = PUBLISHERSETID_CLASS.attributes[1]
        self.assertEqual(SECOND_ATTRIBUTE.name, 'localizedName')
        self.assertEqual(SECOND_ATTRIBUTE.description, 'List of the localized name parts: first element is the Group Name, second element is the Property Name of the Property.')
        self.assertEqual(SECOND_ATTRIBUTE.type, 'List')
        self.assertEqual(SECOND_ATTRIBUTE.required, True)
        self.assertEqual(SECOND_ATTRIBUTE.min_items, 2)
        self.assertEqual(SECOND_ATTRIBUTE.max_items, 2)
        self.assertIsNone(SECOND_ATTRIBUTE.unique_items)
        self.assertEqual(SECOND_ATTRIBUTE.itemtype.name, 'ListItem')
        self.assertEqual(SECOND_ATTRIBUTE.itemtype.type, 'str')
        self.assertIsNone(SECOND_ATTRIBUTE.itemtype.description)
        self.assertEqual(SECOND_ATTRIBUTE.itemtype.required, False)
        self.assertIsNone(SECOND_ATTRIBUTE.itemtype.min_length)
        self.assertIsNone(SECOND_ATTRIBUTE.itemtype.max_length)
        self.assertIsNone(SECOND_ATTRIBUTE.itemtype.pattern)
        self.assertIsNone(SECOND_ATTRIBUTE.itemtype.values)

    def test_class_with_object(self):
        REQUIRED_FILES = ['APITypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        schema_folder = os.path.join(script_path, 'APICommandJSONSchema', 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)
        self.assertTrue(converter.classes)
        self.assertFalse(converter.commands)

        ELEMENTIDARRAYITEM_CLASS = converter.classes[converter.classes.index('ElementIdArrayItem')]
        self.assertEqual(ELEMENTIDARRAYITEM_CLASS.name, 'ElementIdArrayItem')
        self.assertFalse(ELEMENTIDARRAYITEM_CLASS.description)
        self.assertEqual(ELEMENTIDARRAYITEM_CLASS.class_type, ClassType.NORMAL)
        self.assertIsNone(ELEMENTIDARRAYITEM_CLASS.title)
        self.assertIsNone(ELEMENTIDARRAYITEM_CLASS.default)
        self.assertEqual(ELEMENTIDARRAYITEM_CLASS.additional_properties, False)
        ELEMENTID_CLASS = converter.classes[converter.classes.index(ELEMENTIDARRAYITEM_CLASS.attributes[0].type)]
        self.assertEqual(ELEMENTID_CLASS.name, 'ElementId')
        self.assertEqual(ELEMENTID_CLASS.description, 'The identifier of an element.')
        self.assertEqual(ELEMENTID_CLASS.class_type, ClassType.NORMAL)
        self.assertIsNone(ELEMENTID_CLASS.title)
        self.assertIsNone(ELEMENTID_CLASS.default)
        self.assertEqual(ELEMENTID_CLASS.additional_properties, False)
        self.assertEqual(ELEMENTID_CLASS.attributes[0].name, 'guid')
        self.assertEqual(ELEMENTID_CLASS.attributes[0].type, 'UUID')
        self.assertEqual(ELEMENTID_CLASS.attributes[0].description, 'A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.')
        self.assertEqual(ELEMENTID_CLASS.attributes[0].pattern, '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')

    def test_class_with_one_of(self):
        REQUIRED_FILES = ['APITypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        schema_folder = os.path.join(script_path, 'APICommandJSONSchema', 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)
        self.assertTrue(converter.classes)
        self.assertFalse(converter.commands)

        BOUNDINGBOX2DORERROR_CLASS = converter.classes[converter.classes.index('BoundingBox2DOrError')]
        self.assertEqual(BOUNDINGBOX2DORERROR_CLASS.name, 'BoundingBox2DOrError')
        self.assertEqual(BOUNDINGBOX2DORERROR_CLASS.description, 'A 2D bounding box or error.')
        self.assertEqual(BOUNDINGBOX2DORERROR_CLASS.class_type, ClassType.ONEOF)
        self.assertIsNone(BOUNDINGBOX2DORERROR_CLASS.title)
        self.assertIsNone(BOUNDINGBOX2DORERROR_CLASS.default)
        self.assertIsNone(BOUNDINGBOX2DORERROR_CLASS.additional_properties)

        FIRST_TYPE: Class = converter.classes[converter.classes.index(BOUNDINGBOX2DORERROR_CLASS.attributes[0].type)]
        self.assertEqual(FIRST_TYPE.name, 'BoundingBox2DWrapper')
        self.assertFalse(FIRST_TYPE.description)
        self.assertEqual(FIRST_TYPE.class_type, ClassType.NORMAL)
        self.assertEqual(FIRST_TYPE.title, 'boundingBox2D')
        self.assertIsNone(FIRST_TYPE.default)
        self.assertEqual(FIRST_TYPE.additional_properties, False)
        self.assertTrue(FIRST_TYPE.attributes)
        self.assertTrue(len(FIRST_TYPE.attributes) == 1)
        self.assertEqual(FIRST_TYPE.attributes[0].name, 'boundingBox2D')
        FIRST_WRAPPED_CLASS: Class = converter.classes[converter.classes.index(FIRST_TYPE.attributes[0].type)]
        self.assertEqual(FIRST_WRAPPED_CLASS.name, 'BoundingBox2D')
        self.assertEqual(FIRST_WRAPPED_CLASS.description, '2D bounding box of an element.')
        self.assertEqual(FIRST_WRAPPED_CLASS.class_type, ClassType.NORMAL)
        self.assertIsNone(FIRST_WRAPPED_CLASS.default)
        self.assertEqual(FIRST_WRAPPED_CLASS.additional_properties, False)
        self.assertTrue(FIRST_WRAPPED_CLASS.attributes)
        self.assertTrue(len(FIRST_WRAPPED_CLASS.attributes) == 4)
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[0].name, 'xMin')
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[0].type, 'float')
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[0].description, 'Minimum X value of bounding box.')
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[0].required, True)
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[1].name, 'yMin')
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[1].type, 'float')
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[1].description, 'Minimum Y value of bounding box.')
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[1].required, True)
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[2].name, 'xMax')
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[2].type, 'float')
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[2].description, 'Maximum X value of bounding box.')
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[2].required, True)
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[3].name, 'yMax')
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[3].type, 'float')
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[3].description, 'Maximum Y value of bounding box.')
        self.assertEqual(FIRST_WRAPPED_CLASS.attributes[3].required, True)

        SECOND_TYPE: Class = converter.classes[converter.classes.index(BOUNDINGBOX2DORERROR_CLASS.attributes[1].type)]
        self.assertEqual(SECOND_TYPE.name, 'ErrorWrapper')
        self.assertFalse(SECOND_TYPE.description)
        self.assertEqual(SECOND_TYPE.class_type, ClassType.NORMAL)
        self.assertEqual(SECOND_TYPE.title, 'error')
        self.assertIsNone(SECOND_TYPE.default)
        self.assertEqual(SECOND_TYPE.additional_properties, False)
        self.assertTrue(SECOND_TYPE.attributes)
        self.assertTrue(len(SECOND_TYPE.attributes) == 1)
        self.assertEqual(SECOND_TYPE.attributes[0].name, 'error')
        SECOND_WRAPPED_CLASS: Class = converter.classes[converter.classes.index(SECOND_TYPE.attributes[0].type)]
        self.assertEqual(SECOND_WRAPPED_CLASS.name, 'Error')
        self.assertEqual(SECOND_WRAPPED_CLASS.description, 'Error details.')
        self.assertEqual(SECOND_WRAPPED_CLASS.class_type, ClassType.NORMAL)
        self.assertIsNone(SECOND_WRAPPED_CLASS.default)
        self.assertEqual(SECOND_WRAPPED_CLASS.additional_properties, False)
        self.assertTrue(SECOND_WRAPPED_CLASS.attributes)
        self.assertTrue(len(SECOND_WRAPPED_CLASS.attributes) == 2)
        self.assertEqual(SECOND_WRAPPED_CLASS.attributes[0].name, 'code')
        self.assertEqual(SECOND_WRAPPED_CLASS.attributes[0].type, 'int')
        self.assertEqual(SECOND_WRAPPED_CLASS.attributes[0].description, 'The error code.')
        self.assertEqual(SECOND_WRAPPED_CLASS.attributes[0].required, True)
        self.assertEqual(SECOND_WRAPPED_CLASS.attributes[1].name, 'message')
        self.assertEqual(SECOND_WRAPPED_CLASS.attributes[1].type, 'str')
        self.assertEqual(SECOND_WRAPPED_CLASS.attributes[1].description, 'The error message.')
        self.assertEqual(SECOND_WRAPPED_CLASS.attributes[1].required, True)
        
class TestConverterForCommands(unittest.TestCase):
    def test_getter_command(self):
        REQUIRED_FILES = ['API.GetProductInfo.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        schema_folder = os.path.join(script_path, 'APICommandJSONSchema', 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)
        self.assertFalse(converter.classes)
        self.assertTrue(converter.commands)

        COMMAND: Command = converter.commands[0]
        self.assertEqual(COMMAND.name, 'GetProductInfo')
        self.assertEqual(COMMAND.description, 'Accesses the version information from the running ARCHICAD.')
        self.assertIsNone(COMMAND.title)
        self.assertIsNone(COMMAND.default)

        COMMAND_PARAMETERS: Class = COMMAND.command_parameters
        self.assertEqual(COMMAND_PARAMETERS.name, 'GetProductInfo_parameters')
        self.assertFalse(COMMAND_PARAMETERS.description)
        self.assertEqual(COMMAND_PARAMETERS.class_type, ClassType.NORMAL)
        self.assertIsNone(COMMAND_PARAMETERS.title)
        self.assertIsNone(COMMAND_PARAMETERS.default)
        self.assertEqual(COMMAND_PARAMETERS.additional_properties, False)
        self.assertFalse(COMMAND_PARAMETERS.attributes)

        RESPONSE_PARAMETERS: Class = COMMAND.response_parameters
        self.assertEqual(RESPONSE_PARAMETERS.name, 'GetProductInfo_response')
        self.assertFalse(RESPONSE_PARAMETERS.description)
        self.assertEqual(RESPONSE_PARAMETERS.class_type, ClassType.NORMAL)
        self.assertIsNone(RESPONSE_PARAMETERS.title)
        self.assertIsNone(RESPONSE_PARAMETERS.default)
        self.assertEqual(RESPONSE_PARAMETERS.additional_properties, False)

        FIRST_RESPONSE_PARAMETER: Attribute = RESPONSE_PARAMETERS.attributes[0]
        self.assertEqual(FIRST_RESPONSE_PARAMETER.name, 'version')
        self.assertEqual(FIRST_RESPONSE_PARAMETER.description, 'The version of the running ARCHICAD.')
        self.assertEqual(FIRST_RESPONSE_PARAMETER.type, 'int')
        self.assertEqual(FIRST_RESPONSE_PARAMETER.required, True)

        SECOND_RESPONSE_PARAMETER: Attribute = RESPONSE_PARAMETERS.attributes[1]
        self.assertEqual(SECOND_RESPONSE_PARAMETER.name, 'buildNumber')
        self.assertEqual(SECOND_RESPONSE_PARAMETER.description, 'The build number of the running ARCHICAD.')
        self.assertEqual(SECOND_RESPONSE_PARAMETER.type, 'int')
        self.assertEqual(SECOND_RESPONSE_PARAMETER.required, True)

        SECOND_RESPONSE_PARAMETER: Attribute = RESPONSE_PARAMETERS.attributes[2]
        self.assertEqual(SECOND_RESPONSE_PARAMETER.name, 'languageCode')
        self.assertEqual(SECOND_RESPONSE_PARAMETER.description, 'The language code of the running ARCHICAD.')
        self.assertEqual(SECOND_RESPONSE_PARAMETER.type, 'str')
        self.assertEqual(SECOND_RESPONSE_PARAMETER.required, True)

    def test_setter_command(self):
        REQUIRED_FILES = ['API.SetLayoutSettings.json', 'APITypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        schema_folder = os.path.join(script_path, 'APICommandJSONSchema', 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)

        self.assertTrue(converter.classes)
        self.assertTrue(converter.commands)

        COMMAND: Command = converter.commands[0]
        self.assertEqual(COMMAND.name, 'SetLayoutSettings')
        self.assertEqual(COMMAND.description, 'Sets the parameters (settings) of the given layout.')
        self.assertIsNone(COMMAND.title)
        self.assertIsNone(COMMAND.default)
        
        COMMAND_PARAMETERS: Class = COMMAND.command_parameters
        self.assertEqual(COMMAND_PARAMETERS.name, 'SetLayoutSettings_parameters')
        self.assertFalse(COMMAND_PARAMETERS.description)
        self.assertEqual(COMMAND_PARAMETERS.class_type, ClassType.NORMAL)
        self.assertIsNone(COMMAND_PARAMETERS.title)
        self.assertIsNone(COMMAND_PARAMETERS.default)
        self.assertEqual(COMMAND_PARAMETERS.additional_properties, False)

        FIRST_COMMAND_PARAMETER: Attribute = COMMAND_PARAMETERS.attributes[0]
        self.assertEqual(FIRST_COMMAND_PARAMETER.name, 'layoutParameters')
        self.assertEqual(FIRST_COMMAND_PARAMETER.description, 'The parameters of the layout.')
        self.assertTrue(FIRST_COMMAND_PARAMETER.type in converter.classes)
        self.assertEqual(FIRST_COMMAND_PARAMETER.type, 'LayoutParameters')
        self.assertEqual(FIRST_COMMAND_PARAMETER.required, True)
        self.assertIsNone(FIRST_COMMAND_PARAMETER.title)
        self.assertIsNone(FIRST_COMMAND_PARAMETER.default)

        SECOND_COMMAND_PARAMETER: Attribute = COMMAND_PARAMETERS.attributes[1]
        self.assertEqual(SECOND_COMMAND_PARAMETER.name, 'layoutNavigatorItemId')
        self.assertEqual(SECOND_COMMAND_PARAMETER.description, 'The identifier of a navigator item.')
        self.assertTrue(SECOND_COMMAND_PARAMETER.type in converter.classes)
        self.assertEqual(SECOND_COMMAND_PARAMETER.type, 'NavigatorItemId')
        self.assertEqual(SECOND_COMMAND_PARAMETER.required, True)
        self.assertIsNone(SECOND_COMMAND_PARAMETER.title)
        self.assertIsNone(SECOND_COMMAND_PARAMETER.default)

        FIRST_COMMAND_PARAMETER_CLASS: Class = converter.classes[converter.classes.index(FIRST_COMMAND_PARAMETER.type)]
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.name, 'LayoutParameters')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.description, 'The parameters of the layout.')
        self.assertEqual(len(FIRST_COMMAND_PARAMETER_CLASS.attributes), 16)
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[2].name, 'leftMargin')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[2].type, 'float')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[2].description, 'Layout margin from the left side of the paper.')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[2].required, True)
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[6].name, 'customLayoutNumber')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[6].type, 'str')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[6].description, 'Specifies the custom ID.')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[6].required, True)
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[10].name, 'layoutPageNumber')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[10].type, 'int')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[10].description, 'Page number of layout when this layout contains multi-page drawings.')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[10].required, True)
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[14].name, 'hasIssuedRevision')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[14].type, 'bool')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[14].description, 'One or more issued document revisions have already been created for the layout.')
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.attributes[14].required, True)
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.class_type, ClassType.NORMAL)
        self.assertIsNone(FIRST_COMMAND_PARAMETER_CLASS.title)
        self.assertIsNone(FIRST_COMMAND_PARAMETER_CLASS.default)
        self.assertEqual(FIRST_COMMAND_PARAMETER_CLASS.additional_properties, False)

        SECOND_COMMAND_PARAMETER_CLASS: Class = converter.classes[converter.classes.index(SECOND_COMMAND_PARAMETER.type)]
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS.name, 'NavigatorItemId')
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS.description, 'The identifier of a navigator item.')
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS.class_type, ClassType.NORMAL)
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS.additional_properties, False)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_CLASS.title)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_CLASS.default)

        SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR: Attribute = SECOND_COMMAND_PARAMETER_CLASS.attributes[0]
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.name, 'guid')
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.type, 'UUID')
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.description, 'A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.')
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.pattern, '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')
        self.assertEqual(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.required, True)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.title)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.default)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.min_length)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.max_length)
        self.assertIsNone(SECOND_COMMAND_PARAMETER_CLASS_INNER_ATTR.values)

        RESPONSE_PARAMETERS: Class = COMMAND.response_parameters
        self.assertEqual(RESPONSE_PARAMETERS.name, 'SetLayoutSettings_response')
        self.assertFalse(RESPONSE_PARAMETERS.description)
        self.assertEqual(RESPONSE_PARAMETERS.class_type, ClassType.NORMAL)
        self.assertIsNone(RESPONSE_PARAMETERS.title)
        self.assertIsNone(RESPONSE_PARAMETERS.default)
        self.assertEqual(RESPONSE_PARAMETERS.additional_properties, False)

    def test_complex_command(self):
        REQUIRED_FILES = ['API.GetElementsByType.json', 'APITypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        schema_folder = os.path.join(script_path, 'APICommandJSONSchema', 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)

        self.assertTrue(converter.classes)
        self.assertTrue(converter.commands)
        
        COMMAND: Command = converter.commands[0]
        self.assertEqual(COMMAND.name, 'GetElementsByType')
        self.assertEqual(COMMAND.description, "Returns the identifier of every element of the given type on the plan.")
        self.assertIsNone(COMMAND.title)
        self.assertIsNone(COMMAND.default)

        COMMAND_PARAMETERS: Class = COMMAND.command_parameters
        self.assertEqual(COMMAND_PARAMETERS.name, 'GetElementsByType_parameters')
        self.assertFalse(COMMAND_PARAMETERS.description)
        self.assertEqual(COMMAND_PARAMETERS.class_type, ClassType.NORMAL)
        self.assertIsNone(COMMAND_PARAMETERS.title)
        self.assertIsNone(COMMAND_PARAMETERS.default)
        self.assertEqual(COMMAND_PARAMETERS.additional_properties, False)
        self.assertEqual(COMMAND_PARAMETERS.attributes[0].name, 'elementType')
        self.assertEqual(COMMAND_PARAMETERS.attributes[0].description, 'The type of an element.')
        self.assertEqual(COMMAND_PARAMETERS.attributes[0].type, 'str')
        self.assertEqual(COMMAND_PARAMETERS.attributes[0].required, True)
        self.assertIsNone(COMMAND_PARAMETERS.attributes[0].title)
        self.assertIsNone(COMMAND_PARAMETERS.attributes[0].default)
        self.assertIsNone(COMMAND_PARAMETERS.attributes[0].min_length)
        self.assertIsNone(COMMAND_PARAMETERS.attributes[0].max_length)
        self.assertIsNone(COMMAND_PARAMETERS.attributes[0].pattern)
        self.assertIsNotNone(COMMAND_PARAMETERS.attributes[0].values)
        self.assertEqual(len(COMMAND_PARAMETERS.attributes[0].values), 18)
        self.assertIn('Lamp', COMMAND_PARAMETERS.attributes[0].values)
        self.assertIn('Morph', COMMAND_PARAMETERS.attributes[0].values)
        self.assertIn('Wall', COMMAND_PARAMETERS.attributes[0].values)
        self.assertIn('Opening', COMMAND_PARAMETERS.attributes[0].values)
        self.assertNotIn('NotStair', COMMAND_PARAMETERS.attributes[0].values)

        RESPONSE_PARAMETERS: Class = COMMAND.response_parameters
        self.assertEqual(RESPONSE_PARAMETERS.name, 'GetElementsByType_response')
        self.assertFalse(RESPONSE_PARAMETERS.description)
        self.assertEqual(RESPONSE_PARAMETERS.class_type, ClassType.NORMAL)
        self.assertIsNone(RESPONSE_PARAMETERS.title)
        self.assertIsNone(RESPONSE_PARAMETERS.default)
        self.assertEqual(RESPONSE_PARAMETERS.additional_properties, False)
        self.assertEqual(RESPONSE_PARAMETERS.attributes[0].name, 'elements')
        self.assertEqual(RESPONSE_PARAMETERS.attributes[0].description, 'List of the elements.')
        self.assertEqual(RESPONSE_PARAMETERS.attributes[0].type, 'List')
        self.assertEqual(RESPONSE_PARAMETERS.attributes[0].required, True)
        self.assertIsNone(RESPONSE_PARAMETERS.attributes[0].title)
        self.assertIsNone(RESPONSE_PARAMETERS.attributes[0].default)
        self.assertIsNone(RESPONSE_PARAMETERS.attributes[0].min_items)
        self.assertIsNone(RESPONSE_PARAMETERS.attributes[0].max_items)
        self.assertIsNone(RESPONSE_PARAMETERS.attributes[0].unique_items)
        self.assertEqual(RESPONSE_PARAMETERS.attributes[0].itemtype, 'ElementIdArrayItem')
        self.assertIn(RESPONSE_PARAMETERS.attributes[0].itemtype, converter.classes)
        
        RESPONSE_PARAMETER_ITEMTYPE = converter.classes[converter.classes.index(RESPONSE_PARAMETERS.attributes[0].itemtype)]
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE.name, 'ElementIdArrayItem')
        self.assertFalse(RESPONSE_PARAMETER_ITEMTYPE.description)
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE.class_type, ClassType.NORMAL)
        self.assertIsNone(RESPONSE_PARAMETER_ITEMTYPE.title)
        self.assertIsNone(RESPONSE_PARAMETER_ITEMTYPE.default)
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE.additional_properties, False)
        RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS = converter.classes[converter.classes.index(RESPONSE_PARAMETER_ITEMTYPE.attributes[0].type)]
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.name, 'ElementId')
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.description, 'The identifier of an element.')
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.class_type, ClassType.NORMAL)
        self.assertIsNone(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.title)
        self.assertIsNone(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.default)
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.additional_properties, False)
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.attributes[0].name, 'guid')
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.attributes[0].type, 'UUID')
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.attributes[0].description, 'A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.')
        self.assertEqual(RESPONSE_PARAMETER_ITEMTYPE_WRAPPED_CLASS.attributes[0].pattern, '^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$')
        
    def test_one_of_command(self):
        REQUIRED_FILES = ['API.RenameNavigatorItem.json', 'APITypes.json']
        parser = SchemaParser()
        script_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        schema_folder = os.path.join(script_path, 'APICommandJSONSchema', 'RFIX')
        for schema_file in REQUIRED_FILES:
            json_content: Dict[str, Any] = {}
            with open(os.path.join(schema_folder, schema_file)) as file:
                json_content = json.load(file)

                if schema_file.startswith('API.'):
                    parser.parse_command(schema_file.split('.')[1], json_content)
                else:
                    parser.parse_types(json_content)

        converter = SchemaConverter(parser)

        self.assertTrue(converter.classes)
        self.assertTrue(converter.commands)
        
        COMMAND: Command = converter.commands[0]
        self.assertEqual(COMMAND.name, 'RenameNavigatorItem')
        self.assertEqual(COMMAND.description, "Renames an existing navigator item by specifying either the name or the ID, or both.")
        self.assertIsNone(COMMAND.title)
        self.assertIsNone(COMMAND.default)

        COMMAND_PARAMETERS: Class = COMMAND.command_parameters
        self.assertEqual(COMMAND_PARAMETERS.name, 'RenameNavigatorItem_parameters')
        self.assertFalse(COMMAND_PARAMETERS.description)
        self.assertEqual(COMMAND_PARAMETERS.class_type, ClassType.ONEOF)
        self.assertIsNone(COMMAND_PARAMETERS.title)
        self.assertIsNone(COMMAND_PARAMETERS.default)
        self.assertIsNone(COMMAND_PARAMETERS.additional_properties)
        
        FIRST_COMMAND_PARAMETER: Attribute = COMMAND_PARAMETERS.attributes[0]
        self.assertEqual(FIRST_COMMAND_PARAMETER.name, 'navigatorItemId')
        self.assertEqual(FIRST_COMMAND_PARAMETER.description, 'The identifier of a navigator item.')
        self.assertEqual(FIRST_COMMAND_PARAMETER.type, 'NavigatorItemId')
        self.assertEqual(FIRST_COMMAND_PARAMETER.required, True)
        self.assertIsNone(FIRST_COMMAND_PARAMETER.title)
        self.assertIsNone(FIRST_COMMAND_PARAMETER.default)
        
        SECOND_COMMAND_PARAMETER: Attribute = COMMAND_PARAMETERS.attributes[1]
        self.assertEqual(SECOND_COMMAND_PARAMETER.name, 'newName')
        self.assertEqual(SECOND_COMMAND_PARAMETER.description, 'New name of the navigator item.')
        self.assertEqual(SECOND_COMMAND_PARAMETER.type, 'str')
        self.assertEqual(SECOND_COMMAND_PARAMETER.required, False)
        self.assertIsNone(SECOND_COMMAND_PARAMETER.title)
        self.assertIsNone(SECOND_COMMAND_PARAMETER.default)
        
        THIRD_COMMAND_PARAMETER: Attribute = COMMAND_PARAMETERS.attributes[2]
        self.assertEqual(THIRD_COMMAND_PARAMETER.name, 'newId')
        self.assertEqual(THIRD_COMMAND_PARAMETER.description, 'New ID of the navigator item.')
        self.assertEqual(THIRD_COMMAND_PARAMETER.type, 'str')
        self.assertEqual(THIRD_COMMAND_PARAMETER.required, False)
        self.assertIsNone(THIRD_COMMAND_PARAMETER.title)
        self.assertIsNone(THIRD_COMMAND_PARAMETER.default)

        RESPONSE_PARAMETERS: Class = COMMAND.response_parameters
        self.assertEqual(RESPONSE_PARAMETERS.name, 'RenameNavigatorItem_response')
        self.assertFalse(RESPONSE_PARAMETERS.description)
        self.assertEqual(RESPONSE_PARAMETERS.class_type, ClassType.NORMAL)
        self.assertIsNone(RESPONSE_PARAMETERS.title)
        self.assertIsNone(RESPONSE_PARAMETERS.default)
        self.assertEqual(RESPONSE_PARAMETERS.additional_properties, False)
        self.assertFalse(RESPONSE_PARAMETERS.attributes)

