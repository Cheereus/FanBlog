import http.server as BaseHTTPServer


class RequestHandler(BaseHTTPServer.SimpleHTTPRequestHandler):

    def __init__(self, *args, directory=None, **kwargs):
        if directory is None:
            self.directory = '/home/fanwei/workspace/FanBlog/web/'
        else:
            self.directory = directory
        super().__init__(*args, directory=self.directory, **kwargs)

    '''处理请求并返回页面'''

    # 页面模板
    Page = '''\
        <html>
        <body>
        <p>Hello, web!</p>
        </body>
        </html>
    '''

    # # 处理一个GET请求
    # def do_GET(self):
    #     print(self.path)
    #     self.send_response(200)
    #     self.send_header("Content-Type", "text/html")
    #     self.send_header("Content-Length", str(len(self.Page)))
    #     self.end_headers()
    #     self.wfile.write(self.Page.encode())

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = BaseHTTPServer.HTTPServer(serverAddress, RequestHandler)
    server.serve_forever()
