n = int(input("enter a number"))
for i in range(1, n + 1):
    if i % n == 0:
        print("number is prime number", n)
    else:
        print("not a prime number", n)
