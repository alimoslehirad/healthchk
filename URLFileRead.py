import os
import requests
from requests.auth import HTTPBasicAuth
class URLFileRead:
    def __init__(self):
        self.counter = 0
        self.url = "end"
        self.var = 1
        self.f = open("URLs.txt")

    def service_test(self):
        print(os.environ['HOME'])
        print(os.environ['PATH'])
        self.f = open("URLs.txt")
    # perform file operations
        while (self.var==1):
            self.url = str(self.f.readline())
            print(self.url)
            self.url=self.url.replace("\n","")
            self.usr = "admin"
            password = 'POWERofHUMAN@mon'
            if("end" in self.url):
                break
            answer=str(requests.get(self.url, auth = HTTPBasicAuth("admin", password)))
            if("200" in answer):
                print("request send OK")
        print("read end")
        self.f.close()