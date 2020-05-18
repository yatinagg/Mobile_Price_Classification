def prime(n):
    size = int(n**(0.5)+1)
    for i in range (2,size):
        if(n%i == 0):
            return False
    return True
def printPrime(a,b):
    for i in range(a,b+1):
        if(prime(i)):
            print(i,end=" ")
x = 100
y = 300
printPrime(x,y)