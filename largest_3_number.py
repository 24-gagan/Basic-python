a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if a>b and a>c:
    print("a is greater than both b and c",a)
elif b>a and b>c:
    print("b is greater than both c and a")
else:
    print("c is greater",c)