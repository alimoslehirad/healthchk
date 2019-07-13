from html_manager import Html_manager
import threading
from URLFileRead import URLFileRead
class Periodic_request_sender(threading.Thread):

    html: Html_manager=Html_manager()
    def run(self):
        url_read = URLFileRead()
        request_list = url_read.service_test()
        self.html.write_index(request_list)
        print("container is running")
        timer = threading.Timer(2.0, self.run)
        timer.start()