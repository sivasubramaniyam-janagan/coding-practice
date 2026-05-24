import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    count=0
    for i in range(n):
        for j in range(n-1):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
                count +=1
            
    
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
