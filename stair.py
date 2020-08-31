def climbStairs(n)
  num = [0,1]
  for i in range(0,n,2):
    num[0] = num[0] + num[1]
    num[1] = num[1] + num[0]
  return num[(n+1)%2]

"""
if stepsize = [1,2,4,5,7]
def climbStairs(n,stepsize)
  s = len(stepsize)
  num = [0 for i in range(s+1)]
  num[0] = 1
  for i in range(1,s+1):
    for x in stepsize:
      num[i] += num[i-x]
  
  for i in range(1,n+1,s):
    for j in range(1,(s+1)%s):
      num[i] += num[i+j]
  return num[(n+2)%s]
  
  
  num = [0 for i in range(s)]
  for i in range(s):
    for x in stepsize:
      num[i] += num[i-x]
   
"""
