import requests
from globals import grpc_puertos

class ServicioREST:
    def __init__(self):
        self.base_url = 'http://localhost:5000'

    def inicio_sesion(self, usuario, contrasena_peer, ip):
        url = f'{self.base_url}/login'
        datos = {'usuario': usuario, 'contraseña': contrasena_peer, 'ip': ip}
        respuesta = requests.post(url, json=datos)
        return respuesta.json()

    def cerrar_sesion(self, usuario):
        url = f'{self.base_url}/logout'
        datos = {'usuario': usuario}
        respuesta = requests.post(url, json=datos)
        return respuesta.json()

    def indexar(self, usuario, archivos):
        url = f'{self.base_url}/index'
        datos = {'usuario': usuario, 'archivos': archivos, 'puerto': grpc_puertos}
        respuesta = requests.post(url, json=datos)
        return respuesta.json()

    def buscar(self, nombre_archivo):
        url = f'{self.base_url}/search'
        parametros = {'nombre_archivo': nombre_archivo}
        respuesta = requests.get(url, params=parametros)
        if respuesta.status_code == 200:
            return respuesta.json()
        else: 
            return False