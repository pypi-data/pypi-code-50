# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OpenApiCommonMessages.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import OpenApiCommonModelMessages_pb2 as OpenApiCommonModelMessages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='OpenApiCommonMessages.proto',
  package='',
  syntax='proto2',
  serialized_options=_b('\n\"com.xtrader.protocol.proto.commonsB\027ContainerCommonMessagesP\001\240\001\001'),
  serialized_pb=_b('\n\x1bOpenApiCommonMessages.proto\x1a OpenApiCommonModelMessages.proto\"I\n\x0cProtoMessage\x12\x13\n\x0bpayloadType\x18\x01 \x02(\r\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\x12\x13\n\x0b\x63lientMsgId\x18\x03 \x01(\t\"\x8b\x01\n\rProtoErrorRes\x12\x31\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x11.ProtoPayloadType:\tERROR_RES\x12\x11\n\terrorCode\x18\x02 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x1f\n\x17maintenanceEndTimestamp\x18\x04 \x01(\x04\"N\n\x13ProtoHeartbeatEvent\x12\x37\n\x0bpayloadType\x18\x01 \x01(\x0e\x32\x11.ProtoPayloadType:\x0fHEARTBEAT_EVENTBB\n\"com.xtrader.protocol.proto.commonsB\x17\x43ontainerCommonMessagesP\x01\xa0\x01\x01')
  ,
  dependencies=[OpenApiCommonModelMessages__pb2.DESCRIPTOR,])




_PROTOMESSAGE = _descriptor.Descriptor(
  name='ProtoMessage',
  full_name='ProtoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payloadType', full_name='ProtoMessage.payloadType', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='ProtoMessage.payload', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clientMsgId', full_name='ProtoMessage.clientMsgId', index=2,
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
  serialized_start=65,
  serialized_end=138,
)


_PROTOERRORRES = _descriptor.Descriptor(
  name='ProtoErrorRes',
  full_name='ProtoErrorRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payloadType', full_name='ProtoErrorRes.payloadType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=50,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='errorCode', full_name='ProtoErrorRes.errorCode', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='ProtoErrorRes.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maintenanceEndTimestamp', full_name='ProtoErrorRes.maintenanceEndTimestamp', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=141,
  serialized_end=280,
)


_PROTOHEARTBEATEVENT = _descriptor.Descriptor(
  name='ProtoHeartbeatEvent',
  full_name='ProtoHeartbeatEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payloadType', full_name='ProtoHeartbeatEvent.payloadType', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=51,
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
  serialized_start=282,
  serialized_end=360,
)

_PROTOERRORRES.fields_by_name['payloadType'].enum_type = OpenApiCommonModelMessages__pb2._PROTOPAYLOADTYPE
_PROTOHEARTBEATEVENT.fields_by_name['payloadType'].enum_type = OpenApiCommonModelMessages__pb2._PROTOPAYLOADTYPE
DESCRIPTOR.message_types_by_name['ProtoMessage'] = _PROTOMESSAGE
DESCRIPTOR.message_types_by_name['ProtoErrorRes'] = _PROTOERRORRES
DESCRIPTOR.message_types_by_name['ProtoHeartbeatEvent'] = _PROTOHEARTBEATEVENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProtoMessage = _reflection.GeneratedProtocolMessageType('ProtoMessage', (_message.Message,), dict(
  DESCRIPTOR = _PROTOMESSAGE,
  __module__ = 'OpenApiCommonMessages_pb2'
  # @@protoc_insertion_point(class_scope:ProtoMessage)
  ))
_sym_db.RegisterMessage(ProtoMessage)

ProtoErrorRes = _reflection.GeneratedProtocolMessageType('ProtoErrorRes', (_message.Message,), dict(
  DESCRIPTOR = _PROTOERRORRES,
  __module__ = 'OpenApiCommonMessages_pb2'
  # @@protoc_insertion_point(class_scope:ProtoErrorRes)
  ))
_sym_db.RegisterMessage(ProtoErrorRes)

ProtoHeartbeatEvent = _reflection.GeneratedProtocolMessageType('ProtoHeartbeatEvent', (_message.Message,), dict(
  DESCRIPTOR = _PROTOHEARTBEATEVENT,
  __module__ = 'OpenApiCommonMessages_pb2'
  # @@protoc_insertion_point(class_scope:ProtoHeartbeatEvent)
  ))
_sym_db.RegisterMessage(ProtoHeartbeatEvent)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
