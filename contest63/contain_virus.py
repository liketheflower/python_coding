import collections
import heapq
class Solution(object):
    def containVirus(self,grid):
        def find_region(virus_lab,region_id):
           
            #init_region_id = region_id 
           region_db={} 
           for i in range(m):
                for j in range(n):
                    if grid[i][j]==virus_lab:
                        region_id+=1
                      #  print "region_id",region_id
                        region_db = dfs((i,j),region_id,region_db)
           virus_lab+=1
           return virus_lab, region_id, region_db
        def dfs((i,j),region_id,region_db):
            open_list, closed = [(i,j)],[]
           # print "region id dfs",region_id
            while open_list:
                (i,j) = open_list.pop()
                closed+=[(i,j)]
                grid[i][j] = virus_lab+1
                for (di,dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if 0<=i+di<m and 0<=j+dj<n and grid[i+di][j+dj]>0:
                        if (i+di,j+dj) not in open_list and (i+di,j+dj) not in closed:
                            open_list+=[(i+di,j+dj)]
            region_db[region_id] = closed
            return region_db
                    
        def get_to_be_infected(region_db):
            heap = []
            to_be_infected =collections.defaultdict(list)
            if not region_db:
                return heap, to_be_infected
            for reg in region_db:
               # to_be_infected[reg] = []
                for (i,j) in region_db[reg]:
                    for (di,dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
                        if 0<=i+di<m and 0<=j+dj<n and grid[i+di][j+dj]==0 and (i+di,j+dj) not in to_be_infected[reg]:
                            to_be_infected[reg]+=[(i+di,j+dj)]
                tem = (-len(to_be_infected[reg]), reg)
                heapq.heappush(heap, tem)
            return heap,to_be_infected
                
        def build_wall(reg, wall,region_db):
            for (i,j) in region_db[reg]:
                grid[i][j] = -1
                for (di,dj) in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if 0<=i+di<m and 0<=j+dj<n and grid[i+di][j+dj]==0:
                        wall+=1
            return wall
                        
        def infect_a_specified_region(reg,virus_lab,to_be_infected):
            for (i,j) in to_be_infected[reg]:
                grid[i][j] = virus_lab
       # region_db={}
       # region_to_be_visted={}
        
        #to_be_infected =collections.defaultdict(list)
        m, n ,region_id,virus_lab= len(grid),len(grid[0]),0,1
        wall = 0
        while True:
            #print grid
            virus_lab, region_id,region_db = find_region(virus_lab,region_id)
            #print "####", region_db
            heap, to_be_infected = get_to_be_infected(region_db)
            #print "heap and to be infected",heap,to_be_infected
            if not heap or not any(to_be_infected[reg] for reg in to_be_infected):
                break
            _, reg = heapq.heappop(heap)
            wall=build_wall(reg,wall,region_db)
           # print "virus id", virus_lab
           # print to_be_infected
            for (_, reg) in heap:
                infect_a_specified_region(reg,virus_lab,to_be_infected)
            #for gr_ in grid:
             #   print gr_
        return wall

        
grid = [[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]
import time
start_time = time.time()
a = Solution()
print a.containVirus(grid)
print("--- %s seconds ---" % (time.time() - start_time))        
