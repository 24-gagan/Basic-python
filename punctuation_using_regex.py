import re

text = "Hello!!! How are you? I'm fine, thank you."

result=re.sub(r'[^\w\s]','',text)
print(result)