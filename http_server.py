import http.server
import socketserver
import threading

# Esta es una clase de servidor HTTP que admite la concurrencia basada en hilos.
class ThreadedHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    pass

# Esta es una clase de controlador de solicitudes HTTP personalizada.
class MyHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    # Maneja las solicitudes GET
    def do_GET(self):
        self.send_response(200)  # Envía una respuesta de estado HTTP 200 (OK)
        self.end_headers()  # Termina los encabezados de la respuesta
        self.wfile.write(b'Hello, GET!')  # Escribe el cuerpo de la respuesta

    # Maneja las solicitudes POST
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, POST!')

    # Maneja las solicitudes PUT
    def do_PUT(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, PUT!')

    # Maneja las solicitudes DELETE
    def do_DELETE(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, DELETE!')

    # Maneja las solicitudes HEAD
    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    # Maneja las solicitudes OPTIONS
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Allow', 'OPTIONS, GET, POST, HEAD, PUT, DELETE')  # Envía un encabezado 'Allow' con los métodos permitidos
        self.end_headers()

    # Maneja las solicitudes CONNECT
    def do_CONNECT(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, CONNECT!')

    # Maneja las solicitudes TRACE
    def do_TRACE(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, TRACE!')

    # Maneja las solicitudes LINK
    def do_LINK(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, LINK!')

    # Maneja las solicitudes UNLINK
    def do_UNLINK(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, UNLINK!')

    # Maneja las solicitudes CUSTOM
    def do_CUSTOM(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, CUSTOM!')

# Si este script se ejecuta como el programa principal, inicia el servidor
if __name__ == "__main__":
    server = ThreadedHTTPServer(('localhost', 8000), MyHTTPRequestHandler)  # Crea un servidor en localhost en el puerto 8000
    print('Starting server, use <Ctrl-C> to stop')  # Imprime un mensaje indicando que el servidor está iniciando
    server.serve_forever()  # Inicia el servidor
