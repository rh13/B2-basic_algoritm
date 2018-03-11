flag=1
i=2
n=input()
while i<(n/2):
 if (n%i==0):
   flag=0
 i=i+1
if flag==0:
  print(n,"is not prime")
else:
 print(n,"is prime")
