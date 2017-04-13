from wsgiref import simple_server
from http import HTTPStatus
import json


# WSGI app
class WsgiApp(object):
    def __call__(self, environ, start_response):
        print("WSGI APP!")
        start_response('200 OK', [('Content-Type', 'application/json')])
        dc = {"statusCode": HTTPStatus.OK}
        return [json.dumps(dc).encode()]


class Middleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        print("class Middleware!")
        return self.app(environ, start_response)


def main():
    application = WsgiApp()
    application = Middleware(application)
    httpd = simple_server.make_server('', 8888, application)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
