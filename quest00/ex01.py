import asyncio
import time


async def my_task(msg, delay):
    print("task is starting")
    await asyncio.sleep(delay)
    print(msg)

async def main():
    my_task("task 00 has ended", 3)
    my_task("task 01 has ended", 1)


asyncio.run(main())
