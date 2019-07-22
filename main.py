from tinydb import TinyDB, Query
import threading
from TelegramSend import TelegramSend
from serviceTest import ServiceTest
from server import ServerSide
from html_manager import  Html_manager
from URLFileRead import URLFileRead
import cherrypy
class Main:

    x = ServerSide()
    T = ServiceTest()
    T.start()
    x.start()
    print("server is running")

