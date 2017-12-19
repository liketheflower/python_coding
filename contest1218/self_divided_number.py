class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        if left>right:
            return []
        res = []
        for i in range(left,right+1):
            if str(i).count('0')==0:
                indicator = True
                for k in str(i):
                   if i%int(k) !=0:
                     indicator =False
                     break
                if indicator:
                    res.append(i)
        return res

a=Solution()
print a.selfDividingNumbers(1, 22)
