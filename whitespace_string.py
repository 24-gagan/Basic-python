#6.	Count vowels and consonants in a string.
str1="My name is gagan"
vowel="aeiouAEIOU"
def vowel_num(str1):
    count=0
    for num in str1:
        if num in vowel:
            count+=1
    print("vowel num is",count)
def consonent_num(str1):
    count=0
    for num in str1:
        if num.isalpha() and num not in vowel:
            count+=1
    print("consonent num is",count)

vowel_num(str1)
consonent_num(str1)