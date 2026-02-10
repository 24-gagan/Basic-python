try:
    a=int(input("enter a numebr"))
    b=int(input("enter second number"))
    result=a/b
except (ValueError,ZeroDivisionError) as e:
    print("exception occured",e)
