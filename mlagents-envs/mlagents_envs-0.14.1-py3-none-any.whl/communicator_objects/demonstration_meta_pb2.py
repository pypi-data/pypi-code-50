# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mlagents_envs/communicator_objects/demonstration_meta.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mlagents_envs/communicator_objects/demonstration_meta.proto',
  package='communicator_objects',
  syntax='proto3',
  serialized_pb=_b('\n;mlagents_envs/communicator_objects/demonstration_meta.proto\x12\x14\x63ommunicator_objects\"\x8d\x01\n\x16\x44\x65monstrationMetaProto\x12\x13\n\x0b\x61pi_version\x18\x01 \x01(\x05\x12\x1a\n\x12\x64\x65monstration_name\x18\x02 \x01(\t\x12\x14\n\x0cnumber_steps\x18\x03 \x01(\x05\x12\x17\n\x0fnumber_episodes\x18\x04 \x01(\x05\x12\x13\n\x0bmean_reward\x18\x05 \x01(\x02\x42\x1f\xaa\x02\x1cMLAgents.CommunicatorObjectsb\x06proto3')
)




_DEMONSTRATIONMETAPROTO = _descriptor.Descriptor(
  name='DemonstrationMetaProto',
  full_name='communicator_objects.DemonstrationMetaProto',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='api_version', full_name='communicator_objects.DemonstrationMetaProto.api_version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='demonstration_name', full_name='communicator_objects.DemonstrationMetaProto.demonstration_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_steps', full_name='communicator_objects.DemonstrationMetaProto.number_steps', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_episodes', full_name='communicator_objects.DemonstrationMetaProto.number_episodes', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mean_reward', full_name='communicator_objects.DemonstrationMetaProto.mean_reward', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=227,
)

DESCRIPTOR.message_types_by_name['DemonstrationMetaProto'] = _DEMONSTRATIONMETAPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DemonstrationMetaProto = _reflection.GeneratedProtocolMessageType('DemonstrationMetaProto', (_message.Message,), dict(
  DESCRIPTOR = _DEMONSTRATIONMETAPROTO,
  __module__ = 'mlagents_envs.communicator_objects.demonstration_meta_pb2'
  # @@protoc_insertion_point(class_scope:communicator_objects.DemonstrationMetaProto)
  ))
_sym_db.RegisterMessage(DemonstrationMetaProto)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\034MLAgents.CommunicatorObjects'))
# @@protoc_insertion_point(module_scope)
