class Solution(object):
    # top down + memo
    def find_number_paths(self, grid):
        if not grid or not grid[0]: return 0
        R,C = len(grid), len(grid[0])
        memo = {}
        def dp(i,j):
            if (i,j) not in memo:
                if grid[i][j]:
                    memo[(i,j)] =0
                    return 0
                if (i,j) ==(R-1,C-1):
                    memo[(i,j)] =1
                    return 1
                tem = [(ii,jj) for ii,jj in [(i,j+1),(i+1,j)] if ii<R and jj<C]
                memo[(i,j)] = sum(dp(ii,jj) for ii,jj in tem)
            return memo[(i,j)]
            
        return dp(0,1)+dp(1,0)
    def find_number_paths_bottom_up(self, grid):
        if not grid or not grid[0]: return 0
        R,C = len(grid), len(grid[0])
        dp = [[0 for j in range(C)] for i in range(R)]
        for i in range(R-1,-1,-1):
            for j in range(C-1,-1,-1):
               # print "I am here"
                if i==R-1 and j==C-1:
                    dp[i][j] = 1
                    continue
                if grid[i][j]: continue
                tem = [(ii,jj) for ii, jj in [(i+1,j),(i,j+1)] if ii<R and jj<C]
                dp[i][j] = sum(dp[ii][jj] for ii, jj in tem)
        return dp[0][0]


a = Solution()
grid = [[0 for i in range(8)] for j in range(8)]
grid[1][2]=1
grid[1][-2]=1
grid[2][4]=1
grid[3][0]=1
grid[3][2]=1
grid[3][5]=1

grid[4][2]=1
grid[5][3:5]=[1,1]
grid[5][-2]=1
grid[6][1]=1
grid[6][-3]=1

print a.find_number_paths(grid)
print grid
print a.find_number_paths_bottom_up(grid)
