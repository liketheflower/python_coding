import collections
import heapq
import numpy as np

class Test(object):
    def f(self, grid):
        print grid
        x=10
        db = collections.defaultdict(list)
        print db
        def f1():
            print "grid with 1", grid
           # global x
            #x+=1
            db['t']=[1,2,3,4]
            print db
            grid[0][0] = 100
            grid.append([1,2,3,4])
            print "grid with 2", grid
        f1()
        def f2():
            print "grid with 1", grid
           # x+=1
            db['t']=[11,22,33,44,55,6611,22,33,44,55,6611,22,33,44,55,6611,22,33,44,55,6611,22,33,44,55,6611,22,33,44,55,6611,22,33,44,55,6611,22,33,44,55,6611,22,33,44,55,6611,22,33,44,55,6611,22,33,44,55,66]
            #db['t']=[1,2,3,4]
            print "within f2", db
        f2()
        print db
        print "grid out",grid

a= Test()

grid = [[1,2],[3,4]]
a.f(grid)


