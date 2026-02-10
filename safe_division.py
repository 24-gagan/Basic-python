def safe_division(a,b):
    try:
        result=a/b
        return result
    except ZeroDivisionError as e:
        print("Error occured")
print(safe_division(10,3))
print(safe_division(5,0))