import threading
from server import ServerSide
from URLFileRead import URLFileRead
def service_test_timer():
    url_read = URLFileRead()
    url_read.service_test()
    print("container is running")
    timer = threading.Timer(2.0, service_test_timer)
    timer.start()
x = ServerSide()
x.socketing()
print("server is running")
#service_test_timer()
#print("timer start")
