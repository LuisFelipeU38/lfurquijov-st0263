from concurrent import futures
from globals import puerto_usuario,  UN_DIA_EN_SEGUNDOS
import peerServidor_pb2_grpc
from servicios_peers import ServicioEntrePares
import time, grpc

def puerto_server():
    global puerto_usuario
    for puerto in range(50051, 50061):
        servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        peerServidor_pb2_grpc.add_ServicioEntrePeersServicer_to_server(ServicioEntrePares(), servidor)
        try:
            puerto_usuario = puerto
            servidor.add_insecure_port('[::]:{}'.format(puerto))
            servidor.start()
            print("Servidor en el puerto {}...".format(puerto))
            break 
        except Exception as e:
            print("Puerto en uso {}. Intentando otro puerto...".format(puerto))
            if puerto == 50060:
                print("Ningún puerto disponible.")
                return
    try:
        while True:
            time.sleep(UN_DIA_EN_SEGUNDOS)
    except KeyboardInterrupt:
        servidor.stop(0)

if __name__ == '__main__':
    puerto_server()
