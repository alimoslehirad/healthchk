import threading
from TelegramSend import TelegramSend
from periodic_request_sender import Periodic_request_sender
from server import ServerSide
from URLFileRead import URLFileRead
import cherrypy
class Main:

    @cherrypy.expose
    def example(self):
        index = open("indexformat.html").read().format(var1='goodbye',var2='goodbye',var3='goodbye',var4='goodbye',var5='goodbye',var6='goodbye')
        return index
# m = Main()
# e=m.example()
# f = open("index.html", "w")
# f.write(e)
# f.close()
# y = TelegramSend()
# # print(y.send())
# x = ServerSide()
# T1=Periodic_request_sender()
# T1.start()
# x.start()
print("server is running")

