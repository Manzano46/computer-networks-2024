from http_client import HttpClient

# Crea una instancia del cliente HTTP
client = HttpClient('httpbin.org')

# Envía una solicitud GET
headers, body = client.get('/get')
print('GET /get')
print('Headers:', headers)
print('Body:', body)

# Envía una solicitud POST
headers, body = client.post('/post', body='Hello, world!')
print('POST /post')
print('Headers:', headers)
print('Body:', body)