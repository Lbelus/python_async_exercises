import asyncio

async def task_1():
    await asyncio.sleep(3)
    print("Task 1 completed")

async def task_2():
    await asyncio.sleep(2)
    print("Task 2 completed")


async def main():
    await asyncio.gather(task_1(), task_2())

# Run the event loop
asyncio.run(main())
