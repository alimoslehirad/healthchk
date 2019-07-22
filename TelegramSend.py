import requests
class TelegramSend:


    def __init__(self):
        self.SERVER = 'pg1'
        self.token = '879341611:AAHjdFnz30JHuXepwl4XUgaufH8hriMDjT8'

    def send(self):
        # proxy = 'http://user:pass@198.143.183.123:400'
        proxy = {
            'http': 'http://qbit:bloodsucker@proxy1.qcluster.org:3128',
            'https': 'http://qbit:bloodsucker@proxy1.qcluster.org:3128',
        }
        msg = 'ali'
        bot_chatID = '-328266093'
        send_text = 'https://api.telegram.org/bot' + self.token + '/sendMessage?chat_id=' + bot_chatID + '&text=' + msg
        response=requests.get(send_text, proxies=proxy)
        print(response.text)
        return response.json()