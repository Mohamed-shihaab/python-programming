num=int(input('Enter a number'))
flag=0
for i in range(2,num//2):
    if num %i==0:
        flag=1
if flag ==0:
    print(num,"is prime number")
else:
    print(num,"is not prime number")
    
