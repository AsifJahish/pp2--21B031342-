

#  Write a Python program to calculate two date difference in seconds.

from datetime import datetime
def difference_date(first, second):
    return (first-second).total_seconds()


date_input= input("Enter datetime in format 'YYYY-MM-DD HH:MM:SS':")
b=datetime.strptime(date_input, '%Y-%m-%d %H:%M:%S')

date_input2= input("Enter the seond datetime in format 'YYYY-MM-DD HH:MM:SS':")
c=datetime.strptime(date_input, '%Y-%m-%d %H:%M:%S')

d= difference_date(b ,c)
print(d)
