import threading
import datetime


class my_td(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter

    def run(self):
        print_date(self.name, self.counter)


def print_date(tdname, counter):
    dt = []
    today = datetime.date.today()
    dt.append(today)
    print("{}[{}]: {}".format(tdname, counter, dt[0]))


thread1 = my_td("current-date:", 1)

thread1.start()

thread1.join()
