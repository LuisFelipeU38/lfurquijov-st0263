from flask import Flask, jsonify, request

app = Flask(__name__)

base_de_datos = {}
base_de_datos_ips = {}

# Método login(): permite al servidor almacenar el usuario, contraseña e ip del peer que inicia sesión.
@app.route('/login', methods=['POST'])
def login():
    global base_de_datos
    global base_de_datos_ips
    datos = request.json
    identificador_peer = datos['usuario']
    contrasena_peer = datos["contraseña"]
    ip_peer = datos["ip"]
    base_de_datos[identificador_peer] = {}
    base_de_datos_ips[identificador_peer] = ip_peer
    return jsonify({'ingreso': True, 'identificador_peer': identificador_peer, 'contraseña_peer': contrasena_peer, 'ip': ip_peer}), 200

# Método index(): permite al servidor almacenar los archivos de un peer.
@app.route('/index', methods=['POST'])
def index():
    global base_de_datos
    global base_de_datos_ips
    datos = request.json
    identificador_peer = datos['usuario']
    puerto = datos['puerto']
    if identificador_peer in base_de_datos:
        archivos = datos['archivos']
        base_de_datos[identificador_peer]['archivos'] = archivos
        base_de_datos_ips[identificador_peer] = puerto
        return jsonify({'identificador_peer': identificador_peer, 'archivos': archivos}), 200
    else:
        return jsonify({'error': 'Este peer no existe ', 'identificador_peer': identificador_peer}), 404

# Método buscar(): permite buscar un archivo en los peers almacenados en el servidor.
@app.route('/search', methods=['GET'])
def buscar():
    global base_de_datos
    global base_de_datos_ips
    nombre_archivo = request.args.get('nombre_archivo')
    for identificador_peer, info in base_de_datos.items():
        print(identificador_peer, " ", info)
        if 'archivos' in info and nombre_archivo in info['archivos']:
            return jsonify({'usuario': identificador_peer, 'nombre_archivo': nombre_archivo, 'puerto': base_de_datos_ips[identificador_peer]}), 200
    return jsonify({'error': 'Archivo no encontrado'}), 404

# Método logout(): permite cerrar sesión de un peer en el servidor.
@app.route('/logout', methods=['POST'])
def logout():
    global base_de_datos
    global base_de_datos_ips
    datos = request.json
    identificador_peer = datos['usuario']
    if identificador_peer in base_de_datos:
        del base_de_datos[identificador_peer]
        del base_de_datos_ips[identificador_peer]
        return jsonify({'identificador_peer': identificador_peer}), 200
    else:
        return jsonify({'error': 'Peer no encontrado'}), 404
    
if __name__ == '__main__':
    app.run(debug=True)


