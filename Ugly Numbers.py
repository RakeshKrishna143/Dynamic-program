#Dynamic solution for Ugly number Problem 

def getNthUglyNo(n):
    ugly_no = [0]*n
    ugly_no[0] = 1
    count_2 = count_3 = count_5 = 0
    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    
    for i in range(1,n):
        ugly_no[i] = min(next_multiple_of_2,next_multiple_of_3,next_multiple_of_5)
        
        if ugly_no[i] == next_multiple_of_2:
            count_2 +=1
            next_multiple_of_2 = ugly_no[count_2] * 2
        if ugly_no[i] == next_multiple_of_3:
            count_3 +=1
            next_multiple_of_3 = ugly_no[count_3] * 3
        if ugly_no[i] == next_multiple_of_5:
            count_5 +=1
            next_multiple_of_5 = ugly_no[count_5] * 5
            
            
    return ugly_no[-1]
n = 150
print(getNthUglyNo(n))
