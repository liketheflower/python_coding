class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        binary_ = bin(n)[2:]
        for i in range(1,len(binary_)):
            if binary_[i] == binary_[i-1]:
                return False
        return True

test = Solution()

print test.hasAlternatingBits(11)
print test.hasAlternatingBits(10)
