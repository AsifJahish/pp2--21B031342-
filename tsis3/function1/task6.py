
#       Write a function that accepts string from user, 
# return a sentence with the words reversed. We are ready -> ready are We

def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)

s= str(input("enter the sentence you want to revers    "))
print(reverse_words(s))

