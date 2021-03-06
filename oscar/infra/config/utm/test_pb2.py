# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


DESCRIPTOR = descriptor.FileDescriptor(
  name='infra/config/utm/test.proto',
  package='a.config.utm',
  serialized_pb='\n\x1binfra/config/utm/test.proto\x12\x0c\x61.config.utm\x1a)include/a/infra/config/config_types.proto\x1a&include/a/infra/prov/definitions.proto\"7\n\x0eType1ConfigGpb\x12\x10\n\x05\x61ttr1\x18\x01 \x01(\x03:\x01\x37\x12\x13\n\x05\x61ttr2\x18\x02 \x01(\t:\x04lala\"e\n\x0eType2ConfigGpb\x12\r\n\x05stuff\x18\x01 \x03(\x03\x12\x32\n\x10stuffListControl\x18\x02 \x01(\x0b\x32\x18.a.config.ListControlGpb\x12\x10\n\x05\x61ttr3\x18\x03 \x01(\x03:\x01\x37\"<\n\x0eType3ConfigGpb\x12\x14\n\x0c\x63reateChildA\x18\x01 \x01(\x08\x12\x14\n\x0c\x63reateChildB\x18\x02 \x01(\x03\"%\n\rKey1ConfigGpb\x12\t\n\x01\x61\x18\x01 \x01(\t\x12\t\n\x01\x62\x18\x02 \x01(\x03\"\x8d\x01\n\rKey2ConfigGpb\x12\x34\n\x02\x65n\x18\x01 \x01(\x0e\x32\".a.config.utm.Key2ConfigGpb.Corpus:\x04kWeb\"F\n\x06\x43orpus\x12\x0e\n\nkUniversal\x10\x00\x12\x08\n\x04kWeb\x10\x01\x12\x0b\n\x07kImages\x10\x02\x12\n\n\x06kLocal\x10\x03\x12\t\n\x05kNews\x10\x04\"\x1e\n\x11Type4KeyConfigGpb\x12\t\n\x01\x61\x18\x01 \x01(\x05\"+\n\x0eType4ConfigGpb\x12\t\n\x01\x63\x18\x01 \x01(\x08\x12\x0e\n\x01\x64\x18\x02 \x01(\t:\x03\x64\x65\x66\"\x9d\x01\n\x0eType5ConfigGpb\x12*\n\x05k1opt\x18\x01 \x01(\x0b\x32\x1b.a.config.utm.Key1ConfigGpb\x12+\n\x05t1rep\x18\x02 \x03(\x0b\x32\x1c.a.config.utm.Type1ConfigGpb\x12\x32\n\x10t1repListControl\x18\x03 \x01(\x0b\x32\x18.a.config.ListControlGpb\":\n\x11TypeBadConfig1Gpb\x12\x10\n\x05\x61ttr1\x18\x01 \x02(\x03:\x01\x37\x12\x13\n\x05\x61ttr2\x18\x02 \x01(\t:\x04lala\"U\n\x11TypeBadConfig2Gpb\x12\x10\n\x05\x61ttr1\x18\x01 \x01(\x03:\x01\x37\x12.\n\x05\x61ttr2\x18\x02 \x01(\x0b\x32\x1f.a.config.utm.TypeBadConfig1Gpb\"\"\n\x11TypeBadConfig3Gpb\x12\r\n\x05\x61ttr1\x18\x01 \x03(\x03\"4\n\x11TypeBadConfig4Gpb\x12\r\n\x05\x61ttr1\x18\x01 \x03(\x03\x12\x10\n\x05\x61ttr3\x18\x03 \x01(\x03:\x01\x37\"N\n\x11TypeBadConfig5Gpb\x12\x10\n\x05\x61ttr1\x18\x01 \x01(\x03:\x01\x37\x12\'\n\x05\x61ttr3\x18\x02 \x01(\x0b\x32\x18.a.config.ListControlGpb\"<\n\x11TypeBadConfig6Gpb\x12\'\n\x05\x61ttr1\x18\x01 \x01(\x0b\x32\x18.a.config.ListControlGpb\"R\n\x11TypeBadConfig7Gpb\x12\r\n\x05stuff\x18\x01 \x03(\x03\x12.\n\x0cstuffListCon\x18\x02 \x01(\x0b\x32\x18.a.config.ListControlGpb')



_KEY2CONFIGGPB_CORPUS = descriptor.EnumDescriptor(
  name='Corpus',
  full_name='a.config.utm.Key2ConfigGpb.Corpus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='kUniversal', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kWeb', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kImages', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kLocal', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='kNews', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=461,
  serialized_end=531,
)


_TYPE1CONFIGGPB = descriptor.Descriptor(
  name='Type1ConfigGpb',
  full_name='a.config.utm.Type1ConfigGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attr1', full_name='a.config.utm.Type1ConfigGpb.attr1', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=7,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attr2', full_name='a.config.utm.Type1ConfigGpb.attr2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("lala", "utf-8"),
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
  serialized_start=128,
  serialized_end=183,
)


_TYPE2CONFIGGPB = descriptor.Descriptor(
  name='Type2ConfigGpb',
  full_name='a.config.utm.Type2ConfigGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='stuff', full_name='a.config.utm.Type2ConfigGpb.stuff', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stuffListControl', full_name='a.config.utm.Type2ConfigGpb.stuffListControl', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attr3', full_name='a.config.utm.Type2ConfigGpb.attr3', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=7,
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
  serialized_start=185,
  serialized_end=286,
)


_TYPE3CONFIGGPB = descriptor.Descriptor(
  name='Type3ConfigGpb',
  full_name='a.config.utm.Type3ConfigGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='createChildA', full_name='a.config.utm.Type3ConfigGpb.createChildA', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='createChildB', full_name='a.config.utm.Type3ConfigGpb.createChildB', index=1,
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
  serialized_start=288,
  serialized_end=348,
)


_KEY1CONFIGGPB = descriptor.Descriptor(
  name='Key1ConfigGpb',
  full_name='a.config.utm.Key1ConfigGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='a', full_name='a.config.utm.Key1ConfigGpb.a', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='b', full_name='a.config.utm.Key1ConfigGpb.b', index=1,
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
  serialized_start=350,
  serialized_end=387,
)


_KEY2CONFIGGPB = descriptor.Descriptor(
  name='Key2ConfigGpb',
  full_name='a.config.utm.Key2ConfigGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='en', full_name='a.config.utm.Key2ConfigGpb.en', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _KEY2CONFIGGPB_CORPUS,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=390,
  serialized_end=531,
)


_TYPE4KEYCONFIGGPB = descriptor.Descriptor(
  name='Type4KeyConfigGpb',
  full_name='a.config.utm.Type4KeyConfigGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='a', full_name='a.config.utm.Type4KeyConfigGpb.a', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=533,
  serialized_end=563,
)


_TYPE4CONFIGGPB = descriptor.Descriptor(
  name='Type4ConfigGpb',
  full_name='a.config.utm.Type4ConfigGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='c', full_name='a.config.utm.Type4ConfigGpb.c', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='d', full_name='a.config.utm.Type4ConfigGpb.d', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("def", "utf-8"),
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
  serialized_start=565,
  serialized_end=608,
)


_TYPE5CONFIGGPB = descriptor.Descriptor(
  name='Type5ConfigGpb',
  full_name='a.config.utm.Type5ConfigGpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='k1opt', full_name='a.config.utm.Type5ConfigGpb.k1opt', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='t1rep', full_name='a.config.utm.Type5ConfigGpb.t1rep', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='t1repListControl', full_name='a.config.utm.Type5ConfigGpb.t1repListControl', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=611,
  serialized_end=768,
)


_TYPEBADCONFIG1GPB = descriptor.Descriptor(
  name='TypeBadConfig1Gpb',
  full_name='a.config.utm.TypeBadConfig1Gpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attr1', full_name='a.config.utm.TypeBadConfig1Gpb.attr1', index=0,
      number=1, type=3, cpp_type=2, label=2,
      has_default_value=True, default_value=7,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attr2', full_name='a.config.utm.TypeBadConfig1Gpb.attr2', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("lala", "utf-8"),
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
  serialized_start=770,
  serialized_end=828,
)


_TYPEBADCONFIG2GPB = descriptor.Descriptor(
  name='TypeBadConfig2Gpb',
  full_name='a.config.utm.TypeBadConfig2Gpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attr1', full_name='a.config.utm.TypeBadConfig2Gpb.attr1', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=7,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attr2', full_name='a.config.utm.TypeBadConfig2Gpb.attr2', index=1,
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
  extension_ranges=[],
  serialized_start=830,
  serialized_end=915,
)


_TYPEBADCONFIG3GPB = descriptor.Descriptor(
  name='TypeBadConfig3Gpb',
  full_name='a.config.utm.TypeBadConfig3Gpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attr1', full_name='a.config.utm.TypeBadConfig3Gpb.attr1', index=0,
      number=1, type=3, cpp_type=2, label=3,
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
  extension_ranges=[],
  serialized_start=917,
  serialized_end=951,
)


_TYPEBADCONFIG4GPB = descriptor.Descriptor(
  name='TypeBadConfig4Gpb',
  full_name='a.config.utm.TypeBadConfig4Gpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attr1', full_name='a.config.utm.TypeBadConfig4Gpb.attr1', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attr3', full_name='a.config.utm.TypeBadConfig4Gpb.attr3', index=1,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=7,
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
  serialized_start=953,
  serialized_end=1005,
)


_TYPEBADCONFIG5GPB = descriptor.Descriptor(
  name='TypeBadConfig5Gpb',
  full_name='a.config.utm.TypeBadConfig5Gpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attr1', full_name='a.config.utm.TypeBadConfig5Gpb.attr1', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=True, default_value=7,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='attr3', full_name='a.config.utm.TypeBadConfig5Gpb.attr3', index=1,
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
  extension_ranges=[],
  serialized_start=1007,
  serialized_end=1085,
)


_TYPEBADCONFIG6GPB = descriptor.Descriptor(
  name='TypeBadConfig6Gpb',
  full_name='a.config.utm.TypeBadConfig6Gpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attr1', full_name='a.config.utm.TypeBadConfig6Gpb.attr1', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  extension_ranges=[],
  serialized_start=1087,
  serialized_end=1147,
)


_TYPEBADCONFIG7GPB = descriptor.Descriptor(
  name='TypeBadConfig7Gpb',
  full_name='a.config.utm.TypeBadConfig7Gpb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='stuff', full_name='a.config.utm.TypeBadConfig7Gpb.stuff', index=0,
      number=1, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='stuffListCon', full_name='a.config.utm.TypeBadConfig7Gpb.stuffListCon', index=1,
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
  extension_ranges=[],
  serialized_start=1149,
  serialized_end=1231,
)

import include.a.infra.config.config_types_pb2
import include.a.infra.prov.definitions_pb2

_TYPE2CONFIGGPB.fields_by_name['stuffListControl'].message_type = include.a.infra.config.config_types_pb2._LISTCONTROLGPB
_KEY2CONFIGGPB.fields_by_name['en'].enum_type = _KEY2CONFIGGPB_CORPUS
_KEY2CONFIGGPB_CORPUS.containing_type = _KEY2CONFIGGPB;
_TYPE5CONFIGGPB.fields_by_name['k1opt'].message_type = _KEY1CONFIGGPB
_TYPE5CONFIGGPB.fields_by_name['t1rep'].message_type = _TYPE1CONFIGGPB
_TYPE5CONFIGGPB.fields_by_name['t1repListControl'].message_type = include.a.infra.config.config_types_pb2._LISTCONTROLGPB
_TYPEBADCONFIG2GPB.fields_by_name['attr2'].message_type = _TYPEBADCONFIG1GPB
_TYPEBADCONFIG5GPB.fields_by_name['attr3'].message_type = include.a.infra.config.config_types_pb2._LISTCONTROLGPB
_TYPEBADCONFIG6GPB.fields_by_name['attr1'].message_type = include.a.infra.config.config_types_pb2._LISTCONTROLGPB
_TYPEBADCONFIG7GPB.fields_by_name['stuffListCon'].message_type = include.a.infra.config.config_types_pb2._LISTCONTROLGPB

class Type1ConfigGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPE1CONFIGGPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.Type1ConfigGpb)

class Type2ConfigGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPE2CONFIGGPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.Type2ConfigGpb)

class Type3ConfigGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPE3CONFIGGPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.Type3ConfigGpb)

class Key1ConfigGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KEY1CONFIGGPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.Key1ConfigGpb)

class Key2ConfigGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _KEY2CONFIGGPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.Key2ConfigGpb)

class Type4KeyConfigGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPE4KEYCONFIGGPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.Type4KeyConfigGpb)

class Type4ConfigGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPE4CONFIGGPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.Type4ConfigGpb)

class Type5ConfigGpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPE5CONFIGGPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.Type5ConfigGpb)

class TypeBadConfig1Gpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPEBADCONFIG1GPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.TypeBadConfig1Gpb)

class TypeBadConfig2Gpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPEBADCONFIG2GPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.TypeBadConfig2Gpb)

class TypeBadConfig3Gpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPEBADCONFIG3GPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.TypeBadConfig3Gpb)

class TypeBadConfig4Gpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPEBADCONFIG4GPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.TypeBadConfig4Gpb)

class TypeBadConfig5Gpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPEBADCONFIG5GPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.TypeBadConfig5Gpb)

class TypeBadConfig6Gpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPEBADCONFIG6GPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.TypeBadConfig6Gpb)

class TypeBadConfig7Gpb(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TYPEBADCONFIG7GPB
  
  # @@protoc_insertion_point(class_scope:a.config.utm.TypeBadConfig7Gpb)

# @@protoc_insertion_point(module_scope)
