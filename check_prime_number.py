
x=int(input())
def is_prime(x):
  for n in range(2,x):
      if x%n==0:
         return False
  return True
if is_prime(x):
 print(x, "is a prime number")
else: print(x, "is not a prime number")