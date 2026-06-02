# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def isprime(n):
    if n== 1:
        print("Not prime")
        return 
    prime = True
    for i in range(2, math.isqrt(n) + 1):
        if n%i == 0:
            prime = False
            break
    if prime:
        print("Prime")
    else:
        print("Not prime")



n=int(input())
test=[]
for i in range (n):
    test.append(int(input()))
    
for i in test:
    isprime(i)
