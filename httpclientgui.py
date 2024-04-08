import tkinter as tk
from tkinter import messagebox, font
from http_client import HttpClient

# Esta es una clase para una interfaz gráfica de usuario (GUI) para el cliente HTTP.
class HttpClientGUI:
    def __init__(self):
        # Crea una ventana de tkinter
        self.window = tk.Tk()
        self.window.title("HTTP Client")  # Establece el título de la ventana
        self.window.configure(bg='lightblue')  # Establece el color de fondo de la ventana

        # Cambia la fuente
        my_font = font.Font(family='Helvetica', size=12, weight='bold')

        # Crea etiquetas y campos de entrada para el host, la URL y el método HTTP
        self.host_label = tk.Label(self.window, text="Host:", bg='lightblue', font=my_font)
        self.host_entry = tk.Entry(self.window)

        self.url_label = tk.Label(self.window, text="URL:", bg='lightblue', font=my_font)
        self.url_entry = tk.Entry(self.window)

        self.method_label = tk.Label(self.window, text="Method:", bg='lightblue', font=my_font)
        self.method_entry = tk.Entry(self.window)

        # Agrega campos de entrada para los encabezados
        self.accept_label = tk.Label(self.window, text="Accept:", bg='lightblue', font=my_font)
        self.accept_entry = tk.Entry(self.window)

        self.content_type_label = tk.Label(self.window, text="Content-Type:", bg='lightblue', font=my_font)
        self.content_type_entry = tk.Entry(self.window)

        self.user_agent_label = tk.Label(self.window, text="User-Agent:", bg='lightblue', font=my_font)
        self.user_agent_entry = tk.Entry(self.window)

        # Crea un botón para enviar la solicitud
        self.send_button = tk.Button(self.window, text="Send Request", command=self.send_request, bg='lightgreen', font=my_font)

        # Agrega los widgets a la ventana
        self.host_label.pack()
        self.host_entry.pack()
        self.url_label.pack()
        self.url_entry.pack()
        self.method_label.pack()
        self.method_entry.pack()

        # Empaqueta los campos de entrada de los encabezados
        self.accept_label.pack()
        self.accept_entry.pack()
        self.content_type_label.pack()
        self.content_type_entry.pack()
        self.user_agent_label.pack()
        self.user_agent_entry.pack()

        self.send_button.pack()

    # Esta función se llama cuando se presiona el botón "Send Request"
    def send_request(self):
        # Obtiene los valores de los campos de entrada
        host = self.host_entry.get()
        url = self.url_entry.get()
        method = self.method_entry.get().upper()

        # Obtiene los encabezados de los campos de entrada
        headers = {
            'Accept': self.accept_entry.get(),
            'Content-Type': self.content_type_entry.get(),
            'User-Agent': self.user_agent_entry.get(),
        }

        # Crea un cliente HTTP
        client = HttpClient(host)

        try:
            # Envía la solicitud HTTP y obtiene la respuesta
            if method == 'GET':
                headers, body = client.get(url, headers)
            elif method == 'POST':
                headers, body = client.post(url, headers)
            elif method == 'PUT':
                headers, body = client.put(url, headers)
            elif method == 'DELETE':
                headers, body = client.delete(url, headers)
            elif method == 'HEAD':
                headers, body = client.head(url, headers)
            elif method == 'OPTIONS':
                headers, body = client.options(url, headers)
            elif method == 'CONNECT':
                headers, body = client.connect(url, headers)
            elif method == 'TRACE':
                headers, body = client.trace(url, headers)
            elif method == 'LINK':
                headers, body = client.link(url, headers)
            elif method == 'UNLINK':
                headers, body = client.unlink(url, headers)
            elif method == 'CUSTOM':
                headers, body = client.custom_method(url, headers)
            else:
                raise Exception(f"Unsupported HTTP method: {method}")

            # Muestra la respuesta en una ventana de mensaje
            messagebox.showinfo("Response", f"Headers:\n{headers}\n\nBody:\n{body}")
        except Exception as e:
            # Si ocurre un error, muestra un mensaje de error
            messagebox.showerror("Error", str(e))

    # Esta función inicia la GUI
    def run(self):
        self.window.mainloop()

# Crea una GUI para el cliente
gui = HttpClientGUI()

# Ejecuta la GUI
gui.run()
