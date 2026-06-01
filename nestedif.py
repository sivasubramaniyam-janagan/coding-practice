
day,month,year = map(int, input().split(" "))
due_day , due_month,  due_year = map(int,input().split(" "))

fine=0
if year > due_year:
    fine=10000
elif year==due_year:
    if month > due_month:
        fine=(month-due_month)*500
    elif month==due_month :
        if day>due_day:
            fine=(day-due_day)*15
        
print(fine)
