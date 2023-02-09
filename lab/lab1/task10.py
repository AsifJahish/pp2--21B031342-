

def count_letters(word):
    letter_counts = {}
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1
    for letter, count in letter_counts.items():
        print(f"{letter}: {count}")

word = "international"
count_letters(word)
