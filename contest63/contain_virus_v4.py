import collections
class Solution(object):
    def containVirus(self, grid):
        def around(r,c,t=None):
            # all cells 1-step away from (r,c)
            # optionally, if t!=None, target value must be t
            for d in (-1,1):
                for (rr,cc) in ((r+d,c), (r,c+d)):
                    if 0<=rr<m and 0<=cc<n and (t == None or grid[rr][cc]==t):
                        yield (rr,cc)
        def find_region(virus_lab,region_id):
            region_db={}
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==virus_lab:
                        region_id+=1
                        dfs((i,j),region_id,region_db)
            virus_lab+=1
            return virus_lab, region_id,region_db
        def dfs((i,j),region_id,region_db):
            open_list, closed = [(i,j)],[]
            while open_list:
                (i,j) = open_list.pop()
                closed+=[(i,j)]
                grid[i][j] = virus_lab+1
                for (i,j) in around(i,j,virus_lab):
                        if (i,j) not in open_list and (i,j) not in closed:
                            open_list+=[(i,j)]
            region_db[region_id] = closed
        def update_region(region_db,to_be_infected):
            region_db_={}
            if region_db:
                for reg in region_db:
                    region_db[reg] = set(region_db[reg]) | set(to_be_infected[reg])
                regs = region_db.keys()
                for i in xrange(len(regs)-1):
                    combine = False
                    for j in xrange(i+1,len(regs)):
                        if region_db[regs[i]] & region_db[regs[j]]:
                            region_db[regs[j]]|=region_db[regs[i]]
                           # region_db[regs[i]] = set()
                           # break
                            combine= True
                    if combine:
                        region_db[regs[i]] =set()
                for reg in region_db:
                    if region_db[reg]:
                        region_db_[reg]=region_db[reg]
                return region_db_
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

        def infect_a_specified_region(reg,virus_lab,to_be_infected):
            if to_be_infected[reg]:
                for (i,j) in to_be_infected[reg]:
                    grid[i][j] = virus_lab
        m, n ,region_id,virus_lab= len(grid),len(grid[0]),0,1
        gwall = 0
        while True:
            if virus_lab ==1:
                virus_lab, region_id,region_db = find_region(virus_lab,region_id)
            else:
                region_db=update_region(region_db,to_be_infected)
            to_be_infected = get_to_be_infected(region_db)
            for _ in region_db:
                print sorted(list(region_db[_])), sorted(list(to_be_infected[_]))
            if not any(to_be_infected[reg] for reg in to_be_infected):
                break
            reg = max(to_be_infected.keys(),key=lambda reg:len(set(to_be_infected[reg])))
            print reg, gwall
            gwall+= len(to_be_infected[reg])
            build_wall(reg,region_db)
            region_db.pop(reg)
            to_be_infected.pop(reg)
            for reg in to_be_infected:
                infect_a_specified_region(reg,virus_lab,to_be_infected)
        return gwall
        
grid = [[0,1,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,1],
 [0,0,0,0,0,0,0,0]]

grid = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,0],[1,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,1,0,0,0],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,1,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
for gr in grid:
    print gr
import time
start_time = time.time()
a = Solution()
print a.containVirus(grid)
print("--- %s seconds ---" % (time.time() - start_time))        
