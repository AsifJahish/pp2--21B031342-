

#  Write a Python program to calculate two date difference in seconds.

from datetime import datetime

# get the two dates as strings from the user
date1 = input("Enter the first date (YYYY-MM-DD HH:MM:SS): ")
date2 = input("Enter the second date (YYYY-MM-DD HH:MM:SS): ")

# convert the strings to datetime objects
date1_obj = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S')
date2_obj = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S')

# calculate the difference between the two dates in seconds
diff_seconds = abs((date2_obj - date1_obj).total_seconds())

# print the result
print("The difference between the two dates is {} seconds".format(diff_seconds))
