import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print("Execution time:", end - start, "seconds")
        return result
    return wrapper

@timer
def heavy_task():
    total = 0
    for i in range(10000000):
        total += i
    print("Sum:", total)

heavy_task()
#output:-
#Sum: 49999995000000
#Execution time: 0.6057400703430176 seconds
