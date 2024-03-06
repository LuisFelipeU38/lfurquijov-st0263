import random
from globals import grpc_puertos
from funciones_grpc import ServicioGRPC
from rutas import ServicioREST

def imprimir_menu(conectado):
    if not conectado:
        print("1. Iniciar sesión en el servidor")
        print("2. Salir")
    else:
        print("1. Obtener archivo")
        print("2. Buscar archivo en el servidor")
        print("3. Agregar archivos en el servidor")
        print("4. Cerrar sesión en el servidor")
        print("5. Salir")

def manejar_sesion(servicio_rest, servicio_grpc, archivos):
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    ip = input("Ingrese dirección IP: ")
    respuesta_inicio_sesion = servicio_rest.inicio_sesion(usuario, contraseña, ip)
    if respuesta_inicio_sesion.get('ingreso'):
        for puerto in range(50051, 50061):
            if not servicio_grpc.establecer_puerto_usuario(usuario):
                grpc_puertos = f'localhost:{puerto}'
            else:
                servicio_grpc.crear_archivo(archivos)
                break
    print("Respuesta del servidor:", respuesta_inicio_sesion)
    return respuesta_inicio_sesion, usuario

def principal():
    servicio_grpc = ServicioGRPC()
    servicio_rest = ServicioREST()
    archivos = [servicio_grpc.generar_cadena() for _ in range(1, random.randint(2, 5))]
    conectado = False 

    while True:
        print("\nAPI REST:")
        imprimir_menu(conectado)
        opcion = input("API REST: ")

        if opcion == '1':
            if not conectado:
                respuesta_inicio_sesion, usuario = manejar_sesion(servicio_rest, servicio_grpc, archivos)
                conectado = respuesta_inicio_sesion.get('ingreso')
            else:
                nombre_archivo = archivo_busqueda
                puerto_servidor = puerto_busqueda 
                respuesta_grpc = servicio_grpc.obtener_archivo(nombre_archivo, puerto_servidor)
                archivos.append(respuesta_grpc)
                servicio_grpc.crear_archivo(respuesta_grpc)
                print("Respuesta del servidor:", respuesta_grpc)
        elif opcion == '2':
            if not conectado:
                print("Saliendo...")
                break
            else:
                nombre_archivo = input("Archivo a buscar: ")
                respuesta_buscar = servicio_rest.buscar(nombre_archivo)
                if respuesta_buscar:
                    archivo_busqueda = respuesta_buscar['nombre_archivo']
                    puerto_busqueda = respuesta_buscar['puerto']
                print("Respuesta del servidor:", respuesta_buscar)
        elif opcion == '3':
            if not conectado:
                print("Opción inválida. Por favor inicie sesión primero.")
            else:
                respuesta_indexar = servicio_rest.indexar(usuario, archivos)
                print("Respuesta de indexación del servidor:", respuesta_indexar)
        elif opcion == '4':
            if not conectado:
                print("Opción inválida. Por favor inicie sesión primero.")
            else:
                print("Cerrando sesión en el servidor...")
                respuesta_cerrar_sesion = servicio_rest.cerrar_sesion(usuario)
                if respuesta_cerrar_sesion.get('mensaje') == 'Sesión cerrada exitosamente':
                    servicio_grpc.establecer_puerto_usuario("logout")
                    conectado = False
                print("Respuesta de cierre de sesión del servidor:", respuesta_cerrar_sesion)
                print("Saliendo...")
                break
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Por favor ingrese un número entre 1 y 5.")

if __name__ == '__main__':
    principal()