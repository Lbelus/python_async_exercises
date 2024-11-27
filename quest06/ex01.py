import asyncio


async def periodic_task(interval, msg, stop_after):
    start = asyncio.get_event_loop().time()
    while asyncio.get_event_loop().time() - start < stop_after:
        print(f"{msg} executed")
        await asyncio.sleep(interval)

async def get_tasks(inputs):
    cors = [asyncio.wait_for([periodic_task(interval, msg, delay), timeout=10) for msg, delay in inputs]
    try:
        results = await asyncio.gather(*cors)
        print(results)
    except asyncio.TimeoutError as err:
        print("A task timed out:", err)

asyncio.run(get_tasks([(2, "task1", 4), (1, "task2", 5)]))

