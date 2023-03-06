
# # Write a Python program with builtin function that checks whether a passed string is palindrome or not.
# class name:
#     def isPalindrome(st):
#         for i in range(0, int(len(st)/2)):
#          if st[i] != st[len(st)-i-1]:
#             return False
        
#         return True
    



# st= str(input("Enter a String    "))
# str= name(isPalindrome(st))
# print(str)

import string
string = input("Enter yor string")

for i in range (len(string)):
    if string[::-1] == string[i]:
        print("Your string is Palindrome")
else:
    print("Your string is not palindrome")