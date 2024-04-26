from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class Server(BaseHTTPRequestHandler):
    """
    Обрабатывает входящие запросы
    """

    @staticmethod
    def __get_index():
        """
        Читает html файл
        """

        with open('index.html', 'r', encoding='utf-8') as file:
            result = file.read()

        return result


    def do_GET(self):
        """
        Метод для обработки входящих GET-запросов
        """

        page_content = self.__get_index()
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(page_content, "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), Server)
    print("Старт http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Остановка сервера")
