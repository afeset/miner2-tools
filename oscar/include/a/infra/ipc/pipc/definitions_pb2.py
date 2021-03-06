# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='include/a/infra/ipc/pipc/definitions.proto',
  package='a.ipc',
  serialized_pb='\n*include/a/infra/ipc/pipc/definitions.proto\x12\x05\x61.ipc\"\xa1\x01\n\x0eMetaRequestGpb\x12\x13\n\x0brequestName\x18\x01 \x01(\t\x12\x37\n\x0crequestPairs\x18\x02 \x03(\x0b\x32!.a.ipc.MetaRequestGpb.MetaPairGpb\x12\x15\n\trequestId\x18\x03 \x01(\x03:\x02-1\x1a*\n\x0bMetaPairGpb\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"<\n\x0fMetaResponseGpb\x12\x15\n\nresponseRc\x18\x01 \x01(\x03:\x01\x30\x12\x12\n\nresponseId\x18\x02 \x01(\x03')




_METAREQUESTGPB_METAPAIRGPB = descriptor.Descriptor(
  name='MetaPairGpb',
  full_name='a.ipc.MetaRequestGpb.MetaPairGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='a.ipc.MetaRequestGpb.MetaPairGpb.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='a.ipc.MetaRequestGpb.MetaPairGpb.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=173,
  serialized_end=215,
)

_METAREQUESTGPB = descriptor.Descriptor(
  name='MetaRequestGpb',
  full_name='a.ipc.MetaRequestGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='requestName', full_name='a.ipc.MetaRequestGpb.requestName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='requestPairs', full_name='a.ipc.MetaRequestGpb.requestPairs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='requestId', full_name='a.ipc.MetaRequestGpb.requestId', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_METAREQUESTGPB_METAPAIRGPB, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=54,
  serialized_end=215,
)


_METARESPONSEGPB = descriptor.Descriptor(
  name='MetaResponseGpb',
  full_name='a.ipc.MetaResponseGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='responseRc', full_name='a.ipc.MetaResponseGpb.responseRc', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='responseId', full_name='a.ipc.MetaResponseGpb.responseId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=217,
  serialized_end=277,
)


_METAREQUESTGPB_METAPAIRGPB.containing_type = _METAREQUESTGPB;
_METAREQUESTGPB.fields_by_name['requestPairs'].message_type = _METAREQUESTGPB_METAPAIRGPB

class MetaRequestGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class MetaPairGpb(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _METAREQUESTGPB_METAPAIRGPB
    
    # @@protoc_insertion_point(class_scope:a.ipc.MetaRequestGpb.MetaPairGpb)
  DESCRIPTOR = _METAREQUESTGPB
  
  # @@protoc_insertion_point(class_scope:a.ipc.MetaRequestGpb)

class MetaResponseGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _METARESPONSEGPB
  
  # @@protoc_insertion_point(class_scope:a.ipc.MetaResponseGpb)

# @@protoc_insertion_point(module_scope)
