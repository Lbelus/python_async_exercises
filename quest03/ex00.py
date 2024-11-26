from queue import Queue
from datetime import datetime, timedelta


class Delay_task:
    def __init__(self, secs):
        self.secs = secs
        self.when = datetime.now() + timedelta(seconds=secs)

    def __await__(self):
        while self.when >= datetime.now():
            yield False
        return True

def my_task(msg, delay):
    print(msg + " is starting")
    dt = Delay_task(delay)
    res = yield from dt.__await__()
    if res is True:
        print(msg)

def event_loop(queue):
    while not queue.empty():
        task = queue.get()
        task()

def event_loop(queue):
    tasks = []
    while not queue.empty() or tasks:
        while not queue.empty():
            tasks.append(queue.get())

        for task in tasks[:]:
            try:
                next(task)  
            except StopIteration:
                tasks.remove(task)

task_queue = Queue()

task_queue.put(my_task("task 1", 3))
task_queue.put(my_task("task 2", 1))

event_loop(task_queue)
