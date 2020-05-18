def armstrong(n):
    sum = 0
    x = n
    while(n):
        d = n%10
        sum += d**3
        n = n//10
    if(sum == x):
        return True
    return False
n = int(input("Enter a number "))
if(armstrong(n)):
    print("Number is Armstrong Number")
else:
    print("Number is not Armstrong Number")