from html_manager import Html_manager
from TelegramSend import TelegramSend
from serviceTest import ServiceTest
import threading
from URLFileRead import URLFileRead
class Periodic_request_sender(threading.Thread):

    html: Html_manager=Html_manager()
    def run(self):
        serviceTest = ServiceTest()
        # request_list = serviceTest.url_test()
        request_list = serviceTest.general_test()
        # self.html.write_index(request_list)
        # telegram = TelegramSend()
        # telegram.send()
        timer = threading.Timer(2.0, self.run)
        timer.start()