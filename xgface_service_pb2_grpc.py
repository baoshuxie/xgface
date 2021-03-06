# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import xgface_service_pb2 as xgface__service__pb2


class XgfaceServiceStub(object):
  """Interface exported by the server.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetFeature = channel.unary_unary(
        '/xgface.XgfaceService/GetFeature',
        request_serializer=xgface__service__pb2.Request.SerializeToString,
        response_deserializer=xgface__service__pb2.Features.FromString,
        )
    self.GetBox = channel.unary_unary(
        '/xgface.XgfaceService/GetBox',
        request_serializer=xgface__service__pb2.Request.SerializeToString,
        response_deserializer=xgface__service__pb2.Boxs.FromString,
        )
    self.GetLandmark = channel.unary_unary(
        '/xgface.XgfaceService/GetLandmark',
        request_serializer=xgface__service__pb2.Request.SerializeToString,
        response_deserializer=xgface__service__pb2.Landmarks.FromString,
        )
    self.GetDetectInfo = channel.unary_unary(
        '/xgface.XgfaceService/GetDetectInfo',
        request_serializer=xgface__service__pb2.Request.SerializeToString,
        response_deserializer=xgface__service__pb2.DetectInfo.FromString,
        )
    self.GetDetectInfo_mutli_images = channel.unary_unary(
        '/xgface.XgfaceService/GetDetectInfo_mutli_images',
        request_serializer=xgface__service__pb2.Request.SerializeToString,
        response_deserializer=xgface__service__pb2.DetectInfos.FromString,
        )


class XgfaceServiceServicer(object):
  """Interface exported by the server.
  """

  def GetFeature(self, request, context):
    """xgface RPC service

    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetBox(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLandmark(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDetectInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDetectInfo_mutli_images(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_XgfaceServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetFeature': grpc.unary_unary_rpc_method_handler(
          servicer.GetFeature,
          request_deserializer=xgface__service__pb2.Request.FromString,
          response_serializer=xgface__service__pb2.Features.SerializeToString,
      ),
      'GetBox': grpc.unary_unary_rpc_method_handler(
          servicer.GetBox,
          request_deserializer=xgface__service__pb2.Request.FromString,
          response_serializer=xgface__service__pb2.Boxs.SerializeToString,
      ),
      'GetLandmark': grpc.unary_unary_rpc_method_handler(
          servicer.GetLandmark,
          request_deserializer=xgface__service__pb2.Request.FromString,
          response_serializer=xgface__service__pb2.Landmarks.SerializeToString,
      ),
      'GetDetectInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetDetectInfo,
          request_deserializer=xgface__service__pb2.Request.FromString,
          response_serializer=xgface__service__pb2.DetectInfo.SerializeToString,
      ),
      'GetDetectInfo_mutli_images': grpc.unary_unary_rpc_method_handler(
          servicer.GetDetectInfo_mutli_images,
          request_deserializer=xgface__service__pb2.Request.FromString,
          response_serializer=xgface__service__pb2.DetectInfos.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'xgface.XgfaceService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
