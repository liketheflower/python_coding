class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_av = sum(nums[:k])/float(k)
        for i in range(1,len(nums)-k+1):
            if nums[i+k-1]<=nums[i-1]:
                continue
            else:
                max_av = max(max_av, sum(nums[i:i+k])/float(k))
        return max_av
            #1234
        #0,1
nums = [0,1,1,3,3]

k=4

a=Solution()
print a.findMaxAverage(nums, k)


