num = 123456
sum_digits=0
temp=num

while temp>0:
    digit=temp%10
    sum_digits+=digit
    temp//=10
print("Sum of digits",sum_digits)