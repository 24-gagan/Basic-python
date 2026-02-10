num = 123456
count=0

temp=num
while temp>0:
    temp=temp//10
    count+=1
print("Total digit",count)