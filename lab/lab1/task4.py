

def word_count(S):
    words = S.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

a=str(input("enter a string   "))
print(word_count(a))
