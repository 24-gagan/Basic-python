s = "programming"
seen=set()
result=""
for char in s:
    if char not in seen:
        result+=char
        seen.add(char)
print(result)