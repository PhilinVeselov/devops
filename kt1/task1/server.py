from http.server import HTTPServer, SimpleHTTPRequestHandler

# Задайте путь к вашим статическим файлам
DIRECTORY = "static_files"

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print(f"Сервер запущен на порту {server_address[1]}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
