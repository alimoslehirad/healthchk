from TelegramSend import TelegramSend


class Alerting:

    telegram_send_flag = True
    email_send_flag = False
    slack_send_flag = False
    telegram_send_obj = TelegramSend()

    def alert_send(self, msg):
        self.telegram_send(msg)
        self.email_send(msg)
        self.slack_send(msg)

    def telegram_send(self, msg):
        if self.telegram_send_flag:
            self.telegram_send_obj.send(msg)

    def email_send(self, msg):
        if self.email_send_flag:
            pass

    def slack_send(self, msg):
        if self.slack_send_flag:
            pass
