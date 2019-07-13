import threading
from TelegramSend import TelegramSend
from periodic_request_sender import Periodic_request_sender
from server import ServerSide
from html_manager import  Html_manager
from URLFileRead import URLFileRead
import cherrypy
class Main:

    x = ServerSide()
    T1=Periodic_request_sender()
    T1.start()
    x.start()
    print("server is running")

