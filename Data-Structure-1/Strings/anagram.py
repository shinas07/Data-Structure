
def count_chars(word):
    count = {}
    for char in word:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1


def are_anagrams(w1, w2):
    if count_chars(w1) == count_chars(w2):
        print('Anagram')
    else:
        print("Not Anagram")

w1 = "listen"
w2 = "silent"

are_anagrams(w1,w2)