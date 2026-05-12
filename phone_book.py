# simple phone book
n=int(input())
phone_book={}
for i in range(n):
    name,phone=input().split(" ")
    phone_book[name]=phone


search=[]
while True:
    try:
        search.append(input())
    except EOFError:
        break
        
for name in search:
    try:
        print(f"{name}={phone_book[name]}")
    except KeyError:
        print("Not found")
        
    
