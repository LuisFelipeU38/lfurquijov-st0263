from flask import Flask, jsonify, request

app = Flask(__name__)

base_de_datos = {}
base_de_datos_ips = {}

# implementación de métodos en API REST: login(), index(), search(), logout() .

# El método login() permitirá al servidor almacenar el usuario, contraseña e ip del peer que inicia sesión. 
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
    return jsonify({'mensaje': 'Inicio de sesión exitoso', 'ingreso': True, 'identificador_peer': identificador_peer, 'contraseña_peer': contrasena_peer, 'ip': ip_peer}), 200

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
        return jsonify({'mensaje': 'Indexación exitosa', 'identificador_peer': identificador_peer, 'archivos': archivos}), 200
    else:
        return jsonify({'mensaje': 'Este peer no existe ', 'identificador_peer': identificador_peer}), 404

@app.route('/search', methods=['GET'])
def buscar():
    global base_de_datos
    global base_de_datos_ips
    nombre_archivo = request.args.get('nombre_archivo')
    for identificador_peer, info in base_de_datos.items():
        print(identificador_peer, " ", info)
        if 'archivos' in info and nombre_archivo in info['archivos']:
            return jsonify({'mensaje': 'Archivo encontrado', 'usuario': identificador_peer, 'nombre_archivo': nombre_archivo, 'puerto': base_de_datos_ips[identificador_peer]}), 200
    return jsonify({'error': 'Archivo no encontrado'}), 404

@app.route('/logout', methods=['POST'])
def logout():
    global base_de_datos
    global base_de_datos_ips
    datos = request.json
    identificador_peer = datos['usuario']
    if identificador_peer in base_de_datos:
        del base_de_datos[identificador_peer]
        del base_de_datos_ips[identificador_peer]
        return jsonify({'mensaje': 'Cierre de sesión exitoso', 'identificador_peer': identificador_peer}), 200
    else:
        return jsonify({'error': 'Peer no encontrado'}), 404
    
if __name__ == '__main__':
    app.run(debug=True)
