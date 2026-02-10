from collections import Counter

str1 = "listen"
str2 = "silent"
if Counter(str1)==Counter(str2):
    print("Anagrams")
else:
    print("Not anagrams")