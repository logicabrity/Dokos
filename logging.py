import os
import time

class Logging(object):
    def __init__(self, path):
        self.path = path

        # try to open the file right now so that in case of lacking writing
        # permissions for example, an exception is raised right when the
        # script starts instead of much later down the road when the first
        # entry should be created.
        f = open(path, 'a')
        f.close()

    def write(self, entry):
        prefix = time.strftime('%Y-%m-%d %H:%M:%S') + ' '
        with open(self.path, 'a') as f:
            f.write(prefix + entry + "\n")
