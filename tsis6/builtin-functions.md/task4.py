import time
import math

def squareAfterTime(number, wait_time):

    time.sleep(wait_time / 1000)

    sqrt = math.sqrt(number)
    return sqrt


number= int(input("enter a Number   "))
wait_time= int(input("enter the time   "))
print(f"The square root of {number} is {squareAfterTime(number, wait_time)} after {wait_time} millisecond")
