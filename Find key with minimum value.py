data = {"a": 10, "b": 25, "c": 15}
dict1 = min(data, key=data.get)
print(dict1)
