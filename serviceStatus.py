from tinydb import TinyDB, Query
import requests
from requests.auth import HTTPBasicAuth
class ServiceStatus:
    def __init__(self):
        self.db = TinyDB('db2.json')
        self.statusdb_table = self.db.table('STATUS')
        self.urlTable = self.db.table('URL')

    def define_url_status(self, request_answer):
        status = ''
        if int(request_answer) < 300:
            status = 'service is OK'
        elif int(request_answer) > 399 & int(request_answer) < 500:
            status = 'client error'

        elif int(request_answer) > 499 & int(request_answer) < 600:
            status = 'server error'

        return status

    def write_to_database(self, name, status):
        self.urlTable.insert({'sevice_name': name, 'status': status})

    def service_test(self, url, usr, password):
        req = requests.get(url, auth = HTTPBasicAuth(usr, password))
        req.encoding
        answer = req.status_code
        print("status = " + str(answer))
        status = self.define_url_status(answer)
        return status
        # self.service_stattus.write_to_database(url[1], status)






