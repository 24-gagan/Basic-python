def check_number(num):
    if num<0:
        raise ValueError("Negative number are not allowed")
    else:
        print("valid number")
try:
    n=int(input("enter the number"))
    check_number(n)
except ValueError as e:
    print("Exception occured")