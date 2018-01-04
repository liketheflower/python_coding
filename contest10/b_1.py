class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal:
            return False
        if desiredTotal<=0:
            return True
        def dp(a,target):
           if not a:
               return False
           if sum(a)<target:
               return False
           if max(a)>=target:
              return True
           for i in range(len(a)):
               if not dp(a[:i]+a[i+1:], target - a[i]):
                   return True
           return False
        return dp(range(1,maxChoosableInteger+1), desiredTotal)
a=Solution()
print a.canIWin(10,40)
