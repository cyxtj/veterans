#coding=utf8

from cherrypy import wsgiserver
#from app folder import app defined in __init__.py
from app import app

d = wsgiserver.WSGIPathInfoDispatcher({'/': app})
server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 8008), d)

if __name__ == '__main__':
    try:
        print "start server ....."
        server.start()
    except KeyboardInterrupt:
        print "stop server ....."
        server.stop()
