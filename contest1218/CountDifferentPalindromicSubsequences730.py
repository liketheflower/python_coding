"""
 Given a string S, find the number of different non-empty palindromic subsequences in S, and return that number modulo 10^9 + 7.

A subsequence of a string S is obtained by deleting 0 or more characters from S.

A sequence is palindromic if it is equal to the sequence reversed.

Two sequences A_1, A_2, ... and B_1, B_2, ... are different if there is some i for which A_i != B_i.

Example 1:

Input: 
S = 'bccb'
Output: 6
Explanation: 
The 6 different non-empty palindromic subsequences are 'b', 'c', 'bb', 'cc', 'bcb', 'bccb'.
Note that 'bcb' is counted only once, even though it occurs twice.

Example 2:

Input: 
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
Output: 104860361
Explanation: 
There are 3104860382 different non-empty palindromic subsequences, which is 104860361 modulo 10^9 + 7.

Note:
The length of S will be in the range [1, 1000].
Each character S[i] will be in the set {'a', 'b', 'c', 'd'}.
"""

"""

class Solution(object):
    def countPalindromicSubsequences(self, S):
#        :type S: str
 #       :rtype: int
        dp = [[] for i in range(len(S))]
        if not S:
            return 0
        dp[0] =[S[0]]
        dp[1] =[S[0],S[1]]
        if S[:2] == S[:2][::-1]:
            dp[1] += [S[:2]]
        for i in range(2,len(S)):
            dp[i]=dp[i-1][::]
            if S[i] not in dp[i-1]:
               dp[i]=dp[i]+[S[i]]
            s_more = []
            for s_ in dp[i]:
                if s_[0] == S[i]:
                   s_new = s_ + S[i]
                   if s_new == s_new[::-1] and s_new not in dp[i] and s_new not in s_more:
                       s_more+=[s_new]
            dp[i]+= s_more
            print dp[-1]
        return len(dp[-1])%(10**9+7)
"""
class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        prime = (10**9) + 7
        vocab = list(set(S))
        mem = dict()
        def search(x, y):
            res = mem.get((x, y), None)
            if res is not None:
                return res
            res = 1
            for nxt in vocab:
                a = S.find(nxt, x)
                if a == -1: continue
                b = S.rfind(nxt, x, y+1)
                if b == -1: continue
                if a == b:
                    res = (res + 1) % prime
                elif a < b:
                    res = (res + search(a+1, b-1) + 1) % prime
            mem[(x,y)] = res
            print "mem", mem
            return res
        return (search(0, n-1) - 1) % prime


                   
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
S = 'bccb'
print S
a=Solution()
print a.countPalindromicSubsequences(S)
       
