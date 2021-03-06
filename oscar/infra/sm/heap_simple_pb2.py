# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='infra/sm/heap_simple.proto',
  package='a.sm',
  serialized_pb='\n\x1ainfra/sm/heap_simple.proto\x12\x04\x61.sm\"\xb8\x01\n\x10HeapSimpleCfgGpb\x12\x0e\n\x06offset\x18\x01 \x01(\x03\x12\x0c\n\x04size\x18\x02 \x01(\x03\x12\x14\n\x0cheaderOffset\x18\x03 \x01(\x03\x12/\n\x07\x66saData\x18\x04 \x03(\x0b\x32\x1e.a.sm.HeapSimpleCfgGpb.FsaData\x1a?\n\x07\x46saData\x12\x11\n\tblockSize\x18\x01 \x01(\x03\x12\x11\n\tnumBlocks\x18\x02 \x01(\x03\x12\x0e\n\x06offset\x18\x03 \x01(\x03')




_HEAPSIMPLECFGGPB_FSADATA = descriptor.Descriptor(
  name='FsaData',
  full_name='a.sm.HeapSimpleCfgGpb.FsaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='blockSize', full_name='a.sm.HeapSimpleCfgGpb.FsaData.blockSize', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='numBlocks', full_name='a.sm.HeapSimpleCfgGpb.FsaData.numBlocks', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='offset', full_name='a.sm.HeapSimpleCfgGpb.FsaData.offset', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=158,
  serialized_end=221,
)

_HEAPSIMPLECFGGPB = descriptor.Descriptor(
  name='HeapSimpleCfgGpb',
  full_name='a.sm.HeapSimpleCfgGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='offset', full_name='a.sm.HeapSimpleCfgGpb.offset', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='size', full_name='a.sm.HeapSimpleCfgGpb.size', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='headerOffset', full_name='a.sm.HeapSimpleCfgGpb.headerOffset', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fsaData', full_name='a.sm.HeapSimpleCfgGpb.fsaData', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_HEAPSIMPLECFGGPB_FSADATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=37,
  serialized_end=221,
)


_HEAPSIMPLECFGGPB_FSADATA.containing_type = _HEAPSIMPLECFGGPB;
_HEAPSIMPLECFGGPB.fields_by_name['fsaData'].message_type = _HEAPSIMPLECFGGPB_FSADATA

class HeapSimpleCfgGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class FsaData(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _HEAPSIMPLECFGGPB_FSADATA
    
    # @@protoc_insertion_point(class_scope:a.sm.HeapSimpleCfgGpb.FsaData)
  DESCRIPTOR = _HEAPSIMPLECFGGPB
  
  # @@protoc_insertion_point(class_scope:a.sm.HeapSimpleCfgGpb)

# @@protoc_insertion_point(module_scope)
