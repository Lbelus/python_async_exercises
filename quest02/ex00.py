from queue import Queue

def event_loop(queue):
    while not queue.empty():
        task = queue.get()
        task()

task_queue = Queue()

task_queue.put(lambda: print("Task 1 executed"))
task_queue.put(lambda: print("Task 2 executed"))

event_loop(task_queue)
