# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import peerServidor_pb2 as peerServidor__pb2


class ServicioEntrePeersStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ObtenerPuertoParaUsuario = channel.unary_unary(
                '/ServicioEntrePeers/ObtenerPuertoParaUsuario',
                request_serializer=peerServidor__pb2.SolicitudPuertoParaUsuario.SerializeToString,
                response_deserializer=peerServidor__pb2.RespuestaPuerto.FromString,
                )
        self.EstablecerPuertoUsuario = channel.unary_unary(
                '/ServicioEntrePeers/EstablecerPuertoUsuario',
                request_serializer=peerServidor__pb2.SolicitudPuertoUsuario.SerializeToString,
                response_deserializer=peerServidor__pb2.Respuesta.FromString,
                )
        self.ObtenerArchivo = channel.unary_unary(
                '/ServicioEntrePeers/ObtenerArchivo',
                request_serializer=peerServidor__pb2.SolicitudArchivo.SerializeToString,
                response_deserializer=peerServidor__pb2.RespuestaArchivo.FromString,
                )
        self.CrearArchivo = channel.unary_unary(
                '/ServicioEntrePeers/CrearArchivo',
                request_serializer=peerServidor__pb2.SolicitudCrearArchivo.SerializeToString,
                response_deserializer=peerServidor__pb2.RespuestaCrearArchivo.FromString,
                )


class ServicioEntrePeersServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ObtenerPuertoParaUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EstablecerPuertoUsuario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ObtenerArchivo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CrearArchivo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServicioEntrePeersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ObtenerPuertoParaUsuario': grpc.unary_unary_rpc_method_handler(
                    servicer.ObtenerPuertoParaUsuario,
                    request_deserializer=peerServidor__pb2.SolicitudPuertoParaUsuario.FromString,
                    response_serializer=peerServidor__pb2.RespuestaPuerto.SerializeToString,
            ),
            'EstablecerPuertoUsuario': grpc.unary_unary_rpc_method_handler(
                    servicer.EstablecerPuertoUsuario,
                    request_deserializer=peerServidor__pb2.SolicitudPuertoUsuario.FromString,
                    response_serializer=peerServidor__pb2.Respuesta.SerializeToString,
            ),
            'ObtenerArchivo': grpc.unary_unary_rpc_method_handler(
                    servicer.ObtenerArchivo,
                    request_deserializer=peerServidor__pb2.SolicitudArchivo.FromString,
                    response_serializer=peerServidor__pb2.RespuestaArchivo.SerializeToString,
            ),
            'CrearArchivo': grpc.unary_unary_rpc_method_handler(
                    servicer.CrearArchivo,
                    request_deserializer=peerServidor__pb2.SolicitudCrearArchivo.FromString,
                    response_serializer=peerServidor__pb2.RespuestaCrearArchivo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ServicioEntrePeers', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ServicioEntrePeers(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ObtenerPuertoParaUsuario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ServicioEntrePeers/ObtenerPuertoParaUsuario',
            peerServidor__pb2.SolicitudPuertoParaUsuario.SerializeToString,
            peerServidor__pb2.RespuestaPuerto.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EstablecerPuertoUsuario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ServicioEntrePeers/EstablecerPuertoUsuario',
            peerServidor__pb2.SolicitudPuertoUsuario.SerializeToString,
            peerServidor__pb2.Respuesta.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ObtenerArchivo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ServicioEntrePeers/ObtenerArchivo',
            peerServidor__pb2.SolicitudArchivo.SerializeToString,
            peerServidor__pb2.RespuestaArchivo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CrearArchivo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ServicioEntrePeers/CrearArchivo',
            peerServidor__pb2.SolicitudCrearArchivo.SerializeToString,
            peerServidor__pb2.RespuestaCrearArchivo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
