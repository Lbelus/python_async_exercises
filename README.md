### Step-by-Step Exercises to Master Event Loops in Python

Event loops are the backbone of asynchronous programming, and Python provides tools like `asyncio` to work with them. Let’s build the concept organically with exercises.

---

### **Exercise 1: Understand Blocking vs. Non-Blocking Code**
Write a simple program where two tasks are executed sequentially (blocking) and then rewrite it to simulate non-blocking behavior.

1. **Sequential (Blocking)**:
   - Task 1: Sleep for 3 seconds and print a message.
   - Task 2: Sleep for 2 seconds and print a message.

2. **Non-Blocking Simulation**:
   - Print "Task 1 started", then after 3 seconds, print "Task 1 finished".
   - Simultaneously, start "Task 2" and finish it in 2 seconds.

---

### **Exercise 2: Building a Simple Timer with Callbacks**
Implement a timer function that takes a delay and a callback. The callback is called after the delay.

1. Write a `timer` function:
   ```python
   import time

   def timer(delay, callback):
       print(f"Timer started for {delay} seconds.")
       time.sleep(delay)
       callback()
   ```

2. Test it with:
   ```python
   def on_timer_complete():
       print("Timer completed!")

   timer(3, on_timer_complete)
   ```

---

### **Exercise 3: Introduce the Event Queue**
Simulate an event loop by creating a queue where you push tasks (functions) to be executed later.

1. Create a queue and an executor:
   ```python
   from queue import Queue

   def event_loop(queue):
       while not queue.empty():
           task = queue.get()
           task()
   ```

2. Add tasks to the queue:
   ```python
   task_queue = Queue()

   task_queue.put(lambda: print("Task 1 executed"))
   task_queue.put(lambda: print("Task 2 executed"))

   event_loop(task_queue)
   ```

---

### **Exercise 4: Asynchronous Event Loop with Sleep**
Improve the event loop to handle tasks with delays using `time.sleep()`.

1. Modify tasks to include delays:
   ```python
   import time

   def delayed_task(delay, message):
       def task():
           time.sleep(delay)
           print(message)
       return task
   ```

2. Use the updated `event_loop`:
   ```python
   task_queue = Queue()
   task_queue.put(delayed_task(3, "Task 1 completed"))
   task_queue.put(delayed_task(2, "Task 2 completed"))

   event_loop(task_queue)
   ```

---

### **Exercise 5: Asynchronous Tasks with `asyncio`**
Introduce Python’s `asyncio` library to handle concurrency more effectively.

1. Write two asynchronous tasks:
   ```python
   import asyncio

   async def task_1():
       await asyncio.sleep(3)
       print("Task 1 completed")

   async def task_2():
       await asyncio.sleep(2)
       print("Task 2 completed")
   ```

2. Run tasks concurrently:
   ```python
   asyncio.run(asyncio.gather(task_1(), task_2()))
   ```

---

### **Exercise 6: Build a Custom Event Loop Using `asyncio`**
Write your own event loop using `asyncio` primitives.

1. Create a task scheduler:
   ```python
   async def custom_event_loop(tasks):
       await asyncio.gather(*tasks)
   ```

2. Test with multiple asynchronous functions:
   ```python
   tasks = [task_1(), task_2()]
   asyncio.run(custom_event_loop(tasks))
   ```

---

### **Exercise 7: Advanced: Scheduling Periodic Tasks**
Extend the custom event loop to allow periodic tasks (e.g., every 2 seconds).

1. Implement periodic tasks:
   ```python
   async def periodic_task(interval, name, stop_after):
       start = asyncio.get_event_loop().time()
       while asyncio.get_event_loop().time() - start < stop_after:
           print(f"{name} executed")
           await asyncio.sleep(interval)
   ```

2. Run with custom event loop:
   ```python
   asyncio.run(custom_event_loop([periodic_task(2, "Periodic Task", 10)]))
   ```

---

### **Exercise 8: Implement a Producer-Consumer Model**
Simulate producer and consumer tasks sharing a queue.

1. Define producer and consumer:
   ```python
   async def producer(queue):
       for i in range(5):
           await asyncio.sleep(1)
           print(f"Produced {i}")
           await queue.put(i)

   async def consumer(queue):
       while True:
           item = await queue.get()
           print(f"Consumed {item}")
           if item is None:
               break
   ```

2. Combine in an event loop:
   ```python
   queue = asyncio.Queue()
   asyncio.run(custom_event_loop([producer(queue), consumer(queue)]))
   ```

---

### **Exercise 9: Debugging Event Loops**
Introduce intentional delays or errors in tasks and observe how they affect the loop. Add logging to track execution order.

---

### **Exercise 10: Apply in a Real-World Example**
Build a small application that:
- Reads data from a file (producer).
- Processes the data asynchronously (processor).
- Writes the results to another file (consumer).

---

Would you like explanations or solutions for any specific exercise?
