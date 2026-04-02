import threading
import time
def square(numbers):
    for n in numbers:
        print("square of",n,"is",n*n)
        time.sleep(1)
def cube(numbers):
    for n in numbers:
        print("cube of",n,"is",n*n)
        time.sleep(1)
numbers = [1,2,3,4,5,6,7,8,9,10]
square(numbers)
cube(numbers)
