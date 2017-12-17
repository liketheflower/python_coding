
"""
 A virus is spreading rapidly, and your task is to quarantine the infected area by installing walls.

The world is modeled as a 2-D array of cells, where 0 represents uninfected cells, and 1 represents cells contaminated with the virus. A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall. Resources are limited. Each day, you can install walls around only one region -- the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night. There will never be a tie.

Can you save the day? If so, what is the number of walls required? If not, and the world becomes fully infected, return the number of walls used.

Example 1:

Input: grid = 
[[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]
Output: 10
Explanation:
There are 2 contaminated regions.
On the first day, add 5 walls to quarantine the viral region on the left. The board after the virus spreads is:

[[0,1,0,0,0,0,1,1],
 [0,1,0,0,0,0,1,1],
 [0,0,0,0,0,0,1,1],
 [0,0,0,0,0,0,0,1]]

On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.

Example 2:

Input: grid = 
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output: 4
Explanation: Even though there is only one cell saved, there are 4 walls built.
Notice that walls are only built on the shared boundary of two different cells.

Example 3:

Input: grid = 
[[1,1,1,0,0,0,0,0,0],
 [1,0,1,0,1,1,1,1,1],
 [1,1,1,0,0,0,0,0,0]]
Output: 11
Explanation: The region on the left only builds two new walls.
"""




class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        self.walls = {}
    
        while True:
            lst = self.findRegions(grid)
            if not lst: return res
            
            for i, j in lst:
                for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if (i, j, ii, jj) not in self.walls and 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == 0:
                        res += 1
                        self.walls[(i, j, ii, jj)] = 1
                        self.walls[(ii, jj, i, j)] = 1
                        # print i, j, ii, jj
            # print 'aaa'
            for i, j in lst:
                grid[i][j] = 2

            self.spread(grid)
    
    def findRegions(self, grid):
        tmp = []
        num = -1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    lst, affect = self.findRegion(grid, i, j)
                    num1 = len(set(affect))
                    
                    if num1 > num:
                        tmp = lst
                        num = num1
                        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] %= 10
                
        return tmp
    
    def findRegion(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]): return [], []
        
        if grid[i][j] == 0: return [], [(i, j)]
        
        if grid[i][j] != 1: return [], []
        
        res = [(i, j)]
        affect = []
        grid[i][j] += 10
        
        for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if (i, j, ii, jj) not in self.walls:
                res1, a1 = self.findRegion(grid, ii, jj)
                res += res1
                affect += a1
        
        return res, affect
        
    
    def spread(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for ii, jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if (i, j, ii, jj) not in self.walls and 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == 0:
                            grid[ii][jj] = 11
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] %= 10

