from http.server import HTTPServer, SimpleHTTPRequestHandler

DIRECTORY = "static_files"

class CustomHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run(server_class=HTTPServer, handler_class=CustomHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    print(f"Сервер запущен на порту {server_address[1]}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
