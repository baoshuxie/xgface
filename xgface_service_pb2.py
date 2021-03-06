# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xgface_service.proto

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
  name='xgface_service.proto',
  package='xgface',
  syntax='proto3',
  serialized_pb=_b('\n\x14xgface_service.proto\x12\x06xgface\"\x19\n\x07Request\x12\x0e\n\x06images\x18\x01 \x03(\t\"3\n\x05Point\x12\x14\n\x0c\x63oordinate_x\x18\x01 \x01(\x02\x12\x14\n\x0c\x63oordinate_y\x18\x02 \x01(\x02\"%\n\x04Rect\x12\r\n\x05width\x18\x01 \x01(\x02\x12\x0e\n\x06height\x18\x02 \x01(\x02\"\x19\n\x07\x46\x65\x61ture\x12\x0e\n\x06values\x18\x01 \x03(\x02\"-\n\x08\x46\x65\x61tures\x12!\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32\x0f.xgface.Feature\"O\n\x03\x42ox\x12\x1d\n\x06\x63\x65nter\x18\x01 \x01(\x0b\x32\r.xgface.Point\x12\x1a\n\x04rect\x18\x02 \x01(\x0b\x32\x0c.xgface.Rect\x12\r\n\x05score\x18\x03 \x01(\x02\"!\n\x04\x42oxs\x12\x19\n\x04\x62oxs\x18\x01 \x03(\x0b\x32\x0b.xgface.Box\"8\n\x08Landmark\x12\x1d\n\x06points\x18\x01 \x03(\x0b\x32\r.xgface.Point\x12\r\n\x05score\x18\x02 \x01(\x02\"0\n\tLandmarks\x12#\n\tlandmarks\x18\x01 \x03(\x0b\x32\x10.xgface.Landmark\"\xf5\x01\n\x04\x46\x61\x63\x65\x12\x18\n\x03\x62ox\x18\x01 \x01(\x0b\x32\x0b.xgface.Box\x12\"\n\x08landmark\x18\x02 \x01(\x0b\x32\x10.xgface.Landmark\x12 \n\x07\x66\x65\x61ture\x18\x03 \x01(\x0b\x32\x0f.xgface.Feature\x12\x30\n\nattributes\x18\x04 \x03(\x0b\x32\x1c.xgface.Face.AttributesEntry\x12\r\n\x05pitch\x18\x05 \x01(\x02\x12\x0b\n\x03yaw\x18\x06 \x01(\x02\x12\x0c\n\x04roll\x18\x07 \x01(\x02\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x02\x38\x01\")\n\nDetectInfo\x12\x1b\n\x05\x66\x61\x63\x65s\x18\x01 \x03(\x0b\x32\x0c.xgface.Face\"6\n\x0b\x44\x65tectInfos\x12\'\n\x0b\x64\x65tectinfos\x18\x01 \x03(\x0b\x32\x12.xgface.DetectInfo2\xa0\x02\n\rXgfaceService\x12\x31\n\nGetFeature\x12\x0f.xgface.Request\x1a\x10.xgface.Features\"\x00\x12)\n\x06GetBox\x12\x0f.xgface.Request\x1a\x0c.xgface.Boxs\"\x00\x12\x33\n\x0bGetLandmark\x12\x0f.xgface.Request\x1a\x11.xgface.Landmarks\"\x00\x12\x36\n\rGetDetectInfo\x12\x0f.xgface.Request\x1a\x12.xgface.DetectInfo\"\x00\x12\x44\n\x1aGetDetectInfo_mutli_images\x12\x0f.xgface.Request\x1a\x13.xgface.DetectInfos\"\x00\x42,\n\x15\x63om.xgrobotics.xgfaceB\x0bXgfaceProtoP\x01\xa2\x02\x03XGFb\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='xgface.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='images', full_name='xgface.Request.images', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=32,
  serialized_end=57,
)


_POINT = _descriptor.Descriptor(
  name='Point',
  full_name='xgface.Point',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='coordinate_x', full_name='xgface.Point.coordinate_x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coordinate_y', full_name='xgface.Point.coordinate_y', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_start=59,
  serialized_end=110,
)


_RECT = _descriptor.Descriptor(
  name='Rect',
  full_name='xgface.Rect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='width', full_name='xgface.Rect.width', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='xgface.Rect.height', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_start=112,
  serialized_end=149,
)


_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='xgface.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='xgface.Feature.values', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=151,
  serialized_end=176,
)


_FEATURES = _descriptor.Descriptor(
  name='Features',
  full_name='xgface.Features',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='xgface.Features.features', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=178,
  serialized_end=223,
)


_BOX = _descriptor.Descriptor(
  name='Box',
  full_name='xgface.Box',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='center', full_name='xgface.Box.center', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rect', full_name='xgface.Box.rect', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='xgface.Box.score', index=2,
      number=3, type=2, cpp_type=6, label=1,
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
  serialized_start=225,
  serialized_end=304,
)


_BOXS = _descriptor.Descriptor(
  name='Boxs',
  full_name='xgface.Boxs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boxs', full_name='xgface.Boxs.boxs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=306,
  serialized_end=339,
)


_LANDMARK = _descriptor.Descriptor(
  name='Landmark',
  full_name='xgface.Landmark',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='points', full_name='xgface.Landmark.points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='xgface.Landmark.score', index=1,
      number=2, type=2, cpp_type=6, label=1,
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
  serialized_start=341,
  serialized_end=397,
)


_LANDMARKS = _descriptor.Descriptor(
  name='Landmarks',
  full_name='xgface.Landmarks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='landmarks', full_name='xgface.Landmarks.landmarks', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=399,
  serialized_end=447,
)


_FACE_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='xgface.Face.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='xgface.Face.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='xgface.Face.AttributesEntry.value', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=646,
  serialized_end=695,
)

_FACE = _descriptor.Descriptor(
  name='Face',
  full_name='xgface.Face',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='box', full_name='xgface.Face.box', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landmark', full_name='xgface.Face.landmark', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feature', full_name='xgface.Face.feature', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='xgface.Face.attributes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pitch', full_name='xgface.Face.pitch', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yaw', full_name='xgface.Face.yaw', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roll', full_name='xgface.Face.roll', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FACE_ATTRIBUTESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=450,
  serialized_end=695,
)


_DETECTINFO = _descriptor.Descriptor(
  name='DetectInfo',
  full_name='xgface.DetectInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='faces', full_name='xgface.DetectInfo.faces', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=697,
  serialized_end=738,
)


_DETECTINFOS = _descriptor.Descriptor(
  name='DetectInfos',
  full_name='xgface.DetectInfos',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='detectinfos', full_name='xgface.DetectInfos.detectinfos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=740,
  serialized_end=794,
)

_FEATURES.fields_by_name['features'].message_type = _FEATURE
_BOX.fields_by_name['center'].message_type = _POINT
_BOX.fields_by_name['rect'].message_type = _RECT
_BOXS.fields_by_name['boxs'].message_type = _BOX
_LANDMARK.fields_by_name['points'].message_type = _POINT
_LANDMARKS.fields_by_name['landmarks'].message_type = _LANDMARK
_FACE_ATTRIBUTESENTRY.containing_type = _FACE
_FACE.fields_by_name['box'].message_type = _BOX
_FACE.fields_by_name['landmark'].message_type = _LANDMARK
_FACE.fields_by_name['feature'].message_type = _FEATURE
_FACE.fields_by_name['attributes'].message_type = _FACE_ATTRIBUTESENTRY
_DETECTINFO.fields_by_name['faces'].message_type = _FACE
_DETECTINFOS.fields_by_name['detectinfos'].message_type = _DETECTINFO
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Point'] = _POINT
DESCRIPTOR.message_types_by_name['Rect'] = _RECT
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['Features'] = _FEATURES
DESCRIPTOR.message_types_by_name['Box'] = _BOX
DESCRIPTOR.message_types_by_name['Boxs'] = _BOXS
DESCRIPTOR.message_types_by_name['Landmark'] = _LANDMARK
DESCRIPTOR.message_types_by_name['Landmarks'] = _LANDMARKS
DESCRIPTOR.message_types_by_name['Face'] = _FACE
DESCRIPTOR.message_types_by_name['DetectInfo'] = _DETECTINFO
DESCRIPTOR.message_types_by_name['DetectInfos'] = _DETECTINFOS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'xgface_service_pb2'
  # @@protoc_insertion_point(class_scope:xgface.Request)
  ))
_sym_db.RegisterMessage(Request)

Point = _reflection.GeneratedProtocolMessageType('Point', (_message.Message,), dict(
  DESCRIPTOR = _POINT,
  __module__ = 'xgface_service_pb2'
  # @@protoc_insertion_point(class_scope:xgface.Point)
  ))
_sym_db.RegisterMessage(Point)

Rect = _reflection.GeneratedProtocolMessageType('Rect', (_message.Message,), dict(
  DESCRIPTOR = _RECT,
  __module__ = 'xgface_service_pb2'
  # @@protoc_insertion_point(class_scope:xgface.Rect)
  ))
_sym_db.RegisterMessage(Rect)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), dict(
  DESCRIPTOR = _FEATURE,
  __module__ = 'xgface_service_pb2'
  # @@protoc_insertion_point(class_scope:xgface.Feature)
  ))
_sym_db.RegisterMessage(Feature)

Features = _reflection.GeneratedProtocolMessageType('Features', (_message.Message,), dict(
  DESCRIPTOR = _FEATURES,
  __module__ = 'xgface_service_pb2'
  # @@protoc_insertion_point(class_scope:xgface.Features)
  ))
_sym_db.RegisterMessage(Features)

Box = _reflection.GeneratedProtocolMessageType('Box', (_message.Message,), dict(
  DESCRIPTOR = _BOX,
  __module__ = 'xgface_service_pb2'
  # @@protoc_insertion_point(class_scope:xgface.Box)
  ))
_sym_db.RegisterMessage(Box)

Boxs = _reflection.GeneratedProtocolMessageType('Boxs', (_message.Message,), dict(
  DESCRIPTOR = _BOXS,
  __module__ = 'xgface_service_pb2'
  # @@protoc_insertion_point(class_scope:xgface.Boxs)
  ))
_sym_db.RegisterMessage(Boxs)

Landmark = _reflection.GeneratedProtocolMessageType('Landmark', (_message.Message,), dict(
  DESCRIPTOR = _LANDMARK,
  __module__ = 'xgface_service_pb2'
  # @@protoc_insertion_point(class_scope:xgface.Landmark)
  ))
_sym_db.RegisterMessage(Landmark)

Landmarks = _reflection.GeneratedProtocolMessageType('Landmarks', (_message.Message,), dict(
  DESCRIPTOR = _LANDMARKS,
  __module__ = 'xgface_service_pb2'
  # @@protoc_insertion_point(class_scope:xgface.Landmarks)
  ))
_sym_db.RegisterMessage(Landmarks)

Face = _reflection.GeneratedProtocolMessageType('Face', (_message.Message,), dict(

  AttributesEntry = _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), dict(
    DESCRIPTOR = _FACE_ATTRIBUTESENTRY,
    __module__ = 'xgface_service_pb2'
    # @@protoc_insertion_point(class_scope:xgface.Face.AttributesEntry)
    ))
  ,
  DESCRIPTOR = _FACE,
  __module__ = 'xgface_service_pb2'
  # @@protoc_insertion_point(class_scope:xgface.Face)
  ))
_sym_db.RegisterMessage(Face)
_sym_db.RegisterMessage(Face.AttributesEntry)

DetectInfo = _reflection.GeneratedProtocolMessageType('DetectInfo', (_message.Message,), dict(
  DESCRIPTOR = _DETECTINFO,
  __module__ = 'xgface_service_pb2'
  # @@protoc_insertion_point(class_scope:xgface.DetectInfo)
  ))
_sym_db.RegisterMessage(DetectInfo)

DetectInfos = _reflection.GeneratedProtocolMessageType('DetectInfos', (_message.Message,), dict(
  DESCRIPTOR = _DETECTINFOS,
  __module__ = 'xgface_service_pb2'
  # @@protoc_insertion_point(class_scope:xgface.DetectInfos)
  ))
_sym_db.RegisterMessage(DetectInfos)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025com.xgrobotics.xgfaceB\013XgfaceProtoP\001\242\002\003XGF'))
_FACE_ATTRIBUTESENTRY.has_options = True
_FACE_ATTRIBUTESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_XGFACESERVICE = _descriptor.ServiceDescriptor(
  name='XgfaceService',
  full_name='xgface.XgfaceService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=797,
  serialized_end=1085,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetFeature',
    full_name='xgface.XgfaceService.GetFeature',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_FEATURES,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBox',
    full_name='xgface.XgfaceService.GetBox',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_BOXS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetLandmark',
    full_name='xgface.XgfaceService.GetLandmark',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_LANDMARKS,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetDetectInfo',
    full_name='xgface.XgfaceService.GetDetectInfo',
    index=3,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_DETECTINFO,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetDetectInfo_mutli_images',
    full_name='xgface.XgfaceService.GetDetectInfo_mutli_images',
    index=4,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_DETECTINFOS,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_XGFACESERVICE)

DESCRIPTOR.services_by_name['XgfaceService'] = _XGFACESERVICE

# @@protoc_insertion_point(module_scope)
