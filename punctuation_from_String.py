import string

text = "Hello!!! How are you? I'm fine, thank you."

result=""
for i in text:
    if i not in string.punctuation:
        result+=i
print(result)