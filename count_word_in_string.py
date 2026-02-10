import re
text = "My name is Gagandeep Singh"
x = re.findall(r'\b\w+\b', text)
print(len(x))

