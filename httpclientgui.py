import tkinter as tk
from tkinter import messagebox, font
from http_client import HttpClient

class HttpClientGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("HTTP Client")
        self.window.configure(bg='lightblue')

        my_font = font.Font(family='Helvetica', size=12, weight='bold')

        self.host_label = tk.Label(self.window, text="Host:", bg='lightblue', font=my_font)
        self.host_entry = tk.Entry(self.window)

        self.url_label = tk.Label(self.window, text="URL:", bg='lightblue', font=my_font)
        self.url_entry = tk.Entry(self.window)

        self.method_var = tk.StringVar(self.window)
        self.method_var.set("GET")  # default value

        self.method_label = tk.Label(self.window, text="Method:", bg='lightblue', font=my_font)
        self.method_entry = tk.OptionMenu(self.window, self.method_var, *["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "CONNECT", "TRACE", "LINK", "UNLINK", "CUSTOM"])

        self.accept_label = tk.Label(self.window, text="Accept:", bg='lightblue', font=my_font)
        self.accept_entry = tk.Entry(self.window)

        self.content_type_label = tk.Label(self.window, text="Content-Type:", bg='lightblue', font=my_font)
        self.content_type_entry = tk.Entry(self.window)

        self.user_agent_label = tk.Label(self.window, text="User-Agent:", bg='lightblue', font=my_font)
        self.user_agent_entry = tk.Entry(self.window)

        self.body_label = tk.Label(self.window, text="Body:", bg='lightblue', font=my_font)
        self.body_entry = tk.Text(self.window)

        self.send_button = tk.Button(self.window, text="Send Request", command=self.send_request, bg='lightgreen', font=my_font)

        self.host_label.pack()
        self.host_entry.pack()
        self.url_label.pack()
        self.url_entry.pack()
        self.method_label.pack()
        self.method_entry.pack()
        self.accept_label.pack()
        self.accept_entry.pack()
        self.content_type_label.pack()
        self.content_type_entry.pack()
        self.user_agent_label.pack()
        self.user_agent_entry.pack()
        self.body_label.pack()
        self.body_entry.pack()
        self.send_button.pack()

    def send_request(self):
        host = self.host_entry.get()
        url = self.url_entry.get()
        method = self.method_var.get().upper()

        headers = {
            'Accept': self.accept_entry.get(),
            'Content-Type': self.content_type_entry.get(),
            'User-Agent': self.user_agent_entry.get(),
        }

        body = self.body_entry.get("1.0", tk.END)

        client = HttpClient(host)

        try:
            if method == 'GET':
                headers, body = client.get(url, headers)
            elif method == 'POST':
                headers, body = client.post(url, headers, body)
            elif method == 'PUT':
                headers, body = client.put(url, headers, body)
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

            messagebox.showinfo("Response", f"Headers:\n{headers}\n\nBody:\n{body}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.window.mainloop()

gui = HttpClientGUI()
gui.run()
