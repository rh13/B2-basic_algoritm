a=0
b=1
n=input()
print(a)
print(b)
i=1
while i<=n:
    temp=b
    b=a+b
    a=temp
    print(b)
    i=i+1

 
