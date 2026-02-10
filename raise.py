def divide(a,b):
    if b==0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a/b
try:
    result=divide(10,5)
    print("Result",result)

    result=divide(5/0)
    print("Result",result)
except ZeroDivisionError as e:
    print("Exception occured {e}")
