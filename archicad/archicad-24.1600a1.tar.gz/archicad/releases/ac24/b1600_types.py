"""GRAPHISOFT
"""
from uuid import UUID
from typing import Union, Optional, List

from archicad.acbasetype import _ACBaseType

class ClassificationSystemId(_ACBaseType):
	"""The identifier of a classification system.

	Attributes:
		guid (UUID): A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.

	"""
	__slots__ = ("guid", )

	def __init__(self, guid: UUID):
		self.guid: UUID = guid

ClassificationSystemId.get_classinfo().add_field('guid', UUID)


class ClassificationSystemIdArrayItem(_ACBaseType):
	"""
	Attributes:
		classificationSystemId (:obj:`ClassificationSystemId`): The identifier of a classification system.

	"""
	__slots__ = ("classificationSystemId", )

	def __init__(self, classificationSystemId: ClassificationSystemId):
		self.classificationSystemId: ClassificationSystemId = classificationSystemId

ClassificationSystemIdArrayItem.get_classinfo().add_field('classificationSystemId', ClassificationSystemId)


class ClassificationItemId(_ACBaseType):
	"""The identifier of a classification item.

	Attributes:
		guid (UUID): A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.

	"""
	__slots__ = ("guid", )

	def __init__(self, guid: UUID):
		self.guid: UUID = guid

ClassificationItemId.get_classinfo().add_field('guid', UUID)


class ClassificationItemIdArrayItem(_ACBaseType):
	"""
	Attributes:
		classificationItemId (:obj:`ClassificationItemId`): The identifier of a classification item.

	"""
	__slots__ = ("classificationItemId", )

	def __init__(self, classificationItemId: ClassificationItemId):
		self.classificationItemId: ClassificationItemId = classificationItemId

ClassificationItemIdArrayItem.get_classinfo().add_field('classificationItemId', ClassificationItemId)


class ClassificationId(_ACBaseType):
	"""The element classification identifier.

	Attributes:
		classificationSystemId (:obj:`ClassificationSystemId`): The identifier of a classification system.
		classificationItemId (:obj:`ClassificationItemId`, optional): The identifier of a classification item.

	"""
	__slots__ = ("classificationSystemId", "classificationItemId", )

	def __init__(self, classificationSystemId: ClassificationSystemId, classificationItemId: Optional[ClassificationItemId] = None):
		self.classificationSystemId: ClassificationSystemId = classificationSystemId
		self.classificationItemId: Optional[ClassificationItemId] = classificationItemId

ClassificationId.get_classinfo().add_field('classificationSystemId', ClassificationSystemId)
ClassificationId.get_classinfo().add_field('classificationItemId', Optional[ClassificationItemId])


class ClassificationItemDetails(_ACBaseType):
	"""Details of a classification item.

	Attributes:
		id (str): The user specified unique identifier of the classification item.
		name (str): The display name of the classification item.
		description (str): The description of the classification item.

	"""
	__slots__ = ("id", "name", "description", )

	def __init__(self, id: str, name: str, description: str):
		self.id: str = id
		self.name: str = name
		self.description: str = description

ClassificationItemDetails.get_classinfo().add_field('id', str)
ClassificationItemDetails.get_classinfo().add_field('name', str)
ClassificationItemDetails.get_classinfo().add_field('description', str)


class ClassificationSystem(_ACBaseType):
	"""Details of a classification system.

	Attributes:
		classificationSystemId (:obj:`ClassificationSystemId`): The identifier of a classification system.
		name (str): The display name of the classification system.
		description (str): The description of the classification system.
		source (str): The source of the classification system (e.g. URL to a classification system standard).
		version (str): The version string of the classification system.
		date (str): A date in its string representation as defined in ISO 8601: YYYY-MM-DD.

	"""
	__slots__ = ("classificationSystemId", "name", "description", "source", "version", "date", )

	def __init__(self, classificationSystemId: ClassificationSystemId, name: str, description: str, source: str, version: str, date: str):
		self.classificationSystemId: ClassificationSystemId = classificationSystemId
		self.name: str = name
		self.description: str = description
		self.source: str = source
		self.version: str = version
		self.date: str = date

ClassificationSystem.get_classinfo().add_field('classificationSystemId', ClassificationSystemId)
ClassificationSystem.get_classinfo().add_field('name', str)
ClassificationSystem.get_classinfo().add_field('description', str)
ClassificationSystem.get_classinfo().add_field('source', str)
ClassificationSystem.get_classinfo().add_field('version', str)
ClassificationSystem.get_classinfo().add_field('date', str)


class UserDefinedPropertyUserId(_ACBaseType):
	"""An object which uniquely identifies a User-Defined Property by its name in human-readable form.

	Attributes:
		type (str): None
		localizedName (:obj:`list` of :obj:`str`): List of the localized name parts: first element is the Group Name, second element is the Property Name of the Property.

	"""
	__slots__ = ("type", "localizedName", )

	def __init__(self, type: str, localizedName: List[str]):
		self.type: str = type
		self.localizedName: List[str] = localizedName

UserDefinedPropertyUserId.get_classinfo().add_field('type', str)
UserDefinedPropertyUserId.get_classinfo().add_field('localizedName', List[str])


class BuiltInPropertyUserId(_ACBaseType):
	"""An object which uniquely identifies a Built-In Property by its name in a human-readable form.

	Attributes:
		type (str): None
		nonLocalizedName (str): Non-localized name of the Built-In Property.

	"""
	__slots__ = ("type", "nonLocalizedName", )

	def __init__(self, type: str, nonLocalizedName: str):
		self.type: str = type
		self.nonLocalizedName: str = nonLocalizedName

BuiltInPropertyUserId.get_classinfo().add_field('type', str)
BuiltInPropertyUserId.get_classinfo().add_field('nonLocalizedName', str)


class PropertyUserId:
	"""An object which uniquely identifies a Property by its name in human-readable form. May represent a User-Defined or a Built-In Property.
	"""
	pass

PropertyUserId = Union[UserDefinedPropertyUserId, BuiltInPropertyUserId]


class PropertyId(_ACBaseType):
	"""The identifier of a property.

	Attributes:
		guid (UUID): A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.

	"""
	__slots__ = ("guid", )

	def __init__(self, guid: UUID):
		self.guid: UUID = guid

PropertyId.get_classinfo().add_field('guid', UUID)


class PropertyIdArrayItem(_ACBaseType):
	"""
	Attributes:
		propertyId (:obj:`PropertyId`): The identifier of a property.

	"""
	__slots__ = ("propertyId", )

	def __init__(self, propertyId: PropertyId):
		self.propertyId: PropertyId = propertyId

PropertyIdArrayItem.get_classinfo().add_field('propertyId', PropertyId)


class PropertyGroup(_ACBaseType):
	"""A property group.

	Attributes:
		name (str): The property group name.

	"""
	__slots__ = ("name", )

	def __init__(self, name: str):
		self.name: str = name

PropertyGroup.get_classinfo().add_field('name', str)


class NormalNumberPropertyValue(_ACBaseType):
	"""A number property value containing a valid numeric value.

	Attributes:
		type (str): None
		status (str): None
		value (float): None

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: float):
		self.type: str = type
		self.status: str = status
		self.value: float = value

NormalNumberPropertyValue.get_classinfo().add_field('type', str)
NormalNumberPropertyValue.get_classinfo().add_field('status', str)
NormalNumberPropertyValue.get_classinfo().add_field('value', float)


class NormalIntegerPropertyValue(_ACBaseType):
	"""An integer property value containing a valid integer number.

	Attributes:
		type (str): None
		status (str): None
		value (int): None

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: int):
		self.type: str = type
		self.status: str = status
		self.value: int = value

NormalIntegerPropertyValue.get_classinfo().add_field('type', str)
NormalIntegerPropertyValue.get_classinfo().add_field('status', str)
NormalIntegerPropertyValue.get_classinfo().add_field('value', int)


class NormalStringPropertyValue(_ACBaseType):
	"""A string property value containing a valid string.

	Attributes:
		type (str): None
		status (str): None
		value (str): None

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: str):
		self.type: str = type
		self.status: str = status
		self.value: str = value

NormalStringPropertyValue.get_classinfo().add_field('type', str)
NormalStringPropertyValue.get_classinfo().add_field('status', str)
NormalStringPropertyValue.get_classinfo().add_field('value', str)


class NormalBooleanPropertyValue(_ACBaseType):
	"""A boolean property value containing a valid boolean value.

	Attributes:
		type (str): None
		status (str): None
		value (bool): None

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: bool):
		self.type: str = type
		self.status: str = status
		self.value: bool = value

NormalBooleanPropertyValue.get_classinfo().add_field('type', str)
NormalBooleanPropertyValue.get_classinfo().add_field('status', str)
NormalBooleanPropertyValue.get_classinfo().add_field('value', bool)


class NormalLengthPropertyValue(_ACBaseType):
	"""A length property value containing a real length value. Value is measured in SI (meters).

	Attributes:
		type (str): None
		status (str): None
		value (float): None

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: float):
		self.type: str = type
		self.status: str = status
		self.value: float = value

NormalLengthPropertyValue.get_classinfo().add_field('type', str)
NormalLengthPropertyValue.get_classinfo().add_field('status', str)
NormalLengthPropertyValue.get_classinfo().add_field('value', float)


class NormalAreaPropertyValue(_ACBaseType):
	"""An area property value containing a real area. Value is measured in SI (square meters).

	Attributes:
		type (str): None
		status (str): None
		value (float): None

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: float):
		self.type: str = type
		self.status: str = status
		self.value: float = value

NormalAreaPropertyValue.get_classinfo().add_field('type', str)
NormalAreaPropertyValue.get_classinfo().add_field('status', str)
NormalAreaPropertyValue.get_classinfo().add_field('value', float)


class NormalVolumePropertyValue(_ACBaseType):
	"""A volume property value containing a real volume. Value is measured in SI (cubic meters).

	Attributes:
		type (str): None
		status (str): None
		value (float): None

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: float):
		self.type: str = type
		self.status: str = status
		self.value: float = value

NormalVolumePropertyValue.get_classinfo().add_field('type', str)
NormalVolumePropertyValue.get_classinfo().add_field('status', str)
NormalVolumePropertyValue.get_classinfo().add_field('value', float)


class NormalAnglePropertyValue(_ACBaseType):
	"""An angle property value containing a real angle. Value is measured in SI (radians).

	Attributes:
		type (str): None
		status (str): None
		value (float): None

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: float):
		self.type: str = type
		self.status: str = status
		self.value: float = value

NormalAnglePropertyValue.get_classinfo().add_field('type', str)
NormalAnglePropertyValue.get_classinfo().add_field('status', str)
NormalAnglePropertyValue.get_classinfo().add_field('value', float)


class NormalNumberListPropertyValue(_ACBaseType):
	"""A number list property value containing numbers in an array.

	Attributes:
		type (str): None
		status (str): None
		value (:obj:`list` of :obj:`float`): 

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: List[float]):
		self.type: str = type
		self.status: str = status
		self.value: List[float] = value

NormalNumberListPropertyValue.get_classinfo().add_field('type', str)
NormalNumberListPropertyValue.get_classinfo().add_field('status', str)
NormalNumberListPropertyValue.get_classinfo().add_field('value', List[float])


class NormalIntegerListPropertyValue(_ACBaseType):
	"""An integer list property value containing integers in an array.

	Attributes:
		type (str): None
		status (str): None
		value (:obj:`list` of :obj:`int`): 

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: List[int]):
		self.type: str = type
		self.status: str = status
		self.value: List[int] = value

NormalIntegerListPropertyValue.get_classinfo().add_field('type', str)
NormalIntegerListPropertyValue.get_classinfo().add_field('status', str)
NormalIntegerListPropertyValue.get_classinfo().add_field('value', List[int])


class NormalStringListPropertyValue(_ACBaseType):
	"""A string list property value containing strings in an array.

	Attributes:
		type (str): None
		status (str): None
		value (:obj:`list` of :obj:`str`): 

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: List[str]):
		self.type: str = type
		self.status: str = status
		self.value: List[str] = value

NormalStringListPropertyValue.get_classinfo().add_field('type', str)
NormalStringListPropertyValue.get_classinfo().add_field('status', str)
NormalStringListPropertyValue.get_classinfo().add_field('value', List[str])


class NormalBooleanListPropertyValue(_ACBaseType):
	"""A boolean list property value containing boolean values in an array.

	Attributes:
		type (str): None
		status (str): None
		value (:obj:`list` of :obj:`bool`): 

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: List[bool]):
		self.type: str = type
		self.status: str = status
		self.value: List[bool] = value

NormalBooleanListPropertyValue.get_classinfo().add_field('type', str)
NormalBooleanListPropertyValue.get_classinfo().add_field('status', str)
NormalBooleanListPropertyValue.get_classinfo().add_field('value', List[bool])


class NormalLengthListPropertyValue(_ACBaseType):
	"""A length list property value containing length values in an array. Values are measured in SI (meters).

	Attributes:
		type (str): None
		status (str): None
		value (:obj:`list` of :obj:`float`): 

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: List[float]):
		self.type: str = type
		self.status: str = status
		self.value: List[float] = value

NormalLengthListPropertyValue.get_classinfo().add_field('type', str)
NormalLengthListPropertyValue.get_classinfo().add_field('status', str)
NormalLengthListPropertyValue.get_classinfo().add_field('value', List[float])


class NormalAreaListPropertyValue(_ACBaseType):
	"""A area list property value containing areas in an array. Values are measured in SI (square meters).

	Attributes:
		type (str): None
		status (str): None
		value (:obj:`list` of :obj:`float`): 

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: List[float]):
		self.type: str = type
		self.status: str = status
		self.value: List[float] = value

NormalAreaListPropertyValue.get_classinfo().add_field('type', str)
NormalAreaListPropertyValue.get_classinfo().add_field('status', str)
NormalAreaListPropertyValue.get_classinfo().add_field('value', List[float])


class NormalVolumeListPropertyValue(_ACBaseType):
	"""A volume list property value containing volumes in an array. Values are measured in SI (cubic meters).

	Attributes:
		type (str): None
		status (str): None
		value (:obj:`list` of :obj:`float`): 

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: List[float]):
		self.type: str = type
		self.status: str = status
		self.value: List[float] = value

NormalVolumeListPropertyValue.get_classinfo().add_field('type', str)
NormalVolumeListPropertyValue.get_classinfo().add_field('status', str)
NormalVolumeListPropertyValue.get_classinfo().add_field('value', List[float])


class NormalAngleListPropertyValue(_ACBaseType):
	"""A angle list property value containing angles in an array. Values are measured in SI (radians).

	Attributes:
		type (str): None
		status (str): None
		value (:obj:`list` of :obj:`float`): 

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: List[float]):
		self.type: str = type
		self.status: str = status
		self.value: List[float] = value

NormalAngleListPropertyValue.get_classinfo().add_field('type', str)
NormalAngleListPropertyValue.get_classinfo().add_field('status', str)
NormalAngleListPropertyValue.get_classinfo().add_field('value', List[float])


class UserUndefinedPropertyValue(_ACBaseType):
	"""A userUndefined value means that there is no actual number/string/etc. value, but the user deliberately set an Undefined value: this is a valid value, too.

	Attributes:
		type (str): None
		status (str): None

	"""
	__slots__ = ("type", "status", )

	def __init__(self, type: str, status: str):
		self.type: str = type
		self.status: str = status

UserUndefinedPropertyValue.get_classinfo().add_field('type', str)
UserUndefinedPropertyValue.get_classinfo().add_field('status', str)


class NotAvailablePropertyValue(_ACBaseType):
	"""A notAvailable value means that the property is not available for the property owner (and therefore it has no property value for it).

	Attributes:
		type (str): None
		status (str): None

	"""
	__slots__ = ("type", "status", )

	def __init__(self, type: str, status: str):
		self.type: str = type
		self.status: str = status

NotAvailablePropertyValue.get_classinfo().add_field('type', str)
NotAvailablePropertyValue.get_classinfo().add_field('status', str)


class NotEvaluatedPropertyValue(_ACBaseType):
	"""A notEvaluated value means that the property could not be evaluated for the property owner for some reason.

	Attributes:
		type (str): None
		status (str): None

	"""
	__slots__ = ("type", "status", )

	def __init__(self, type: str, status: str):
		self.type: str = type
		self.status: str = status

NotEvaluatedPropertyValue.get_classinfo().add_field('type', str)
NotEvaluatedPropertyValue.get_classinfo().add_field('status', str)


class DisplayValueEnumId(_ACBaseType):
	"""An enumeration value identifier using the displayed value.

	Attributes:
		type (str): None
		displayValue (str): None

	"""
	__slots__ = ("type", "displayValue", )

	def __init__(self, type: str, displayValue: str):
		self.type: str = type
		self.displayValue: str = displayValue

DisplayValueEnumId.get_classinfo().add_field('type', str)
DisplayValueEnumId.get_classinfo().add_field('displayValue', str)


class EnumValueId:
	"""The identifier of a property enumeration value.
	"""
	pass

EnumValueId = Union[DisplayValueEnumId]


class PossibleEnumValue(_ACBaseType):
	"""Description of an enumeration value.

	Attributes:
		enumValueId (:obj:`EnumValueId`): The identifier of a property enumeration value.
		displayValue (str): Displayed value of the enumeration.

	"""
	__slots__ = ("enumValueId", "displayValue", )

	def __init__(self, enumValueId: EnumValueId, displayValue: str):
		self.enumValueId: EnumValueId = enumValueId
		self.displayValue: str = displayValue

PossibleEnumValue.get_classinfo().add_field('enumValueId', EnumValueId)
PossibleEnumValue.get_classinfo().add_field('displayValue', str)


class PossibleEnumValuesArrayItem(_ACBaseType):
	"""
	Attributes:
		enumValue (:obj:`PossibleEnumValue`): Description of an enumeration value.

	"""
	__slots__ = ("enumValue", )

	def __init__(self, enumValue: PossibleEnumValue):
		self.enumValue: PossibleEnumValue = enumValue

PossibleEnumValuesArrayItem.get_classinfo().add_field('enumValue', PossibleEnumValue)


class Error(_ACBaseType):
	"""Error details.

	Attributes:
		code (int): The error code.
		message (str): The error message.

	"""
	__slots__ = ("code", "message", )

	def __init__(self, code: int, message: str):
		self.code: int = code
		self.message: str = message

Error.get_classinfo().add_field('code', int)
Error.get_classinfo().add_field('message', str)


class SuccessfulExecutionResult(_ACBaseType):
	"""
	Attributes:
		success (bool): None

	"""
	__slots__ = ("success", )

	def __init__(self, success: bool):
		self.success: bool = success

SuccessfulExecutionResult.get_classinfo().add_field('success', bool)


class FailedExecutionResult(_ACBaseType):
	"""
	Attributes:
		success (bool): None
		error (:obj:`Error`): Error details.

	"""
	__slots__ = ("success", "error", )

	def __init__(self, success: bool, error: Error):
		self.success: bool = success
		self.error: Error = error

FailedExecutionResult.get_classinfo().add_field('success', bool)
FailedExecutionResult.get_classinfo().add_field('error', Error)


class ExecutionResult:
	"""The result of the execution for one case.
	"""
	pass

ExecutionResult = Union[SuccessfulExecutionResult, FailedExecutionResult]


class ElementId(_ACBaseType):
	"""The identifier of an element.

	Attributes:
		guid (UUID): A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.

	"""
	__slots__ = ("guid", )

	def __init__(self, guid: UUID):
		self.guid: UUID = guid

ElementId.get_classinfo().add_field('guid', UUID)


class ElementIdArrayItem(_ACBaseType):
	"""
	Attributes:
		elementId (:obj:`ElementId`): The identifier of an element.

	"""
	__slots__ = ("elementId", )

	def __init__(self, elementId: ElementId):
		self.elementId: ElementId = elementId

ElementIdArrayItem.get_classinfo().add_field('elementId', ElementId)


class NavigatorItemId(_ACBaseType):
	"""The identifier of a navigator item.

	Attributes:
		guid (UUID): A Globally Unique Identifier (or Universally Unique Identifier) in its string representation as defined in RFC 4122.

	"""
	__slots__ = ("guid", )

	def __init__(self, guid: UUID):
		self.guid: UUID = guid

NavigatorItemId.get_classinfo().add_field('guid', UUID)


class PublisherSetId(_ACBaseType):
	"""The identifier of a publisher set.

	Attributes:
		type (str): Type of the navigator item tree.
		name (str): Name of the publisher set.

	"""
	__slots__ = ("type", "name", )

	def __init__(self, type: str, name: str):
		self.type: str = type
		self.name: str = name

PublisherSetId.get_classinfo().add_field('type', str)
PublisherSetId.get_classinfo().add_field('name', str)


class OtherNavigatorTreeId(_ACBaseType):
	"""The identifier of a navigator item tree.

	Attributes:
		type (str): Type of the navigator item tree.

	"""
	__slots__ = ("type", )

	def __init__(self, type: str):
		self.type: str = type

OtherNavigatorTreeId.get_classinfo().add_field('type', str)


class FolderParameters(_ACBaseType):
	"""The parameters of a folder.

	Attributes:
		name (str): The name of the folder to create.

	"""
	__slots__ = ("name", )

	def __init__(self, name: str):
		self.name: str = name

FolderParameters.get_classinfo().add_field('name', str)


class NavigatorTreeId:
	"""The identifier of a navigator item tree.
	"""
	pass

NavigatorTreeId = Union[PublisherSetId, OtherNavigatorTreeId]


class BoundingBox2D(_ACBaseType):
	"""2D bounding box of an element.

	Attributes:
		xMin (float): Minimum X value of bounding box.
		yMin (float): Minimum Y value of bounding box.
		xMax (float): Maximum X value of bounding box.
		yMax (float): Maximum Y value of bounding box.

	"""
	__slots__ = ("xMin", "yMin", "xMax", "yMax", )

	def __init__(self, xMin: float, yMin: float, xMax: float, yMax: float):
		self.xMin: float = xMin
		self.yMin: float = yMin
		self.xMax: float = xMax
		self.yMax: float = yMax

BoundingBox2D.get_classinfo().add_field('xMin', float)
BoundingBox2D.get_classinfo().add_field('yMin', float)
BoundingBox2D.get_classinfo().add_field('xMax', float)
BoundingBox2D.get_classinfo().add_field('yMax', float)


class BoundingBox3D(_ACBaseType):
	"""3D bounding box of an element.

	Attributes:
		xMin (float): Minimum X value of bounding box.
		yMin (float): Minimum Y value of bounding box.
		zMin (float): Minimum Z value of bounding box.
		xMax (float): Maximum X value of bounding box.
		yMax (float): Maximum Y value of bounding box.
		zMax (float): Maximum Z value of bounding box.

	"""
	__slots__ = ("xMin", "yMin", "zMin", "xMax", "yMax", "zMax", )

	def __init__(self, xMin: float, yMin: float, zMin: float, xMax: float, yMax: float, zMax: float):
		self.xMin: float = xMin
		self.yMin: float = yMin
		self.zMin: float = zMin
		self.xMax: float = xMax
		self.yMax: float = yMax
		self.zMax: float = zMax

BoundingBox3D.get_classinfo().add_field('xMin', float)
BoundingBox3D.get_classinfo().add_field('yMin', float)
BoundingBox3D.get_classinfo().add_field('zMin', float)
BoundingBox3D.get_classinfo().add_field('xMax', float)
BoundingBox3D.get_classinfo().add_field('yMax', float)
BoundingBox3D.get_classinfo().add_field('zMax', float)


class Subset(_ACBaseType):
	"""Provides a way to assign IDs to the layouts contained in the subset.

	Attributes:
		name (str): Defines the name for the layout subset.
		includeToIDSequence (bool): Indicates whether this subset is included in or excluded from automatic ID assignment.
		customNumbering (bool): Defines whether the IDs are generated automatically or use a custom numbering.
		continueNumbering (bool): Continue using the ID assignment of upper levels. Layouts within this subset are going to be assigned IDs as if they were not within this subset, but part of the level above. In this case you are only using the Subset as a logical grouping which has no effect on IDs.
		useUpperPrefix (bool): Use the prefix and ID of upper levels. Layouts in this subset will be assigned IDs based on the previous layout in the layout book structure.
		addOwnPrefix (bool): Adds own prefix to the subset.
		customNumber (str): Specifies the custom subset ID.
		autoNumber (str): Specifies the automatic subset ID.
		numberingStyle (str): List of the supported numbering styles.
		startAt (int): Specifies a number from which the numbering starts.
		ownPrefix (str): Defines a custom prefix for the subset.

	"""
	__slots__ = ("name", "includeToIDSequence", "customNumbering", "continueNumbering", "useUpperPrefix", "addOwnPrefix", "customNumber", "autoNumber", "numberingStyle", "startAt", "ownPrefix", )

	def __init__(self, name: str, includeToIDSequence: bool, customNumbering: bool, continueNumbering: bool, useUpperPrefix: bool, addOwnPrefix: bool, customNumber: str, autoNumber: str, numberingStyle: str, startAt: int, ownPrefix: str):
		self.name: str = name
		self.includeToIDSequence: bool = includeToIDSequence
		self.customNumbering: bool = customNumbering
		self.continueNumbering: bool = continueNumbering
		self.useUpperPrefix: bool = useUpperPrefix
		self.addOwnPrefix: bool = addOwnPrefix
		self.customNumber: str = customNumber
		self.autoNumber: str = autoNumber
		self.numberingStyle: str = numberingStyle
		self.startAt: int = startAt
		self.ownPrefix: str = ownPrefix

Subset.get_classinfo().add_field('name', str)
Subset.get_classinfo().add_field('includeToIDSequence', bool)
Subset.get_classinfo().add_field('customNumbering', bool)
Subset.get_classinfo().add_field('continueNumbering', bool)
Subset.get_classinfo().add_field('useUpperPrefix', bool)
Subset.get_classinfo().add_field('addOwnPrefix', bool)
Subset.get_classinfo().add_field('customNumber', str)
Subset.get_classinfo().add_field('autoNumber', str)
Subset.get_classinfo().add_field('numberingStyle', str)
Subset.get_classinfo().add_field('startAt', int)
Subset.get_classinfo().add_field('ownPrefix', str)


class LayoutParameters(_ACBaseType):
	"""The parameters of the layout.

	Attributes:
		horizontalSize (float): Horizontal size of the layout in millimeters.
		verticalSize (float): Vertical size of the layout in millimeters.
		leftMargin (float): Layout margin from the left side of the paper.
		topMargin (float): Layout margin from the top side of the paper.
		rightMargin (float): Layout margin from the right side of the paper.
		bottomMargin (float): Layout margin from the bottom side of the paper.
		customLayoutNumber (str): Specifies the custom ID.
		customLayoutNumbering (bool): Defines whether a unique ID is used for the current layout or not.
		doNotIncludeInNumbering (bool): Indicates whether this layout is included in or excluded from automatic ID assignment.
		displayMasterLayoutBelow (bool): Display the master layout above or below the layout.
		layoutPageNumber (int): Page number of layout when this layout contains multi-page drawings.
		actPageIndex (int): The actual index of layout inside the multi-page layout.
		currentRevisionId (str): ID of the current document revision of the layout.
		currentFinalRevisionId (str): ID with optional suffix of the current document revision of the layout.
		hasIssuedRevision (bool): One or more issued document revisions have already been created for the layout.
		hasActualRevision (bool): An open document revision exists for the layout.

	"""
	__slots__ = ("horizontalSize", "verticalSize", "leftMargin", "topMargin", "rightMargin", "bottomMargin", "customLayoutNumber", "customLayoutNumbering", "doNotIncludeInNumbering", "displayMasterLayoutBelow", "layoutPageNumber", "actPageIndex", "currentRevisionId", "currentFinalRevisionId", "hasIssuedRevision", "hasActualRevision", )

	def __init__(self, horizontalSize: float, verticalSize: float, leftMargin: float, topMargin: float, rightMargin: float, bottomMargin: float, customLayoutNumber: str, customLayoutNumbering: bool, doNotIncludeInNumbering: bool, displayMasterLayoutBelow: bool, layoutPageNumber: int, actPageIndex: int, currentRevisionId: str, currentFinalRevisionId: str, hasIssuedRevision: bool, hasActualRevision: bool):
		self.horizontalSize: float = horizontalSize
		self.verticalSize: float = verticalSize
		self.leftMargin: float = leftMargin
		self.topMargin: float = topMargin
		self.rightMargin: float = rightMargin
		self.bottomMargin: float = bottomMargin
		self.customLayoutNumber: str = customLayoutNumber
		self.customLayoutNumbering: bool = customLayoutNumbering
		self.doNotIncludeInNumbering: bool = doNotIncludeInNumbering
		self.displayMasterLayoutBelow: bool = displayMasterLayoutBelow
		self.layoutPageNumber: int = layoutPageNumber
		self.actPageIndex: int = actPageIndex
		self.currentRevisionId: str = currentRevisionId
		self.currentFinalRevisionId: str = currentFinalRevisionId
		self.hasIssuedRevision: bool = hasIssuedRevision
		self.hasActualRevision: bool = hasActualRevision

LayoutParameters.get_classinfo().add_field('horizontalSize', float)
LayoutParameters.get_classinfo().add_field('verticalSize', float)
LayoutParameters.get_classinfo().add_field('leftMargin', float)
LayoutParameters.get_classinfo().add_field('topMargin', float)
LayoutParameters.get_classinfo().add_field('rightMargin', float)
LayoutParameters.get_classinfo().add_field('bottomMargin', float)
LayoutParameters.get_classinfo().add_field('customLayoutNumber', str)
LayoutParameters.get_classinfo().add_field('customLayoutNumbering', bool)
LayoutParameters.get_classinfo().add_field('doNotIncludeInNumbering', bool)
LayoutParameters.get_classinfo().add_field('displayMasterLayoutBelow', bool)
LayoutParameters.get_classinfo().add_field('layoutPageNumber', int)
LayoutParameters.get_classinfo().add_field('actPageIndex', int)
LayoutParameters.get_classinfo().add_field('currentRevisionId', str)
LayoutParameters.get_classinfo().add_field('currentFinalRevisionId', str)
LayoutParameters.get_classinfo().add_field('hasIssuedRevision', bool)
LayoutParameters.get_classinfo().add_field('hasActualRevision', bool)


class ClassificationIdWrapper(_ACBaseType):
	"""
	Attributes:
		classificationId (:obj:`ClassificationId`): The element classification identifier.

	"""
	__slots__ = ("classificationId", )

	def __init__(self, classificationId: ClassificationId):
		self.classificationId: ClassificationId = classificationId

ClassificationIdWrapper.get_classinfo().add_field('classificationId', ClassificationId)


class ErrorWrapper(_ACBaseType):
	"""
	Attributes:
		error (:obj:`Error`): Error details.

	"""
	__slots__ = ("error", )

	def __init__(self, error: Error):
		self.error: Error = error

ErrorWrapper.get_classinfo().add_field('error', Error)


class ClassificationItemDetailsWrapper(_ACBaseType):
	"""
	Attributes:
		classificationItem (:obj:`ClassificationItemDetails`): Details of a classification item.

	"""
	__slots__ = ("classificationItem", )

	def __init__(self, classificationItem: ClassificationItemDetails):
		self.classificationItem: ClassificationItemDetails = classificationItem

ClassificationItemDetailsWrapper.get_classinfo().add_field('classificationItem', ClassificationItemDetails)


class PropertyIdWrapper(_ACBaseType):
	"""
	Attributes:
		propertyId (:obj:`PropertyId`): The identifier of a property.

	"""
	__slots__ = ("propertyId", )

	def __init__(self, propertyId: PropertyId):
		self.propertyId: PropertyId = propertyId

PropertyIdWrapper.get_classinfo().add_field('propertyId', PropertyId)


class EnumValueIdWrapper(_ACBaseType):
	"""
	Attributes:
		enumValueId (:obj:`EnumValueId`): The identifier of a property enumeration value.

	"""
	__slots__ = ("enumValueId", )

	def __init__(self, enumValueId: EnumValueId):
		self.enumValueId: EnumValueId = enumValueId

EnumValueIdWrapper.get_classinfo().add_field('enumValueId', EnumValueId)


class NavigatorItemIdWrapper(_ACBaseType):
	"""
	Attributes:
		navigatorItemId (:obj:`NavigatorItemId`): The identifier of a navigator item.

	"""
	__slots__ = ("navigatorItemId", )

	def __init__(self, navigatorItemId: NavigatorItemId):
		self.navigatorItemId: NavigatorItemId = navigatorItemId

NavigatorItemIdWrapper.get_classinfo().add_field('navigatorItemId', NavigatorItemId)


class BoundingBox2DWrapper(_ACBaseType):
	"""
	Attributes:
		boundingBox2D (:obj:`BoundingBox2D`): 2D bounding box of an element.

	"""
	__slots__ = ("boundingBox2D", )

	def __init__(self, boundingBox2D: BoundingBox2D):
		self.boundingBox2D: BoundingBox2D = boundingBox2D

BoundingBox2DWrapper.get_classinfo().add_field('boundingBox2D', BoundingBox2D)


class BoundingBox3DWrapper(_ACBaseType):
	"""
	Attributes:
		boundingBox3D (:obj:`BoundingBox3D`): 3D bounding box of an element.

	"""
	__slots__ = ("boundingBox3D", )

	def __init__(self, boundingBox3D: BoundingBox3D):
		self.boundingBox3D: BoundingBox3D = boundingBox3D

BoundingBox3DWrapper.get_classinfo().add_field('boundingBox3D', BoundingBox3D)


class ClassificationIdOrError:
	pass

ClassificationIdOrError = Union[ClassificationIdWrapper, ErrorWrapper]


class ElementClassification(_ACBaseType):
	"""Element classification.

	Attributes:
		elementId (:obj:`ElementId`): The identifier of an element.
		classificationId (:obj:`ClassificationId`): The element classification identifier.

	"""
	__slots__ = ("elementId", "classificationId", )

	def __init__(self, elementId: ElementId, classificationId: ClassificationId):
		self.elementId: ElementId = elementId
		self.classificationId: ClassificationId = classificationId

ElementClassification.get_classinfo().add_field('elementId', ElementId)
ElementClassification.get_classinfo().add_field('classificationId', ClassificationId)


class ClassificationItemOrError:
	pass

ClassificationItemOrError = Union[ClassificationItemDetailsWrapper, ErrorWrapper]


class PropertyIdOrError:
	"""A property identifier or error.
	"""
	pass

PropertyIdOrError = Union[PropertyIdWrapper, ErrorWrapper]


class PropertyDefinition(_ACBaseType):
	"""A property definition.

	Attributes:
		group (:obj:`PropertyGroup`): A property group.
		name (str): The localized name of the property.
		description (str): The description of the property.
		possibleEnumValues (:obj:`list` of :obj:`PossibleEnumValuesArrayItem`, optional): List of enumeration values.

	"""
	__slots__ = ("group", "name", "description", "possibleEnumValues", )

	def __init__(self, group: PropertyGroup, name: str, description: str, possibleEnumValues: Optional[List[PossibleEnumValuesArrayItem]] = None):
		self.group: PropertyGroup = group
		self.name: str = name
		self.description: str = description
		self.possibleEnumValues: Optional[List[PossibleEnumValuesArrayItem]] = possibleEnumValues

PropertyDefinition.get_classinfo().add_field('group', PropertyGroup)
PropertyDefinition.get_classinfo().add_field('name', str)
PropertyDefinition.get_classinfo().add_field('description', str)
PropertyDefinition.get_classinfo().add_field('possibleEnumValues', Optional[List[PossibleEnumValuesArrayItem]])


class NormalSingleEnumPropertyValue(_ACBaseType):
	"""A single enumeration property value containing the ID of the selected enum value.

	Attributes:
		type (str): None
		status (str): None
		value (:obj:`EnumValueId`): The identifier of a property enumeration value.

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: EnumValueId):
		self.type: str = type
		self.status: str = status
		self.value: EnumValueId = value

NormalSingleEnumPropertyValue.get_classinfo().add_field('type', str)
NormalSingleEnumPropertyValue.get_classinfo().add_field('status', str)
NormalSingleEnumPropertyValue.get_classinfo().add_field('value', EnumValueId)


class NormalMultiEnumPropertyValue(_ACBaseType):
	"""A multiple choice enumeration property value containing the IDs of the selected enum values in an array.

	Attributes:
		type (str): None
		status (str): None
		value (:obj:`list` of :obj:`EnumValueIdWrapper`): List of enumeration identifiers.

	"""
	__slots__ = ("type", "status", "value", )

	def __init__(self, type: str, status: str, value: List[EnumValueIdWrapper]):
		self.type: str = type
		self.status: str = status
		self.value: List[EnumValueIdWrapper] = value

NormalMultiEnumPropertyValue.get_classinfo().add_field('type', str)
NormalMultiEnumPropertyValue.get_classinfo().add_field('status', str)
NormalMultiEnumPropertyValue.get_classinfo().add_field('value', List[EnumValueIdWrapper])


class NormalOrUserUndefinedPropertyValue:
	"""A normal or a userUndefined property value.
	"""
	pass

NormalOrUserUndefinedPropertyValue = Union[NormalNumberPropertyValue, NormalIntegerPropertyValue, NormalStringPropertyValue, NormalBooleanPropertyValue, NormalLengthPropertyValue, NormalAreaPropertyValue, NormalVolumePropertyValue, NormalAnglePropertyValue, NormalNumberListPropertyValue, NormalIntegerListPropertyValue, NormalStringListPropertyValue, NormalBooleanListPropertyValue, NormalLengthListPropertyValue, NormalAreaListPropertyValue, NormalVolumeListPropertyValue, NormalAngleListPropertyValue, NormalSingleEnumPropertyValue, NormalMultiEnumPropertyValue, UserUndefinedPropertyValue]


class PropertyValue:
	"""A normal, userUndefined, notAvailable or notEvaluated property value.
	"""
	pass

PropertyValue = Union[NormalOrUserUndefinedPropertyValue, NotAvailablePropertyValue, NotEvaluatedPropertyValue]


class ElementPropertyValue(_ACBaseType):
	"""A property value with the identifier of the property and the owner element.

	Attributes:
		elementId (:obj:`ElementId`): The identifier of an element.
		propertyId (:obj:`PropertyId`): The identifier of a property.
		propertyValue (:obj:`NormalOrUserUndefinedPropertyValue`): A normal or a userUndefined property value.

	"""
	__slots__ = ("elementId", "propertyId", "propertyValue", )

	def __init__(self, elementId: ElementId, propertyId: PropertyId, propertyValue: NormalOrUserUndefinedPropertyValue):
		self.elementId: ElementId = elementId
		self.propertyId: PropertyId = propertyId
		self.propertyValue: NormalOrUserUndefinedPropertyValue = propertyValue

ElementPropertyValue.get_classinfo().add_field('elementId', ElementId)
ElementPropertyValue.get_classinfo().add_field('propertyId', PropertyId)
ElementPropertyValue.get_classinfo().add_field('propertyValue', NormalOrUserUndefinedPropertyValue)


class BoundingBox2DOrError:
	"""A 2D bounding box or error.
	"""
	pass

BoundingBox2DOrError = Union[BoundingBox2DWrapper, ErrorWrapper]


class BoundingBox3DOrError:
	"""A 3D bounding box or error.
	"""
	pass

BoundingBox3DOrError = Union[BoundingBox3DWrapper, ErrorWrapper]


class ClassificationIdsOrErrorsWrapper(_ACBaseType):
	"""
	Attributes:
		classificationIds (:obj:`list` of :obj:`ClassificationIdOrError`): The list of element classification identifiers or errors.

	"""
	__slots__ = ("classificationIds", )

	def __init__(self, classificationIds: List[ClassificationIdOrError]):
		self.classificationIds: List[ClassificationIdOrError] = classificationIds

ClassificationIdsOrErrorsWrapper.get_classinfo().add_field('classificationIds', List[ClassificationIdOrError])


class PropertyDefinitionWrapper(_ACBaseType):
	"""
	Attributes:
		propertyDefinition (:obj:`PropertyDefinition`): A property definition.

	"""
	__slots__ = ("propertyDefinition", )

	def __init__(self, propertyDefinition: PropertyDefinition):
		self.propertyDefinition: PropertyDefinition = propertyDefinition

PropertyDefinitionWrapper.get_classinfo().add_field('propertyDefinition', PropertyDefinition)


class PropertyValueWrapper(_ACBaseType):
	"""
	Attributes:
		propertyValue (:obj:`PropertyValue`): A normal, userUndefined, notAvailable or notEvaluated property value.

	"""
	__slots__ = ("propertyValue", )

	def __init__(self, propertyValue: PropertyValue):
		self.propertyValue: PropertyValue = propertyValue

PropertyValueWrapper.get_classinfo().add_field('propertyValue', PropertyValue)


class ElementClassificationOrError:
	"""Element classification identifiers or error.
	"""
	pass

ElementClassificationOrError = Union[ClassificationIdsOrErrorsWrapper, ErrorWrapper]


class PropertyDefinitionOrError:
	"""A property definition or error.
	"""
	pass

PropertyDefinitionOrError = Union[PropertyDefinitionWrapper, ErrorWrapper]


class PropertyValueOrErrorItem:
	"""Contains a property value or an error for the property.
	"""
	pass

PropertyValueOrErrorItem = Union[PropertyValueWrapper, ErrorWrapper]


class PropertyValuesWrapper(_ACBaseType):
	"""
	Attributes:
		propertyValues (:obj:`list` of :obj:`PropertyValueOrErrorItem`): List of property values for an element.

	"""
	__slots__ = ("propertyValues", )

	def __init__(self, propertyValues: List[PropertyValueOrErrorItem]):
		self.propertyValues: List[PropertyValueOrErrorItem] = propertyValues

PropertyValuesWrapper.get_classinfo().add_field('propertyValues', List[PropertyValueOrErrorItem])


class PropertyValuesOrErrorForElement:
	"""Contains either a list of property values or an error for the element
	"""
	pass

PropertyValuesOrErrorForElement = Union[PropertyValuesWrapper, ErrorWrapper]


class ClassificationItemInTree_: pass
class ClassificationItemArrayItem(_ACBaseType):
	"""
	Attributes:
		classificationItem (ClassificationItemInTree_): Details of a classification item.

	"""
	__slots__ = ("classificationItem", )

	def __init__(self, classificationItem: ClassificationItemInTree_):
		self.classificationItem: ClassificationItemInTree_ = classificationItem


class ClassificationItemInTree(_ACBaseType):
	"""Details of a classification item.

	Attributes:
		classificationItemId (:obj:`ClassificationItemId`): The identifier of a classification item.
		id (str): The user specified unique identifier of the classification item.
		name (str): The display name of the classification item.
		description (str): The description of the classification item.
		children (:obj:`list` of :obj:`ClassificationItemArrayItem`, optional): The list of classification items.

	"""
	__slots__ = ("classificationItemId", "id", "name", "description", "children", )

	def __init__(self, classificationItemId: ClassificationItemId, id: str, name: str, description: str, children: Optional[List[ClassificationItemArrayItem]] = None):
		self.classificationItemId: ClassificationItemId = classificationItemId
		self.id: str = id
		self.name: str = name
		self.description: str = description
		self.children: Optional[List[ClassificationItemArrayItem]] = children

ClassificationItemInTree.get_classinfo().add_field('classificationItemId', ClassificationItemId)
ClassificationItemInTree.get_classinfo().add_field('id', str)
ClassificationItemInTree.get_classinfo().add_field('name', str)
ClassificationItemInTree.get_classinfo().add_field('description', str)
ClassificationItemInTree.get_classinfo().add_field('children', Optional[List[ClassificationItemArrayItem]])

ClassificationItemInTree_ = ClassificationItemInTree
ClassificationItemArrayItem.get_classinfo().add_field('classificationItem', ClassificationItemInTree)


class NavigatorItem_: pass
class NavigatorItemArrayItem(_ACBaseType):
	"""
	Attributes:
		navigatorItem (NavigatorItem_): Details of a navigator item.

	"""
	__slots__ = ("navigatorItem", )

	def __init__(self, navigatorItem: NavigatorItem_):
		self.navigatorItem: NavigatorItem_ = navigatorItem


class NavigatorItem(_ACBaseType):
	"""Details of a navigator item.

	Attributes:
		navigatorItemId (:obj:`NavigatorItemId`): The identifier of a navigator item.
		prefix (str): Prefix of the name of the navigator item.
		name (str): Name of the navigator item.
		type (str): Possible types of a navigator item. Most of the names are self-explanatory, the only exception is 'UndefinedItem', which means that the type of this navigator item cannot be retrieved from ARCHICAD yet.
		sourceNavigatorItemId (:obj:`NavigatorItemId`, optional): The identifier of a navigator item.
		children (:obj:`list` of :obj:`NavigatorItemArrayItem`, optional): List of navigator items.

	"""
	__slots__ = ("navigatorItemId", "prefix", "name", "type", "sourceNavigatorItemId", "children", )

	def __init__(self, navigatorItemId: NavigatorItemId, prefix: str, name: str, type: str, sourceNavigatorItemId: Optional[NavigatorItemId] = None, children: Optional[List[NavigatorItemArrayItem]] = None):
		self.navigatorItemId: NavigatorItemId = navigatorItemId
		self.prefix: str = prefix
		self.name: str = name
		self.type: str = type
		self.sourceNavigatorItemId: Optional[NavigatorItemId] = sourceNavigatorItemId
		self.children: Optional[List[NavigatorItemArrayItem]] = children

NavigatorItem.get_classinfo().add_field('navigatorItemId', NavigatorItemId)
NavigatorItem.get_classinfo().add_field('prefix', str)
NavigatorItem.get_classinfo().add_field('name', str)
NavigatorItem.get_classinfo().add_field('type', str)
NavigatorItem.get_classinfo().add_field('sourceNavigatorItemId', Optional[NavigatorItemId])
NavigatorItem.get_classinfo().add_field('children', Optional[List[NavigatorItemArrayItem]])

NavigatorItem_ = NavigatorItem
NavigatorItemArrayItem.get_classinfo().add_field('navigatorItem', NavigatorItem)


class NavigatorTree(_ACBaseType):
	"""A tree of navigator items.

	Attributes:
		rootItem (:obj:`NavigatorItem`): Details of a navigator item.

	"""
	__slots__ = ("rootItem", )

	def __init__(self, rootItem: NavigatorItem):
		self.rootItem: NavigatorItem = rootItem

NavigatorTree.get_classinfo().add_field('rootItem', NavigatorItem)


