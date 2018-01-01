class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        N =len(heights)
        for i in range(V):
            left, right= False,False
            if K!=0:
                for hei in range(K-1,-1,-1):
                    if heights[hei]<heights[hei+1]:
                        left = True
                        index = hei
                        continue
                    elif heights[hei]==heights[hei+1]:
                        continue
                    else:
                        break
            if left:
                heights[index]+=1
                continue
            if K!=N:
                for hei in range(K+1,N):
                    if heights[hei]<heights[hei-1]:
                        right = True        
                        index = hei
                        break
                    elif heights[hei]==heights[hei-1]:
                        continue
                    else:
                        break
            if right:
                heights[index]+=1
                continue
            heights[K]+=1
        return heights

s = Solution()
mm =[1,2,3,4,3,2,1,2,3,4,3,2,1]
print "mm",mm
print s.pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1],5,5)
print s.pourWater([1,2,3,4],2,2)
print s.pourWater([3,1,3],5,1)
