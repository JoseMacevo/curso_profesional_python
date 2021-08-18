from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f"More than {time_elapsed.total_seconds()} seconds")
    return wrapper


@execution_time
def random_function():
    for _ in range(1, 100000000):
        pass


@execution_time
def sum(a: int, b: int) -> int:
    return a + b


@execution_time
def greet(name="Cesar"):
    print(f"Hello {name}")


sum(5, 5)
random_function()
greet()
