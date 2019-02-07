import datetime

class Item(object):

    def __init__(self, task):
        self.timestamp = datetime.datetime.now()
        self.task_comp = False
        self.task = task
