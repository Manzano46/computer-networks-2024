import unittest
from unittest.mock import patch, MagicMock
from http_client import HttpClient 

class TestHttpClient(unittest.TestCase):
    def setUp(self):
        self.client = HttpClient('www.example.com')

    @patch('socket.socket')
    def test_get(self, mock_socket):
        response = b'HTTP/1.1 200 OK\r\nContent-Length: 1256\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n<!doctype html>\n<html>\n<head>\n<title>Example Domain</title>\n</head>\n</html>'
        fragments = [response[i:i+1024] for i in range(0, len(response), 1024)] + [b'']
        mock_socket.return_value.recv.side_effect = lambda x: fragments.pop(0) if fragments else b''
        headers, body = self.client.get('/')
        self.assertEqual(headers['Status'], 'HTTP/1.1 200 OK')
        self.assertEqual(headers['Content-Length'], '1256')
        self.assertEqual(headers['Content-Type'], 'text/html; charset=UTF-8')
        self.assertTrue(body.startswith('<!doctype html>'))


    @patch('socket.socket')
    def test_post(self, mock_socket):
        response = b'HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n'
        mock_socket.return_value.recv.side_effect = [response[i:i+1024] for i in range(0, len(response), 1024)] + [b'']
        headers, body = self.client.post('/', body='Hello, world!')
        self.assertEqual(headers['Status'], 'HTTP/1.1 200 OK')
        self.assertEqual(body, '')

    @patch('socket.socket')
    def test_put(self, mock_socket):
        response = b'HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n'
        mock_socket.return_value.recv.side_effect = [response[i:i+1024] for i in range(0, len(response), 1024)] + [b'']
        headers, body = self.client.put('/', body='Hello, world!')
        self.assertEqual(headers['Status'], 'HTTP/1.1 200 OK')
        self.assertEqual(body, '')

    @patch('socket.socket')
    def test_delete(self, mock_socket):
        response = b'HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n'
        mock_socket.return_value.recv.side_effect = [response[i:i+1024] for i in range(0, len(response), 1024)] + [b'']
        headers, body = self.client.delete('/')
        self.assertEqual(headers['Status'], 'HTTP/1.1 200 OK')
        self.assertEqual(body, '')

    @patch('socket.socket')
    def test_options(self, mock_socket):
        response = b'HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n'
        mock_socket.return_value.recv.side_effect = [response[i:i+1024] for i in range(0, len(response), 1024)] + [b'']
        headers, body = self.client.options('/')
        self.assertEqual(headers['Status'], 'HTTP/1.1 200 OK')
        self.assertEqual(body, '')

    @patch('socket.socket')
    def test_head(self, mock_socket):
        response = b'HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n'
        mock_socket.return_value.recv.side_effect = [response[i:i+1024] for i in range(0, len(response), 1024)] + [b'']
        headers, body = self.client.head('/')
        self.assertEqual(headers['Status'], 'HTTP/1.1 200 OK')
        self.assertEqual(body, '')

    @patch('socket.socket')
    def test_trace(self, mock_socket):
        response = b'HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n'
        mock_socket.return_value.recv.side_effect = [response[i:i+1024] for i in range(0, len(response), 1024)] + [b'']
        headers, body = self.client.trace('/')
        self.assertEqual(headers['Status'], 'HTTP/1.1 200 OK')
        self.assertEqual(body, '')

    @patch('socket.socket')
    def test_connect(self, mock_socket):
        response = b'HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n'
        mock_socket.return_value.recv.side_effect = [response[i:i+1024] for i in range(0, len(response), 1024)] + [b'']
        headers, body = self.client.connect('/')
        self.assertEqual(headers['Status'], 'HTTP/1.1 200 OK')
        self.assertEqual(body, '')

    @patch('socket.socket')
    def test_link(self, mock_socket):
        response = b'HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n'
        mock_socket.return_value.recv.side_effect = [response[i:i+1024] for i in range(0, len(response), 1024)] + [b'']
        headers, body = self.client.link('/')
        self.assertEqual(headers['Status'], 'HTTP/1.1 200 OK')
        self.assertEqual(body, '')

    @patch('socket.socket')
    def test_unlink(self, mock_socket):
        response = b'HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n'
        mock_socket.return_value.recv.side_effect = [response[i:i+1024] for i in range(0, len(response), 1024)] + [b'']
        headers, body = self.client.unlink('/')
        self.assertEqual(headers['Status'], 'HTTP/1.1 200 OK')
        self.assertEqual(body, '')

    @patch('socket.socket')
    def test_custom_method(self, mock_socket):
        response = b'HTTP/1.1 200 OK\r\nContent-Length: 0\r\n\r\n'
        mock_socket.return_value.recv.side_effect = [response[i:i+1024] for i in range(0, len(response), 1024)] + [b'']
        headers, body = self.client.custom_method('/', body='Hello, world!')
        self.assertEqual(headers['Status'], 'HTTP/1.1 200 OK')
        self.assertEqual(body, '')


if __name__ == '__main__':
    unittest.main()
