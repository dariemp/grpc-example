# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculations.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculations.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x12\x63\x61lculations.proto\"X\n\x13\x43\x61lculationsRequest\x12\x12\n\nshape_name\x18\x01 \x01(\t\x12\x0e\n\x06height\x18\x02 \x01(\x01\x12\r\n\x05width\x18\x03 \x01(\x01\x12\x0e\n\x06length\x18\x04 \x01(\x01\"A\n\x14\x43\x61lculationsResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x18\n\x10\x63\x61lculated_value\x18\x02 \x01(\x01\x32\x81\x01\n\x13\x43\x61lculationsService\x12\x33\n\x04\x41rea\x12\x14.CalculationsRequest\x1a\x15.CalculationsResponse\x12\x35\n\x06Volume\x12\x14.CalculationsRequest\x1a\x15.CalculationsResponseb\x06proto3')
)




_CALCULATIONSREQUEST = _descriptor.Descriptor(
  name='CalculationsRequest',
  full_name='CalculationsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='shape_name', full_name='CalculationsRequest.shape_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='CalculationsRequest.height', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='CalculationsRequest.width', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='CalculationsRequest.length', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=110,
)


_CALCULATIONSRESPONSE = _descriptor.Descriptor(
  name='CalculationsResponse',
  full_name='CalculationsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='CalculationsResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='calculated_value', full_name='CalculationsResponse.calculated_value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=177,
)

DESCRIPTOR.message_types_by_name['CalculationsRequest'] = _CALCULATIONSREQUEST
DESCRIPTOR.message_types_by_name['CalculationsResponse'] = _CALCULATIONSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CalculationsRequest = _reflection.GeneratedProtocolMessageType('CalculationsRequest', (_message.Message,), dict(
  DESCRIPTOR = _CALCULATIONSREQUEST,
  __module__ = 'calculations_pb2'
  # @@protoc_insertion_point(class_scope:CalculationsRequest)
  ))
_sym_db.RegisterMessage(CalculationsRequest)

CalculationsResponse = _reflection.GeneratedProtocolMessageType('CalculationsResponse', (_message.Message,), dict(
  DESCRIPTOR = _CALCULATIONSRESPONSE,
  __module__ = 'calculations_pb2'
  # @@protoc_insertion_point(class_scope:CalculationsResponse)
  ))
_sym_db.RegisterMessage(CalculationsResponse)



_CALCULATIONSSERVICE = _descriptor.ServiceDescriptor(
  name='CalculationsService',
  full_name='CalculationsService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=180,
  serialized_end=309,
  methods=[
  _descriptor.MethodDescriptor(
    name='Area',
    full_name='CalculationsService.Area',
    index=0,
    containing_service=None,
    input_type=_CALCULATIONSREQUEST,
    output_type=_CALCULATIONSRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Volume',
    full_name='CalculationsService.Volume',
    index=1,
    containing_service=None,
    input_type=_CALCULATIONSREQUEST,
    output_type=_CALCULATIONSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATIONSSERVICE)

DESCRIPTOR.services_by_name['CalculationsService'] = _CALCULATIONSSERVICE

# @@protoc_insertion_point(module_scope)
