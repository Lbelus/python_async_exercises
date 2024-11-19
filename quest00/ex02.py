import asyncio
import time


async def my_task(msg, delay):
    print("task is starting")
    await asyncio.sleep(delay)
    print(msg)

async def main():
    task0 = asyncio.create_task(my_task("task00", 3))
    task1 = asyncio.create_task(my_task("task01", 1))
    await task0
    await task1


asyncio.run(main())
