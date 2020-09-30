import heapq
import math
  
def minSum(num,k):
    print(num)
    t = 0
    for x in num:
      x *= -1
    for i in range(k):
        heapq.heapify(num)
        t = heapq.heappop(num)
        heapq.heappush(num,math.floor(t/2))
    return -sum(num)

L1=[5,7,8,9,4,3]
print(minSum(L1,4))
