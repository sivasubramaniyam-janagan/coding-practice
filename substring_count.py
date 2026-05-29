def count_substring(string, sub_string):
    N=len(string)
    n=len(sub_string)
    count = 0
    for i in range(N-n+1):
        if string[i] == sub_string[0]:
            k=i
            increase=True
            for j in range(n):
                if string[k] != sub_string[j]:
                    increase=False
                    break
                k+=1
            if increase:
                count+=1 
        
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
