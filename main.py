from serviceTest import ServiceTest
from server import ServerSide


class Main:

    x = ServerSide()
    T = ServiceTest()
    T.start()
    x.start()
    print("server is running")

