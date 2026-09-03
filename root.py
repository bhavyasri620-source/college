import math
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
d=b**2-4*a*c
if d>0:
    print("root are distinct")
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print("x1=",x1)
    print("x2=",x2)
elif d==0:
    x3=-b/(2*a)
    print("x3=",x3)
    print("root are equal")
else:
    print("roots are imaginary")
    
