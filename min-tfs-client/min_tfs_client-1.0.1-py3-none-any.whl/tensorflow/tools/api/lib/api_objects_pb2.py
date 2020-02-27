# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/tools/api/lib/api_objects.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/tools/api/lib/api_objects.proto',
  package='third_party.tensorflow.tools.api',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n*tensorflow/tools/api/lib/api_objects.proto\x12 third_party.tensorflow.tools.api\x1a google/protobuf/descriptor.proto\"*\n\x0bTFAPIMember\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05mtype\x18\x02 \x01(\t\":\n\x0bTFAPIMethod\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x0f\n\x07\x61rgspec\x18\x03 \x01(\t\"\x92\x01\n\x0bTFAPIModule\x12=\n\x06member\x18\x01 \x03(\x0b\x32-.third_party.tensorflow.tools.api.TFAPIMember\x12\x44\n\rmember_method\x18\x02 \x03(\x0b\x32-.third_party.tensorflow.tools.api.TFAPIMethod\"\xa6\x01\n\nTFAPIClass\x12\x13\n\x0bis_instance\x18\x01 \x03(\t\x12=\n\x06member\x18\x02 \x03(\x0b\x32-.third_party.tensorflow.tools.api.TFAPIMember\x12\x44\n\rmember_method\x18\x03 \x03(\x0b\x32-.third_party.tensorflow.tools.api.TFAPIMethod\"F\n\nTFAPIProto\x12\x34\n\ndescriptor\x18\x01 \x01(\x0b\x32 .google.protobuf.DescriptorProto:\x02\x10\x01\"\xdd\x01\n\x0bTFAPIObject\x12\x0c\n\x04path\x18\x01 \x01(\t\x12@\n\ttf_module\x18\x02 \x01(\x0b\x32-.third_party.tensorflow.tools.api.TFAPIModule\x12>\n\x08tf_class\x18\x03 \x01(\x0b\x32,.third_party.tensorflow.tools.api.TFAPIClass\x12>\n\x08tf_proto\x18\x04 \x01(\x0b\x32,.third_party.tensorflow.tools.api.TFAPIProto')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])




_TFAPIMEMBER = _descriptor.Descriptor(
  name='TFAPIMember',
  full_name='third_party.tensorflow.tools.api.TFAPIMember',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='third_party.tensorflow.tools.api.TFAPIMember.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mtype', full_name='third_party.tensorflow.tools.api.TFAPIMember.mtype', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=156,
)


_TFAPIMETHOD = _descriptor.Descriptor(
  name='TFAPIMethod',
  full_name='third_party.tensorflow.tools.api.TFAPIMethod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='third_party.tensorflow.tools.api.TFAPIMethod.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='third_party.tensorflow.tools.api.TFAPIMethod.path', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='argspec', full_name='third_party.tensorflow.tools.api.TFAPIMethod.argspec', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=216,
)


_TFAPIMODULE = _descriptor.Descriptor(
  name='TFAPIModule',
  full_name='third_party.tensorflow.tools.api.TFAPIModule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='member', full_name='third_party.tensorflow.tools.api.TFAPIModule.member', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='member_method', full_name='third_party.tensorflow.tools.api.TFAPIModule.member_method', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=365,
)


_TFAPICLASS = _descriptor.Descriptor(
  name='TFAPIClass',
  full_name='third_party.tensorflow.tools.api.TFAPIClass',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_instance', full_name='third_party.tensorflow.tools.api.TFAPIClass.is_instance', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='member', full_name='third_party.tensorflow.tools.api.TFAPIClass.member', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='member_method', full_name='third_party.tensorflow.tools.api.TFAPIClass.member_method', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=368,
  serialized_end=534,
)


_TFAPIPROTO = _descriptor.Descriptor(
  name='TFAPIProto',
  full_name='third_party.tensorflow.tools.api.TFAPIProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='descriptor', full_name='third_party.tensorflow.tools.api.TFAPIProto.descriptor', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\020\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=536,
  serialized_end=606,
)


_TFAPIOBJECT = _descriptor.Descriptor(
  name='TFAPIObject',
  full_name='third_party.tensorflow.tools.api.TFAPIObject',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='third_party.tensorflow.tools.api.TFAPIObject.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tf_module', full_name='third_party.tensorflow.tools.api.TFAPIObject.tf_module', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tf_class', full_name='third_party.tensorflow.tools.api.TFAPIObject.tf_class', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tf_proto', full_name='third_party.tensorflow.tools.api.TFAPIObject.tf_proto', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=609,
  serialized_end=830,
)

_TFAPIMODULE.fields_by_name['member'].message_type = _TFAPIMEMBER
_TFAPIMODULE.fields_by_name['member_method'].message_type = _TFAPIMETHOD
_TFAPICLASS.fields_by_name['member'].message_type = _TFAPIMEMBER
_TFAPICLASS.fields_by_name['member_method'].message_type = _TFAPIMETHOD
_TFAPIPROTO.fields_by_name['descriptor'].message_type = google_dot_protobuf_dot_descriptor__pb2._DESCRIPTORPROTO
_TFAPIOBJECT.fields_by_name['tf_module'].message_type = _TFAPIMODULE
_TFAPIOBJECT.fields_by_name['tf_class'].message_type = _TFAPICLASS
_TFAPIOBJECT.fields_by_name['tf_proto'].message_type = _TFAPIPROTO
DESCRIPTOR.message_types_by_name['TFAPIMember'] = _TFAPIMEMBER
DESCRIPTOR.message_types_by_name['TFAPIMethod'] = _TFAPIMETHOD
DESCRIPTOR.message_types_by_name['TFAPIModule'] = _TFAPIMODULE
DESCRIPTOR.message_types_by_name['TFAPIClass'] = _TFAPICLASS
DESCRIPTOR.message_types_by_name['TFAPIProto'] = _TFAPIPROTO
DESCRIPTOR.message_types_by_name['TFAPIObject'] = _TFAPIOBJECT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TFAPIMember = _reflection.GeneratedProtocolMessageType('TFAPIMember', (_message.Message,), dict(
  DESCRIPTOR = _TFAPIMEMBER,
  __module__ = 'tensorflow.tools.api.lib.api_objects_pb2'
  # @@protoc_insertion_point(class_scope:third_party.tensorflow.tools.api.TFAPIMember)
  ))
_sym_db.RegisterMessage(TFAPIMember)

TFAPIMethod = _reflection.GeneratedProtocolMessageType('TFAPIMethod', (_message.Message,), dict(
  DESCRIPTOR = _TFAPIMETHOD,
  __module__ = 'tensorflow.tools.api.lib.api_objects_pb2'
  # @@protoc_insertion_point(class_scope:third_party.tensorflow.tools.api.TFAPIMethod)
  ))
_sym_db.RegisterMessage(TFAPIMethod)

TFAPIModule = _reflection.GeneratedProtocolMessageType('TFAPIModule', (_message.Message,), dict(
  DESCRIPTOR = _TFAPIMODULE,
  __module__ = 'tensorflow.tools.api.lib.api_objects_pb2'
  # @@protoc_insertion_point(class_scope:third_party.tensorflow.tools.api.TFAPIModule)
  ))
_sym_db.RegisterMessage(TFAPIModule)

TFAPIClass = _reflection.GeneratedProtocolMessageType('TFAPIClass', (_message.Message,), dict(
  DESCRIPTOR = _TFAPICLASS,
  __module__ = 'tensorflow.tools.api.lib.api_objects_pb2'
  # @@protoc_insertion_point(class_scope:third_party.tensorflow.tools.api.TFAPIClass)
  ))
_sym_db.RegisterMessage(TFAPIClass)

TFAPIProto = _reflection.GeneratedProtocolMessageType('TFAPIProto', (_message.Message,), dict(
  DESCRIPTOR = _TFAPIPROTO,
  __module__ = 'tensorflow.tools.api.lib.api_objects_pb2'
  # @@protoc_insertion_point(class_scope:third_party.tensorflow.tools.api.TFAPIProto)
  ))
_sym_db.RegisterMessage(TFAPIProto)

TFAPIObject = _reflection.GeneratedProtocolMessageType('TFAPIObject', (_message.Message,), dict(
  DESCRIPTOR = _TFAPIOBJECT,
  __module__ = 'tensorflow.tools.api.lib.api_objects_pb2'
  # @@protoc_insertion_point(class_scope:third_party.tensorflow.tools.api.TFAPIObject)
  ))
_sym_db.RegisterMessage(TFAPIObject)


_TFAPIPROTO._options = None
# @@protoc_insertion_point(module_scope)
