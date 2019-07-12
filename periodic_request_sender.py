
import threading
from TelegramSend import TelegramSend
from server import ServerSide
from URLFileRead import URLFileRead
class Periodic_request_sender(threading.Thread):

    def run(self):
        url_read = URLFileRead()
        url_read.service_test()
        print("container is running")
        timer = threading.Timer(2.0, self.run)
        timer.start()