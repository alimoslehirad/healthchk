import threading
from url import Url


class ServiceTest(threading.Thread):

    usr = "admin"
    password = 'POWERofHUMAN@mon'
    first_run_flag = True
    service_obj_list = []

    def run(self):
        self.general_test()
        timer = threading.Timer(4.0, self.run)
        timer.start()

    def general_test(self):
        if self.first_run_flag:
           self.service_obj_list = self.service_obj_creator()
           self.first_run_flag = False

        for svc_obj in self.service_obj_list:
            svc_obj.test()
        print("----------------------------------\n")
        # status.define_status()

    def service_obj_creator(self):

        f = open("URLs.txt")
        var = 1
        url_obj_list = []

        while var == 1:
            line = str(f.readline())
            if "end" in line:
                break

            urllist = line.split()
            print(urllist)
            url_obj_list.append(Url(urllist[1], urllist[0], self.usr, self.password))

        return url_obj_list
