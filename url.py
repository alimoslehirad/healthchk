from service import Service
from serviceStatus import ServiceStatus


class Url(Service):
    def __init__(self, name, url, usr, password):
        self.url = url
        self.name = name
        self.user = usr
        self.password = password
        self.error_con = 'server error'
        self.warning_con = 'client error'
        self.url_status = ServiceStatus()

    def test(self):
        self.status = self.url_status.service_test(self.url, self.user, self.password)
        if self.status == self.warning_con:
            msg = str(self.name + '  ' + str(self.status))
            self.alert_send(msg)
        if self.status == self.error_con:
            msg = str(self.name + '  ' + str(self.status))
            self.alert_send(msg)
        if self.wait2upservice:
            if self.status == 'service is OK':
                self.make_alert_continue()
                msg = str(self.name + '  '+'is OK now')
                self.alert_send(msg)
                self.wait2upservice = False
                self.alert_count = 0










