# Info de la materia: ST0263 Topicos especiales en Telematica.

## Estudiante(s):
- **Luis Felipe Urquijo Vargas** 
- **lfurquijov@eafit.edu.co** 

## Profesor:
- **Nombre:** Alvaro Enrique Ospina Sanjuan
- **Correo Electrónico:** aeospinas@eafit.edu.co

## Reto 1 y 2.

## 1. Breve descripción de la actividad.

1.1 El reto consiste en diseñar e implementar una comunicación basada en una red p2p no estructurada y basada en un servidor central. Se logro simular la implementación de la red creando un servidor central que se encargara de recibir las solicitudes http y donde se encuentran definidas la implementación de los métodos login(), index(), search(), logout() que permitirán la comunicación API REST con los peers. También se simulo el funcionamiento de los peers, desde la comunicación con el servidor central para manejar las request y responses correspondientes hasta la comunicación gRPC del cliente de cada peer con el servidor de otro peer. 

1.2 No se cumplieron aspectos como despliegue en un entorno virtual o distinto a local. No se simulo descarga de archivos reales y tampoco se trabajo de forma real con un sgdb para almacenar las direcciones e información de los peers en el servidor central, se usaron listas y diccionarios para esto.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

- Se utilizo gRPC para la comunicacion entre los peers, nos permitio definir mensajes y servicios para facilitar la comunicacion en nuestra app distribuida.

- Separación de responsabilidades, encapsulamiento, patrones de fachada. Todas estas se evidencian ya que el código separa funcionalidades en diferentes archivos y clases, permitiendo una fácil comprensión y mantenimiento de código. Al crear clases, hemos encapsulado un conjunto coherente de funcionalidades relacionadas, lo que permite su reutilización y modificación sin afectar partes del código. Todo este enfoque para buscar mejorar el modularidad, la legibilidad y la mantenibilidad del código siguiendo las mejores prácticas de diseño de software.

- Se implementa una arquitectura p2p centralizada basada en servidor, donde los peers se conectarán a un servidor para brindar información de ellos mismos y recibir la misma de otros al hacer consultas con los métodos del servidor. A partir de esas consultas, los peers pueden hacer un proceso de comunicación con el middelware grpc a otros peerServidores y simular la obtención de archivos.

  [![redp2p.png](https://i.postimg.cc/LXjDkknR/redp2p.png)](https://postimg.cc/Ppr1TwWF)

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

- IDE: Visual Studio Code
- Lenguaje de Programación: Python v3.11.8
- Librerías - paquetes: 
     grpcio v1.62.0 
     grpcio-tools v1.62.0
     Flask v3.0.0
     requests v2.31.0

Para ejecutar y compilar en el entorno de desarrollo:

Instalamos Flask: 
   'pip install grpcio grpcio-tools Flask requests'

Debemos generar el archivo .proto:
    'python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. peerServidor.proto'

Despues corremos el servidor central de la forma: 

    'python Servidor.py'

Debemos correr los archivos main de los peers:

    'python peerServidor.py'
    'python peerCliente.py'

Es importante entrar a cada ruta para la ejecucion de archivos, para el servidor central debemos acceder a la ruta:
                 'Reto1y2/main/Servidor'

Para los archivos main del peer:
                 'Reto1y2/main/Servidor

[![imagen-2024-03-05-175841797.png](https://i.postimg.cc/3NsKMT32/imagen-2024-03-05-175841797.png)](https://postimg.cc/p5BN83hd)

5. Referencias:

https://github.com/cpurta/p2p-grpc

https://grpc.io/blog/coreos/

https://blog.hubspot.com/website/what-is-rest-api#:~:text=A%20REST%20API%20(also%20called,resource%20in%20a%20standardized%20representation.

https://www.freecodecamp.org/news/rest-api-tutorial-rest-client-rest-service-and-api-calls-explained-with-code-examples/

ia assistance (chatGPT, microsoft Copilot)


