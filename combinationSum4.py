class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for x in range(target+1)]
        dp[0] = 1
        for i in range(1,target+1):
            for NUM in nums:
                if NUM <= i:
                    dp[i] += dp[i-NUM]
                #target - num score krne k tareeke
        return dp[target]
        
"""
for i in 1...Target:
for x in nums:
dp[i] += dp[i-x]
initilized value:
   1 0 0 0 0 0 0 0 0 0
dp 0 1 2 3 4 5 6 7 8 9
"""
