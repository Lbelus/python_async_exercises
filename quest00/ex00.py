from time import sleep


def my_task(msg, delay):
    sleep(delay)
    print(msg)

my_task("task00", 3)

my_task("task01", 2)
