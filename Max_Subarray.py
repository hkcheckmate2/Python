def Kadane(A):
    Length = len(A)
    Sum = [0]
    Sum *= Length
    Sum[0] = A[0]
    for i in range(1,Length):
        if Sum[i-1] > 0:
            Sum[i] = Sum[i-1] + A[i]
        else:
            Sum[i] = A[i]
    Target_Sum = max(Sum)
    ref = Sum.index(Target_Sum)
    x = ref
    s = 0
    while(s != Target_Sum):
        s += A[x]
        x -= 1
    start = x + 1
    return A[start:ref+1]
"""
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
"""
