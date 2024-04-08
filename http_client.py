import socket
import ssl
import base64
from http import cookies

class HttpClient:
    def __init__(self, host, port=80, use_https=False):
        # Inicializa el cliente con el host, puerto y si se debe usar HTTPS
        # También inicializa un diccionario para almacenar las cookies y un lugar para almacenar los encabezados de la última respuesta
        self.host = host
        self.port = port
        self.use_https = use_https
        self.cookies = {}
        self.last_response_headers = None

    def send_request(self, method, path, headers=None, body=None, username=None, password=None):
        try:
            
            # Crea un socket y establece un tiempo de espera
            # socket.AF_INET se refiere a la familia de ipv4, tambie existe AF_INET6 para ipv6
            # socket.SOCK_STREAM representa el tipo de conexion, en este caso utilizamos TCP, tambien esta socket.SOCK_DGRAM como UDP

            sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            sock.settimeout(10.0)

            # Si se debe usar HTTPS, envuelve el socket con un contexto SSL/TLS(secure secret layer y transport layer security) y cambia el puerto a 443
            if self.use_https:
                context = ssl.create_default_context()
                sock = context.wrap_socket(sock, server_hostname=self.host)
                self.port = 443

            # Conecta el socket al host y puerto especificados
            sock.connect((self.host, self.port))

            # Si no se proporcionan encabezados, inicializa un diccionario vacío
            if headers is None:
                headers = {}

            # Si se proporcionan un nombre de usuario y una contraseña, los codifica en base64 y los incluye en el encabezado de autorización
            if username is not None and password is not None:
                credentials = f'{username}:{password}'
                base64_credentials = base64.b64encode(credentials.encode()).decode()
                headers['Authorization'] = f'Basic {base64_credentials}'

            # Si hay cookies almacenadas, las incluye en el encabezado de la solicitud
            if self.cookies:
                cookie_header = '; '.join(f'{k}={v}' for k, v in self.cookies.items())
                headers['Cookie'] = cookie_header

            # Asegura que el encabezado 'Host' esté presente
            if 'Host' not in headers:
                headers['Host'] = self.host

            # Agrega soporte para el encabezado 'User-Agent' si no está presente (aplicacion)
            if 'User-Agent' not in headers:
                headers['User-Agent'] = 'MyHttpClient/1.0'

            # Agrega soporte para el encabezado 'Accept' si no está presente (que puede recibir)
            if 'Accept' not in headers:
                headers['Accept'] = '*/*'

            # Construye la solicitud HTTP
            request = '{} {} HTTP/1.1\r\n'.format(method, path)
            request += ''.join('{}: {}\r\n'.format(k, v) for k, v in headers.items())
            request += '\r\n'

            # Si se proporciona un cuerpo, lo añade a la solicitud
            if body is not None:
                request += '\r\n' + body

            # Envía la solicitud al servidor
            sock.send(request.encode())

            # Recibe la respuesta del servidor
            headers, body = self.receive_response(sock)
            self.last_response_headers = headers

            # Si la respuesta es una redirección, sigue la redirección resuelve recursivo
            if headers['Status'].startswith(('301', '302', '303', '307', '308')):
                new_url = headers['Location']
                sock.close()
                new_client = HttpClient(new_url, use_https=self.use_https)
                return new_client.send_request(method, new_url, headers, body)

            # Si la respuesta incluye una cookie, la almacena
            for header, value in headers.items():
                if header.lower() == 'set-cookie':
                    cookie = cookies.SimpleCookie()
                    cookie.load(value)
                    
                    for morsel in cookie.values():
                        self.cookies[morsel.key] = {
                            'value': morsel.value,
                            'expires': morsel['expires'],
                            'domain': morsel['domain'],
                            'path': morsel['path'],
                        }

            # Cierra el socket y devuelve los encabezados y el cuerpo de la respuesta
            sock.close()

            return headers, body
        
        except socket.timeout:
            # Si se agota el tiempo de espera, lanza una excepción
            raise Exception("La solicitud se agotó.")
        except socket.error as e:
            # Si ocurre un error de socket, lanza una excepción
            raise Exception(f"No se pudo conectar al servidor. {e}")
        except Exception as e:
            # Si ocurre cualquier otro error, lanza una excepción
            raise Exception(f"Ocurrió un error inesperado. {e}")

    # Métodos para enviar solicitudes HTTP de los tipos correspondientes
    def get(self, path, headers=None):
        return self.send_request('GET', path, headers)

    def post(self, path, headers=None, body=None):
        return self.send_request('POST', path, headers, body)

    def put(self, path, headers=None, body=None):
        return self.send_request('PUT', path, headers, body)

    def delete(self, path, headers=None):
        return self.send_request('DELETE', path, headers)
    
    def patch(self, path, headers=None, body=None):
        return self.send_request('PATCH', path, headers, body)

    def options(self, path, headers=None):
        return self.send_request('OPTIONS', path, headers)

    def head(self, path, headers=None):
        return self.send_request('HEAD', path, headers)

    def trace(self, path, headers=None):
        return self.send_request('TRACE', path, headers)

    def connect(self, path, headers=None):
        return self.send_request('CONNECT', path, headers)
    
    def custom_method(self, path, headers=None, body=None):
        return self.send_request('CUSTOM', path, headers, body)

    def link(self, path, headers=None, body=None):
        return self.send_request('LINK', path, headers, body)

    def unlink(self, path, headers=None):
        return self.send_request('UNLINK', path, headers)

    # Método para recibir la respuesta del servidor
    def receive_response(self, sock):
        # Lee los encabezados de la respuesta
        headers = ''
        while True:
            data = sock.recv(1)
            if not data:
                break
            headers += data.decode()
            if headers.endswith('\r\n\r\n'):
                break

        # Separa los encabezados del cuerpo de la respuesta
        headers, body = headers.split('\r\n\r\n', 1)
        headers = headers.split('\r\n')

        # Convierte los encabezados en un diccionario
        header_dict = {}
        for i, header in enumerate(headers):
            if i == 0:
                header_dict['Status'] = header
            else:
                name, value = header.split(': ', 1)
                header_dict[name] = value

        # Comprueba el código de estado de la respuesta
        status_code = int(header_dict['Status'].split()[1])

        if 100 <= status_code < 200:
            if status_code == 100:
                print("Continuar con la solicitud.")
        elif 200 <= status_code < 300:
            if status_code == 204:
                print("La solicitud fue exitosa, pero no hay contenido para devolver.")
        elif 400 <= status_code < 600:
            raise Exception(f"El servidor respondió con un código de estado de error: {status_code}")

        # Procesa los encabezados de la respuesta
        for name, value in header_dict.items():
            if name.lower() == 'set-cookie':
                # Si la respuesta incluye una cookie, la almacena
                cookie = cookies.SimpleCookie()
                cookie.load(value)
                for morsel in cookie.values():
                    self.cookies[morsel.key] = {
                        'value': morsel.value,
                        'expires': morsel['expires'],
                        'domain': morsel['domain'],
                        'path': morsel['path'],
                    }
            elif name.lower() == 'content-encoding':
                # Agrega soporte para el encabezado 'Content-Encoding'
                print(f"El contenido está codificado con: {value}")
            elif name.lower() == 'last-modified':
                # Agrega soporte para el encabezado 'Last-Modified'
                print(f"El contenido fue modificado por última vez en: {value}")

        # Si la respuesta está codificada en trozos, lee los trozos y los une para formar el cuerpo completo de la respuesta
        if 'Transfer-Encoding' in header_dict and header_dict['Transfer-Encoding'] == 'chunked':
            chunks = []
            while True:
                line = ''
                while not line.endswith('\r\n'):
                    line += sock.recv(1).decode()
                chunk_length = int(line[:-2], 16)

                if chunk_length == 0:
                    break

                chunk = ''
                while len(chunk) < chunk_length:
                    chunk += sock.recv(min(chunk_length - len(chunk), 1024)).decode()
                chunks.append(chunk)

                sock.recv(2)
            body = ''.join(chunks)  
        elif 'Content-Length' in header_dict:
            # Si la respuesta incluye un encabezado 'Content-Length', lee el cuerpo de la respuesta hasta que se haya leído la cantidad de datos especificada
            remaining = int(header_dict['Content-Length']) - len(body)
            while remaining > 0:
                data = sock.recv(min(remaining, 1024))
                if not data:
                    break
                body += data.decode()
                remaining -= len(data)

        # Devuelve los encabezados y el cuerpo de la respuesta
        return header_dict, body
