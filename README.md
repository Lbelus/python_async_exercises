### Step-by-Step Exercises to Master Event Loops in Python

Event loops are the backbone of asynchronous programming, and Python provides tools like `asyncio` to work with them. Let’s build the concept organically with exercises.


Ressources: 
- https://medium.com/@pekelny/fake-event-loop-python3-7498761af5e0
- https://docs.python.org/3/library/asyncio-task.html

---

### **Quest 1: Understand Blocking vs. Non-Blocking Code**
Write a simple program where two tasks are executed sequentially (blocking) and then rewrite it to simulate non-blocking behavior.

1. **Sequential (Blocking)**:
   - Task 1: Sleep for 3 seconds and print a message.
   - Task 2: Sleep for 2 seconds and print a message.

2. Do it again with asyncio and async task

3. **Non-Blocking Simulation**:
   - Print "Task 1 started", then after 3 seconds, print "Task 1 finished".
   - Simultaneously, start "Task 2" and finish it in 2 seconds.

4. Do it again without asyncio


---

### **Quest 2: Building a Simple Timer with Callbacks**
Implement a timer function that takes a delay and a callback. The callback is called after the delay.

1. Write a `timer` function:
   ```python
   def timer(delay, callback):
   ```

2. Test it with:
   ```python
   def on_timer_complete():
       print("Timer completed!")

   timer(3, on_timer_complete)
   ```

---

### **Quest 3: Introduce the Event Queue**
Simulate an event loop by creating a queue where you push tasks (functions) to be executed later.

1. Create a queue and an executor:
   ```python
   def event_loop(queue):
   ```

2. Add tasks to the queue:
   ```python
   task_queue = Queue()

   task_queue.put(lambda: print("Task 1 executed"))
   task_queue.put(lambda: print("Task 2 executed"))

   event_loop(task_queue)
   ```

---

### **Quest 4: Asynchronous Event Loop with Sleep**
Improve the event loop to handle tasks with delays using `time.sleep()`.

1. Modify tasks to include delays:
   ```python
   import time
   def delayed_task(delay, message):
   ```

2. Use the updated `event_loop`:
   ```python
   task_queue = Queue()
   task_queue.put(delayed_task(3, "Task 1 completed"))
   task_queue.put(delayed_task(2, "Task 2 completed"))

   event_loop(task_queue)
   ```

---

### **Quest 5: Asynchronous Tasks with `asyncio`**
Introduce Python’s `asyncio` library to handle concurrency more effectively.

1. Write two asynchronous tasks:
   ```python
   import asyncio

   async def task_1():


   async def task_2():

   ```

2. Run tasks concurrently:
   ```python
   asyncio.run(asyncio.gather(task_1(), task_2()))
   ```

---

### **Quest 6: Build a Custom Event Loop Using `asyncio`**
Write your own event loop using `asyncio` primitives.

1. Create a task scheduler:
   ```python
   async def custom_event_loop(tasks):
   ```

2. Test with multiple asynchronous functions:
   ```python
   tasks = [task_1(), task_2()]
   asyncio.run(custom_event_loop(tasks))
   ```

---

### **Quest 7: Advanced: Scheduling Periodic Tasks**
Extend the custom event loop to allow periodic tasks (e.g., every 2 seconds).

1. Implement periodic tasks:
   ```python
   async def periodic_task(interval, name, stop_after):
   ```

2. Run with custom event loop:
   ```python
   asyncio.run(custom_event_loop([periodic_task(2, "Periodic Task", 10)]))
   ```

---

### **Quest 8: Implement a Producer-Consumer Model**
Simulate producer and consumer tasks sharing a queue.

1. Define producer and consumer:
   ```python
   async def producer(queue):

   async def consumer(queue):

   ```

2. Combine in an event loop:
   ```python
   queue = asyncio.Queue()
   asyncio.run(custom_event_loop([producer(queue), consumer(queue)]))
   ```

---

### **Quest 9: Debugging Event Loops**
Introduce intentional delays or errors in tasks and observe how they affect the loop. Add logging to track execution order.

---

### **Quest 10: Apply in a Real-World Example**
Build a small application that:
- Reads data from a file (producer).
- Processes the data asynchronously (processor).
- Writes the results to another file (consumer).

---

Would you like explanations or solutions for any specific exercise?
