def Kadane(lst):
    max_sum = []
    max_sum.append(lst[0])
    L = len(lst)
    for i in range(1,L):
        if max_sum[i-1] > 0:
            max_sum.append(max_sum[i-1] + lst[i])
        else:
            max_sum.append(lst[i])
    target_sum = max(max_sum)
    ref = max_sum.index(max(max_sum))
    x = 0
    for i in range(ref,-1,-1):
        x += lst[i]
        if x == target_sum:
            print(a[i:ref+1])
    

    
