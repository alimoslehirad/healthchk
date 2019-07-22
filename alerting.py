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
            self.urlTable.search(statusQuery.Id == i)




