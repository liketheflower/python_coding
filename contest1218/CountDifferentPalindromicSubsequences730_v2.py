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
class Solution(object):
    def countPalindromicSubsequences(self, S):
        """
        :type S: str
        :rtype: int
        """
        def cache(start, end):            # This function serves to save the result
            print (start, end)
            if end <= start + 2:          # simple cases can be computed directly
                return end - start
            print check,"1"
            if (start, end) not in check: # if not saved, compute and save before returning
                check[(start, end)] = DFS(start, end)
            print check    
            return check[(start, end)]
        
        def DFS(start, end):     #returns the number of distinct palindromes in S[start:end]
            count = 0
            segment = S[start:end]
            
            for x in 'abcd':
                try:
                    i = segment.index(x) + start  # the starting index in S
                    j = segment.rindex(x) + start # the ending index in S
                except:
                    continue
                print check, "3"
                count += cache(i+1, j) + 2 if i != j else 1
            
            return count % 1000000007
                
        check = {}
        return cache(0, len(S))
                   
S = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
S = 'bccbabcd'
#S = 'aa'
print S
a=Solution()
print a.countPalindromicSubsequences(S)
       
