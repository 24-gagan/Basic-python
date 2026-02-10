text="My name is gagandeep"
vowels="aeiou"
def vowels_count(text):
    count=0
    for i in text:
        if i in vowels:
            count+=1
    print("Vowels count",count)
def consonants_count(text):
    count=0
    for i in text:
        if i not in vowels:
            count+=1
    print("consonents count",count)
vowels_count(text)
consonants_count(text)