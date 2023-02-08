





def is_palindrome(phrase):

    phrase =phrase.lower().replace(" ", "")
    l= len(phrase)
    for i in range(l//2):
        if phrase[i]!= phrase[l-i-1]:
            return False
    return True


phrase=str(input("enter the palindrome phrase   "))

print(is_palindrome(phrase))
