import grpc
import peerServidor_pb2
import peerServidor_pb2_grpc
import random
from globals import grpc_puertos

class ServicioGRPC:
    def __init__(self):
        self.canal = grpc.insecure_channel(grpc_puertos)
        self.cliente = peerServidor_pb2_grpc.ServicioEntrePeersStub(self.canal)

    def obtener_archivo(self, nombre_archivo, puerto):
        canal = grpc.insecure_channel(puerto)
        cliente = peerServidor_pb2_grpc.ServicioEntrePeersStub(canal)
        respuesta = cliente.ObtenerArchivo(peerServidor_pb2.SolicitudArchivo(nombre_archivo=nombre_archivo))
        return respuesta.contenido

    def crear_archivo(self, archivos):
        respuesta = self.cliente.CrearArchivo(peerServidor_pb2.SolicitudCrearArchivo(nombre_archivo=archivos))
        return respuesta.exito

    def establecer_puerto_usuario(self, usuario):
        respuesta = self.cliente.EstablecerPuertoUsuario(peerServidor_pb2.SolicitudPuertoUsuario(usuario=usuario))
        return respuesta.exito

    def obtener_puerto_para_usuario(self, usuario):
        respuesta = self.cliente.ObtenerPuertoParaUsuario(peerServidor_pb2.SolicitudPuertoParaUsuario(usuario=usuario))
        return respuesta.puerto

    def generar_cadena(self):
        numero_aleatorio = random.randint(1, 30)
        resultado = "archivo" + str(numero_aleatorio)
        return resultado