from collections import Counter
text = "mississippi"
Count=Counter(text)
var=Count.most_common(1)[0]
print(var[0])
print(var[1])