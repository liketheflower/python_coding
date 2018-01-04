import collections

class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def around(r,c,t=None):
            for d in (-1,1):
                for (rr,cc) in ((r+d,c), (r,c+d)):
                    if 0<=rr<m and 0<=cc<n and (t == None or grid[rr][cc]==t):
                        yield (rr,cc)
        def find_region(region_id):
            region_db={}
            seen = set()
            for i in xrange(m):
                for j in xrange(n):
                    if grid[i][j]==1 and (i,j) not in seen:
                        region_id+=1
                        region_list = dfs((i,j))
                        seen.update(region_list)
                        region_db[region_id] = region_list
            return region_id,region_db
        def dfs((i,j)):
            open_list, closed = [(i,j)],[]
            while open_list:
                (i,j) = open_list.pop()
                closed+=[(i,j)]
                for (ii,jj) in around(i,j,1):
                    if (ii,jj) not in open_list and (ii,jj) not in closed:
                        open_list+=[(ii,jj)]
            return closed
        def get_to_be_infected(region_db):
            to_be_infected =collections.defaultdict(list)
            if not region_db:
                return to_be_infected
            for reg in region_db:
                for (i,j) in region_db[reg]:
                    for (ii,jj) in around(i,j,0):
                       to_be_infected[reg]+=[(ii,jj)]
            return to_be_infected
        def build_wall(reg,region_db):
            for (i,j) in region_db[reg]:
                grid[i][j] = -1

        def infect_a_specified_region(reg,to_be_infected):
            if to_be_infected[reg]:
                for (i,j) in to_be_infected[reg]:
                    grid[i][j] = 1
        m, n ,region_id= len(grid),len(grid[0]),0
        gwall = 0
        while True:
            region_id,region_db = find_region(region_id)
            to_be_infected = get_to_be_infected(region_db)
            if not any(to_be_infected[reg] for reg in to_be_infected):
                break
            reg = max(to_be_infected.keys(),key=lambda reg:len(set(to_be_infected[reg])))
            gwall+= len(to_be_infected[reg])
            build_wall(reg,region_db)
            to_be_infected[reg] = []
            for reg in to_be_infected:
                infect_a_specified_region(reg,to_be_infected)
        return gwall
        
grid = [[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]
import time
grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
start_time = time.time()
a = Solution()
print a.containVirus(grid)
print("--- %s seconds ---" % (time.time() - start_time))        
