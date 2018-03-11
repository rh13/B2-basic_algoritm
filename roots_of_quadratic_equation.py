import cmath
a=float(input())
b=float(input())
c=float(input())
d=b**b-float(4*a*c)
m=cmath.sqrt(d)
n=cmath.sqrt(-d)
if d>=0:
  r1=(-b+m)/2*a
  r2=(-b-m)/2*a 
  print(r1,r2)
else:
  rp=b/2*a
  ip=n/2*a
  print(rp,ip,rp,ip)
