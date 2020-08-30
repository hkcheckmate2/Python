def minPathSum(grid):
    col = len(grid[0])
    row = len(grid)
    dp = [[0 for j in range(col)]for i in range(row)]    
    for x in range(0,row):
        for y in range(0,col):
            if x == 0 or y == 0:
                if x == y:
                    dp[0][0] = grid[x][y]
                elif x == 0:
                    dp[x][y] = grid[x][y] + dp[x][y-1]
                else:
                    dp[x][y] = grid[x][y] + dp[x-1][y]
            else:
                dp[x][y] = grid[x][y] + min(dp[x-1][y],dp[x][y-1])
    return dp[row-1][col-1]
