from tinydb import TinyDB, Query
import requests
import threading
from serviceStatus import ServiceStatus
from requests.auth import HTTPBasicAuth


class ServiceTest(threading.Thread):

    def run(self):

        self.general_test()
        timer = threading.Timer(2.0, self.run)
        timer.start()

    def init(self):
        self.counter = 0
        self.var = 1
        self.f = open("URLs.txt")
        self.requestList = []
        self.usr = "admin"
        self.password = 'POWERofHUMAN@mon'
        self.db = TinyDB('db2.json')
        self.smsTable = self.db.table('SMS')
        self.db.purge_table('SMS')
        self.urlTable = self.db.table('URL')
        self.db.purge_table('URL')
        User = Query()
        print(self.smsTable.search(User.name == 'Rithel'))
        print("print all tables :\n")
        print(self.smsTable.all())

    def general_test(self):
        self.init()
        self.url_test()
        print("print all tables :\n")
        print(self.urlTable.all())
        self.sms_operators_test()
        self.glubal_network_test()
        self.local_network_test()
        self.proxy_test()
        status=ServiceStatus()
        print("-------------------------------------\n")
        status.define_status()


    def url_test(self):

        f = open("URLs.txt")
        var = 1
        requestAnswer=['','']
        count=0
        while (var==1):
            url = str(f.readline())
            print(url)
            url=url.replace("\n","")

            if("end" in url):
                break
            answer=str(requests.get(url, auth = HTTPBasicAuth("admin", self.password)))
            self.urlTable.insert({'Id': count,'URL':url ,'status': answer})
            count = count + 1
            print("send feedback =" + answer)
            if("200" in answer):
                print("request send OK")
                requestAnswer = [url,'OK' ]

            else:
                requestAnswer = [url, 'Fail']

            self.requestList.append(requestAnswer)
        print("read end")
        print(self.requestList)
        self.f.close()
        return self.requestList


    def sms_operators_test(self):
        pass


    def proxy_test(self):
        pass


    def local_network_test(self):
        pass


    def glubal_network_test(self):
        pass

