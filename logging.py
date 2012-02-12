import datetime

class Logging(object):
    def __init__(self):
        today = datetime.datetime.now()
        self.update_filename(today)
        self.day = today.day

    def update_filename(self, d):
        self.filename = "{0}-{1}-{2}.txt".format(d.year, d.month, d.day)

    def write(self, entry):
        today = datetime.datetime.now()
        if today.day != self.day:
            self.update_filename

        with open(self.filename, 'a') as f:
            f.write(entry + "\n")
