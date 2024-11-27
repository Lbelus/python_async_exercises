import asyncio

async def task(msg, delay):
    print(msg + " is starting")
    await asyncio.sleep(delay)
    print(msg + " has ended")
    return msg


async def get_tasks(inputs):
    cors = [asyncio.wait_for(task(msg, delay), timeout=4) for msg, delay in inputs]
    try:
        results = await asyncio.gather(*cors)
        print(results)
    except asyncio.TimeoutError as err:
        print("A task timed out:", err)

asyncio.run(get_tasks([("task1",4),("task2", 3), ("task3", 1)]))

