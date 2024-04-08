# Cliente HTTP

## Cliente

### Descripción

Este proyecto contiene un cliente HTTP básico. El cliente HTTP se encuentra en el archivo http_client.py. Este cliente puede realizar solicitudes HTTP básicas, incluyendo GET, POST, PUT, DELETE, OPTIONS, HEAD, TRACE, CONNECT, LINK, UNLINK y un método personalizado.

### Uso(cliente)

Para usar el cliente HTTP, primero debes instanciar la clase HttpClient con el host al que deseas conectarte. Opcionalmente, puedes especificar un puerto y si deseas usar HTTPS:

> client = HttpClient('www.example.com', use_https=True)

Luego, puedes usar los métodos correspondientes para realizar solicitudes HTTP:

> headers, body = client.get('/')

Cada método devuelve los encabezados de la respuesta como un diccionario y el cuerpo de la respuesta como una cadena.

## Pruebas Unitarias

Las pruebas unitarias se encuentran en el archivo unit_test.py. Estas pruebas verifican que el cliente HTTP puede manejar correctamente las respuestas del servidor para cada tipo de solicitud HTTP.

### Uso(Pruebas unitarias)

Para ejecutar las pruebas unitarias, simplemente ejecuta el archivo unit_test.py con Python:

> python unit_test.py

## Interfaz Gráfica de Usuario

Este proyecto también incluye una interfaz gráfica de usuario (GUI) para el cliente HTTP, que se encuentra en el archivo gui.py. Esta GUI permite a los usuarios ingresar el host, la URL, el método HTTP y los encabezados de la solicitud, y luego enviar la solicitud con un clic en "Send Request".

### Uso(GUI)

Para ejecutar la GUI, simplemente ejecuta el archivo gui.py con Python:

> python gui.py

## Servidor

Este proyecto también incluye un servidor HTTP básico que soporta la concurrencia basada en hilos. El servidor se encuentra en el archivo server.py y puede manejar los métodos HTTP GET, POST, PUT, DELETE, OPTIONS, HEAD, TRACE, CONNECT, LINK, UNLINK y un método personalizado.

### Uso(Servidor)

Para ejecutar el servidor, simplemente ejecuta el archivo server.py con Python:

> python server.py
