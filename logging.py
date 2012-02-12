import os
import datetime

class Logging(object):
    def __init__(self, directory):
        self.dir = directory
        today = datetime.datetime.now()
        self.update_path(today)
        self.day = today.day

    def update_path(self, d):
        self.filename = "{0}-{1}-{2}.txt".format(d.year, d.month, d.day)
        self.path = os.path.join(self.dir, self.filename)

    def write(self, entry):
        today = datetime.datetime.now()
        if today.day != self.day:
            self.update_path(today)

        with open(self.path, 'a') as f:
            f.write(entry + "\n")
