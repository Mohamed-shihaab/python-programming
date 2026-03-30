import math
binary=int(input('enter any binary number'))
deci=0
i=0
while binary!=0:
    r=binary%10
    deci=deci+r*math.pow(2,i)
    i+=1
    binary=binary//10
print("binary to decimal conversion",round(deci))
