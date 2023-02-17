
#Write a Python program to drop microseconds from datetime.
from datetime import datetime

def drop_microsecond():
    
    today= datetime.now()
    today = today.replace(microsecond=0)

    return today
a= drop_microsecond()
print(a)