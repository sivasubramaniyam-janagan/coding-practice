# Enter your code here. Read input from STDIN. Print output to STDOUT
words=[]

N=int(input())
for i in range (N):
    words.append(input())
    
for s in words:
    even=""
    odd=""
    count=0
    
    for ch in s:
        if count==0:
            even+=ch
        elif count%2 == 0:
            even +=ch
        else:
            odd+=ch
        count+=1
            
    print(f"{even} {odd}")
            
            
