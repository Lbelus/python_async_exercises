from time import sleep


def timer(delay, callback):
    print("timer has started")
    sleep(delay)
    callback();


def on_timer_complete():
    print("Timer completed!")

timer(3, on_timer_complete)
