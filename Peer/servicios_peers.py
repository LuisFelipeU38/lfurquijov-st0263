from globals import puerto_usuario, lista_archivos, usuario_unico
import peerServidor_pb2, peerServidor_pb2_grpc

class ServicioEntrePares(peerServidor_pb2_grpc.ServicioEntrePeersServicer):

    def ObtenerPuertoParaUsuario(self, solicitud, contexto):
        usuario = solicitud.usuario
        if usuario == usuario_unico:
            return peerServidor_pb2.RespuestaPuerto(puerto=puerto_usuario)
        else:
            return peerServidor_pb2.RespuestaPuerto(puerto="PuertoInválido") 

    def EstablecerPuertoUsuario(self, solicitud, contexto):
        usuario = solicitud.usuario
        global usuario_unico
        if usuario_unico == None:
            usuario_unico = usuario
            return peerServidor_pb2.Respuesta(exito=True)
        elif usuario_unico == 'logout':
            usuario_unico = None
            return peerServidor_pb2.Respuesta(exito=False)
        else:
            return peerServidor_pb2.Respuesta(exito=False)
        
    def ObtenerArchivo(self, solicitud, contexto):
        nombre_archivo = solicitud.nombre_archivo
        if nombre_archivo in lista_archivos:
            return peerServidor_pb2.RespuestaArchivo(contenido=nombre_archivo)
        else:
            return peerServidor_pb2.RespuestaArchivo(contenido="El Archivo '{}' se ha encontrado".format(nombre_archivo))

    def CrearArchivo(self, solicitud, contexto):
        nombre_archivo = solicitud.nombre_archivo
        global lista_archivos
        for archivo in nombre_archivo:
            lista_archivos.append(archivo)
        return peerServidor_pb2.RespuestaCrearArchivo(exito=True)