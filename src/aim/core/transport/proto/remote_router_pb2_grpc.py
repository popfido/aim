# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
# temporary workaround for M1 build
try:
    import grpc
except ImportError:
    grpc = None

import aim.core.transport.proto.remote_router_pb2 as remote__router__pb2


class RemoteRouterServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.client_heartbeat = channel.unary_unary(
                '/RemoteRouterService/client_heartbeat',
                request_serializer=remote__router__pb2.HeartbeatRequest.SerializeToString,
                response_deserializer=remote__router__pb2.HeartbeatResponse.FromString,
                )
        self.get_version = channel.unary_unary(
                '/RemoteRouterService/get_version',
                request_serializer=remote__router__pb2.VersionRequest.SerializeToString,
                response_deserializer=remote__router__pb2.VersionResponse.FromString,
                )
        self.connect = channel.unary_unary(
                '/RemoteRouterService/connect',
                request_serializer=remote__router__pb2.ConnectRequest.SerializeToString,
                response_deserializer=remote__router__pb2.ConnectResponse.FromString,
                )
        self.reconnect = channel.unary_unary(
                '/RemoteRouterService/reconnect',
                request_serializer=remote__router__pb2.ReconnectRequest.SerializeToString,
                response_deserializer=remote__router__pb2.ReconnectResponse.FromString,
                )
        self.disconnect = channel.unary_unary(
                '/RemoteRouterService/disconnect',
                request_serializer=remote__router__pb2.DisconnectRequest.SerializeToString,
                response_deserializer=remote__router__pb2.DisconnectResponse.FromString,
                )


class RemoteRouterServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def client_heartbeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_version(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def connect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def reconnect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def disconnect(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RemoteRouterServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'client_heartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.client_heartbeat,
                    request_deserializer=remote__router__pb2.HeartbeatRequest.FromString,
                    response_serializer=remote__router__pb2.HeartbeatResponse.SerializeToString,
            ),
            'get_version': grpc.unary_unary_rpc_method_handler(
                    servicer.get_version,
                    request_deserializer=remote__router__pb2.VersionRequest.FromString,
                    response_serializer=remote__router__pb2.VersionResponse.SerializeToString,
            ),
            'connect': grpc.unary_unary_rpc_method_handler(
                    servicer.connect,
                    request_deserializer=remote__router__pb2.ConnectRequest.FromString,
                    response_serializer=remote__router__pb2.ConnectResponse.SerializeToString,
            ),
            'reconnect': grpc.unary_unary_rpc_method_handler(
                    servicer.reconnect,
                    request_deserializer=remote__router__pb2.ReconnectRequest.FromString,
                    response_serializer=remote__router__pb2.ReconnectResponse.SerializeToString,
            ),
            'disconnect': grpc.unary_unary_rpc_method_handler(
                    servicer.disconnect,
                    request_deserializer=remote__router__pb2.DisconnectRequest.FromString,
                    response_serializer=remote__router__pb2.DisconnectResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'RemoteRouterService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RemoteRouterService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def client_heartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RemoteRouterService/client_heartbeat',
            remote__router__pb2.HeartbeatRequest.SerializeToString,
            remote__router__pb2.HeartbeatResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_version(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RemoteRouterService/get_version',
            remote__router__pb2.VersionRequest.SerializeToString,
            remote__router__pb2.VersionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def connect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RemoteRouterService/connect',
            remote__router__pb2.ConnectRequest.SerializeToString,
            remote__router__pb2.ConnectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def reconnect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RemoteRouterService/reconnect',
            remote__router__pb2.ReconnectRequest.SerializeToString,
            remote__router__pb2.ReconnectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def disconnect(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/RemoteRouterService/disconnect',
            remote__router__pb2.DisconnectRequest.SerializeToString,
            remote__router__pb2.DisconnectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
