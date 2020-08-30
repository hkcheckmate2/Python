def climbStairs(n)
  num = [0,1]
  for i in range(0,n,2):
    num[0] = num[0] + num[1]
    num[1] = num[1] + num[0]
  return num[(n+1)%2]
