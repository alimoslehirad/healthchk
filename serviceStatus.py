from tinydb import TinyDB, Query
import requests
from requests.auth import HTTPBasicAuth
class ServiceStatus:
    def __init__(self):
        self.db = TinyDB('db2.json')
        self.status = self.db.table('STATUS')
        self.urlTable = self.db.table('URL')

    def define_status(self):
        statusQuery = Query()
        for i in range(3):
            x = self.urlTable.search(statusQuery.Id == i)
            url = [r['URL'] for r in x]
            status = [r['status'] for r in x]
            status = str(status)
            status = status.replace('Response','')
            print(status , url)
            # y = x.replace('Response','')






