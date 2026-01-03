from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs


HOST = "localhost"
PORT = 8000


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open("contacts.html", "r", encoding="utf-8") as file:
            html = file.read()

        self.wfile.write(html.encode("utf-8"))


    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8")

        data = parse_qs(body)
        print("Получены данные от пользователя:")
        for key, value in data.items():
            print(f"{key}: {value}")

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open("contacts.html", "r", encoding="utf-8") as file:
            html = file.read()

        self.wfile.write(html.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer((HOST, PORT), Handler)
    print(f"Сервер запущен: http://{HOST}:{PORT}")
    server.serve_forever()
