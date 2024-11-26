import asyncio

async def task(msg, delay):
    print(msg + " is starting")
    await asyncio.sleep(delay)
    print(msg + " has ended")
    return msg


async def get_tasks(inputs):
    cors = [asyncio.create_task(task(msg, delay)) for msg, delay in inputs]
    results = asyncio.gather(*cors)
    print(await results)

asyncio.run(get_tasks([("task1", 3), ("task2", 1)]))

