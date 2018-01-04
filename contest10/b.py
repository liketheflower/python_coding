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
        rounds = 0
        candidates = range(1,maxChoosableInteger+1 )
        win = False
        for i in xrange(maxChoosableInteger):
            if desiredTotal-candidates[-1]<=0:
                candidates.pop()
                win= True
                break
                rounds+=1   
            else:
                tem = candidates.pop(0)
                print tem
                desiredTotal-=tem
                rounds+=1
        if not win:
            return False
        if win and (rounds+1)&1:
            return True
        return False

a=Solution()
print a.canIWin(10,40)
