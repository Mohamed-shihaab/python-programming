def function(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
        return fact
def ncr(n,r):
    return factorial(n) // (factorial(r) * factorial(n - r))
n=int(input("Enter n value : "))
r=int(input("Enter r value : "))
print(function (num))
