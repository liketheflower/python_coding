class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        tem = [(num, index) for index, num in enumerate (self.nums) if num==target]
        return random.choice(tem)[1]
        


# Your Solution object will be instantiated and called as such:
nums = [1,2,3,3,3]
obj = Solution(nums)
print obj.pick(3)
