a=int(input("enter first number"))
b=int(input("enter second number"))
try:
    z=a/b
except ZeroDivisionError as e:
    print("Zero division error occured")
else:
    print("This will work if above fails")
finally:
    print("This will always run")