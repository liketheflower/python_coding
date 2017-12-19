from collections import defaultdict
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        r, c =  len(grid), len(grid[0])
        finished = defaultdict(int)
        res_ = {finished[(i,j)] for i in range(r)
                         for j in range(c) if grid[i][j] == 0}

        def dfs(i,j):
            open_list.append((i,j))
            while open_list:
                 i,j = open_list.pop()
                 finished[(i,j)]
                 close_list.append((i,j))
                 temp = [(m,n) for m,n in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)] if m>=0 and m<r and n>=0 and n<c and grid[m][n]]
                 if temp:
                     for item in temp:
                        if item not in open_list and item not in close_list:
                            open_list.append(item)
            res_.add(len(close_list))
        for i in range(r):
            for j in range(c):
               if (i,j) not in finished:
                   open_list = []
                   close_list = []
                   dfs(i,j)
        return max(res_)

test = Solution()
a=[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#a=[[1,1],[1,0]]
print test.maxAreaOfIsland(a)
                 
