class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        for _ in range(V):
            print _
            print heights
            index = -1
            for i in range(K-1, -1, -1):
                if heights[i] > heights[i+1]:
                    break
                elif heights[i] < heights[i+1]:
                    index = i
            if index != -1:
                heights[index] += 1
                continue

            index = -1
            for i in range(K+1, len(heights)):
                if heights[i] > heights[i-1]:
                    break
                elif heights[i] < heights[i-1]:
                    index = i
            if index != -1:
                heights[index] += 1
            else:
                heights[K] += 1
        return heights

s = Solution()
mm =[1,2,3,4,3,2,1,2,3,4,3,2,1]
print "mm",mm
print s.pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1],5,5)
print s.pourWater([1,2,3,4],2,2)
print s.pourWater([3,1,3],5,1)


print s.pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1],10,2)
