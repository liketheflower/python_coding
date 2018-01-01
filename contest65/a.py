import collections
import heapq
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        db =collections.defaultdict(int)
        heap = [(0,0)]
      #  heapq.heappush(heap,(target-0,(0,0)))
       # if abs(target)>10:
        #     patience = 0
       # else:
        #     patience = 4
        import math
        target=abs(target)
        
#        N=math.sqrt(abs(2*target))+1
        res = []
        while heap:
            node = heap.pop(0)
           # print "dis,node",dis,node
            if node[0] == target:
           #     print node
                return node[1]
            depth = node[1]+1
            v1,v2 = node[0]-depth,node[0]+depth
          #  print v1,v2,depth
            if v1>0:
                heap.append((v1,depth))
            if v2>0:
                heap.append((v2,depth))

t =Solution()
print t.reachNumber(4)
print t.reachNumber(-1)
print t.reachNumber(8)
print t.reachNumber(-10000)
