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

# Test PUT request
headers, body = client.put('/put', body='This is a PUT request')
print('PUT /put')
print('Headers:', headers)
print('Body:', body)

# Test DELETE request
headers, body = client.delete('/delete')
print('DELETE /delete')
print('Headers:', headers)
print('Body:', body)

# Test PATCH request
headers, body = client.patch('/patch', body='This is a PATCH request')
print('PATCH /patch')
print('Headers:', headers)
print('Body:', body)