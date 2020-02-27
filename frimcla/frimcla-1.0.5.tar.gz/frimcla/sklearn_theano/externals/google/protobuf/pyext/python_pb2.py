# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/pyext/python.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/pyext/python.proto',
  package='google.protobuf.python.internal',
  syntax='proto2',
  serialized_pb=b'\n\"google/protobuf/pyext/python.proto\x12\x1fgoogle.protobuf.python.internal\"\xbc\x02\n\x0cTestAllTypes\x12\\\n\x17repeated_nested_message\x18\x01 \x03(\x0b\x32;.google.protobuf.python.internal.TestAllTypes.NestedMessage\x12\\\n\x17optional_nested_message\x18\x02 \x01(\x0b\x32;.google.protobuf.python.internal.TestAllTypes.NestedMessage\x12\x16\n\x0eoptional_int32\x18\x03 \x01(\x05\x1aX\n\rNestedMessage\x12\n\n\x02\x62\x62\x18\x01 \x01(\x05\x12;\n\x02\x63\x63\x18\x02 \x01(\x0b\x32/.google.protobuf.python.internal.ForeignMessage\"&\n\x0e\x46oreignMessage\x12\t\n\x01\x63\x18\x01 \x01(\x05\x12\t\n\x01\x64\x18\x02 \x03(\x05\"\x1d\n\x11TestAllExtensions*\x08\x08\x01\x10\x80\x80\x80\x80\x02:\x9a\x01\n!optional_nested_message_extension\x12\x32.google.protobuf.python.internal.TestAllExtensions\x18\x01 \x01(\x0b\x32;.google.protobuf.python.internal.TestAllTypes.NestedMessage:\x9a\x01\n!repeated_nested_message_extension\x12\x32.google.protobuf.python.internal.TestAllExtensions\x18\x02 \x03(\x0b\x32;.google.protobuf.python.internal.TestAllTypes.NestedMessageB\x02H\x01'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


OPTIONAL_NESTED_MESSAGE_EXTENSION_FIELD_NUMBER = 1
optional_nested_message_extension = _descriptor.FieldDescriptor(
  name='optional_nested_message_extension', full_name='google.protobuf.python.internal.optional_nested_message_extension', index=0,
  number=1, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
REPEATED_NESTED_MESSAGE_EXTENSION_FIELD_NUMBER = 2
repeated_nested_message_extension = _descriptor.FieldDescriptor(
  name='repeated_nested_message_extension', full_name='google.protobuf.python.internal.repeated_nested_message_extension', index=1,
  number=2, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_TESTALLTYPES_NESTEDMESSAGE = _descriptor.Descriptor(
  name='NestedMessage',
  full_name='google.protobuf.python.internal.TestAllTypes.NestedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bb', full_name='google.protobuf.python.internal.TestAllTypes.NestedMessage.bb', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cc', full_name='google.protobuf.python.internal.TestAllTypes.NestedMessage.cc', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=388,
)

_TESTALLTYPES = _descriptor.Descriptor(
  name='TestAllTypes',
  full_name='google.protobuf.python.internal.TestAllTypes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='repeated_nested_message', full_name='google.protobuf.python.internal.TestAllTypes.repeated_nested_message', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optional_nested_message', full_name='google.protobuf.python.internal.TestAllTypes.optional_nested_message', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optional_int32', full_name='google.protobuf.python.internal.TestAllTypes.optional_int32', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_TESTALLTYPES_NESTEDMESSAGE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=388,
)


_FOREIGNMESSAGE = _descriptor.Descriptor(
  name='ForeignMessage',
  full_name='google.protobuf.python.internal.ForeignMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c', full_name='google.protobuf.python.internal.ForeignMessage.c', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='d', full_name='google.protobuf.python.internal.ForeignMessage.d', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=428,
)


_TESTALLEXTENSIONS = _descriptor.Descriptor(
  name='TestAllExtensions',
  full_name='google.protobuf.python.internal.TestAllExtensions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  syntax='proto2',
  extension_ranges=[(1, 536870912), ],
  oneofs=[
  ],
  serialized_start=430,
  serialized_end=459,
)

_TESTALLTYPES_NESTEDMESSAGE.fields_by_name['cc'].message_type = _FOREIGNMESSAGE
_TESTALLTYPES_NESTEDMESSAGE.containing_type = _TESTALLTYPES
_TESTALLTYPES.fields_by_name['repeated_nested_message'].message_type = _TESTALLTYPES_NESTEDMESSAGE
_TESTALLTYPES.fields_by_name['optional_nested_message'].message_type = _TESTALLTYPES_NESTEDMESSAGE
DESCRIPTOR.message_types_by_name['TestAllTypes'] = _TESTALLTYPES
DESCRIPTOR.message_types_by_name['ForeignMessage'] = _FOREIGNMESSAGE
DESCRIPTOR.message_types_by_name['TestAllExtensions'] = _TESTALLEXTENSIONS
DESCRIPTOR.extensions_by_name['optional_nested_message_extension'] = optional_nested_message_extension
DESCRIPTOR.extensions_by_name['repeated_nested_message_extension'] = repeated_nested_message_extension

TestAllTypes = _reflection.GeneratedProtocolMessageType('TestAllTypes', (_message.Message,), dict(

  NestedMessage = _reflection.GeneratedProtocolMessageType('NestedMessage', (_message.Message,), dict(
    DESCRIPTOR = _TESTALLTYPES_NESTEDMESSAGE,
    __module__ = 'google.protobuf.pyext.python_pb2'
    # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.TestAllTypes.NestedMessage)
    ))
  ,
  DESCRIPTOR = _TESTALLTYPES,
  __module__ = 'google.protobuf.pyext.python_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.TestAllTypes)
  ))
_sym_db.RegisterMessage(TestAllTypes)
_sym_db.RegisterMessage(TestAllTypes.NestedMessage)

ForeignMessage = _reflection.GeneratedProtocolMessageType('ForeignMessage', (_message.Message,), dict(
  DESCRIPTOR = _FOREIGNMESSAGE,
  __module__ = 'google.protobuf.pyext.python_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.ForeignMessage)
  ))
_sym_db.RegisterMessage(ForeignMessage)

TestAllExtensions = _reflection.GeneratedProtocolMessageType('TestAllExtensions', (_message.Message,), dict(
  DESCRIPTOR = _TESTALLEXTENSIONS,
  __module__ = 'google.protobuf.pyext.python_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.TestAllExtensions)
  ))
_sym_db.RegisterMessage(TestAllExtensions)

optional_nested_message_extension.message_type = _TESTALLTYPES_NESTEDMESSAGE
TestAllExtensions.RegisterExtension(optional_nested_message_extension)
repeated_nested_message_extension.message_type = _TESTALLTYPES_NESTEDMESSAGE
TestAllExtensions.RegisterExtension(repeated_nested_message_extension)

DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), b'H\001')
# @@protoc_insertion_point(module_scope)
