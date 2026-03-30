n=int(input('enter a value'))
a=-1
b=1
i=0
while i<n:
    c=a+b
    print(c,end=' ')
    a=b
    b=c
    i+=1
