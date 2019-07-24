from alerting import Alerting


class Service:
    alert_mute = False
    alert_count = 0
    name = ''
    status = 'service is OK'
    alerting_stop = False
    wait2upservice = False
    alerting_status = 'active'
    alert = Alerting()

    def make_mute(self):
        self.alert_mute = True

    def make_alert_stop(self):
        self.alerting_stop = True
        self.alerting_status = 'waiting to service up'

    def make_alert_continue(self):
        self.alerting_stop = False
        self.alerting_status = 'active'

    def alerting_status_active(self):
        self.alerting_status = 'active'

    def alert_send(self, des):
        if not self.alerting_stop:
            if not self.alert_mute:
                self.alert.alert_send(des)
                self.alert_count = self.alert_count + 1
                if self.alert_count > 1:
                    self.make_alert_stop()
                    print("count greater than 2")
                    self.alert.alert_send("waiting to come up")
                    self.wait2upservice = True
                    self.alert_count = 0



