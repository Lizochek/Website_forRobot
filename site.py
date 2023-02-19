import http.server
import socketserver

PORT = 9000

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = 'index.html' # в этом файле находится html код, для дизайна менять код только в нем
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHttpRequestHandler
def http_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Http Server Serving at port", PORT)
        httpd.serve_forever()

if __name__ == '__main__':
    http_server()