import re
class Solution(object):
    def findPermutation(self, s):
        a = range(1, len(s) + 2)
        for m in re.finditer('D+', s):
            i, j = m.start(), m.end() + 1
            a[i:j] = a[i:j][::-1]
        return a


solution = Solution()
s ='IDDIIDDI'
print solution.findPermutation(s)
