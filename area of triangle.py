import math
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
s=(a+b+c)/2
area = math.sqrt(s *(s-a)*(s-b)*(s-c))
print("Area of Tringle is ",area)
