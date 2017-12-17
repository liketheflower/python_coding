class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        table = {}
        res = 0
        
        for i in range(len(grid)):
            lst = []
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    lst.append(j)
            for j1 in range(len(lst)):
                for j2 in range(j1 + 1, len(lst)):
                    c = (lst[j1], lst[j2])
                    if c in table:
                        #print i, c
                        res += table[c]
                    table[c] = table.get(c, 0) + 1
        return res
