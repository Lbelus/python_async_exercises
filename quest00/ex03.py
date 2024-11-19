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
    print(msg + "is starting")
    dt = Delay_task(delay)
    res = yield from dt.__await__()
    if res is True:
        print(msg)

def event_loop(tasks):
    while tasks:
        for task in tasks[:]:  
            try:
                next(task)
            except StopIteration:
                tasks.remove(task)

if __name__ == "__main__":
    
    
    tasks = [
        my_task("task00", 3),
        my_task("task01", 1),
    ]

    
    tasks = [task for task in tasks]
    

    event_loop(tasks)
