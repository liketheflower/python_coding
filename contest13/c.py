class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums or sum(nums)%4!=0: return False
        
        N = sum(nums)/4
        nums.sort()
        if nums[-1]>N: return False
        four_length = [N]*4
        memo = {}
        
        def dp(a,idx,four_length_,nums_):
            nums = nums_[:]
            four_length = four_length_[:]
            tuple_ = (a,idx)+tuple(four_length)+tuple(nums)
           # print tuple_
            if tuple_ not in memo:
                four_length [idx]-=a
                if min(four_length)<0:
                    memo[tuple_]=False
                    return False
                if sum(four_length)==0:
                    memo[tuple_]=True
                    return True
                else:
                    if not nums: 
                        memo[tuple_]=False
                        return False
                    b= nums.pop()
                    idxes = [idx for idx in range(4) if four_length[idx]-b >=0]
                    if not idxes: 
                        memo[tuple_]=False
                        return False
                    while idxes:
                        idx = idxes.pop()
                        if dp(b, idx, four_length,nums):
                             memo[tuple_]=True
                             return True
                    memo[tuple_]=False
                    return False
                   # memo[tuple_]=any (dp(b,idx,four_length,nums) for idx in range(4) if four_length[idx]-b >=0)
            return memo[tuple_]
            
                
        a = nums.pop()
        idxes = [idx for idx in range(4) if four_length[idx]-a >=0]
        if not idxes: return False
        while idxes:
            idx = idxes.pop()
            if dp(a, idx, four_length,nums): return True
        return False

a = Solution()
nums = [5,5,5,5,4,4,4,4,3,3,3,3]
print a.makesquare(nums)
