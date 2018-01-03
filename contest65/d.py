class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[1])
        print intervals
        low, high, ans= -1, -1, 0
        for interval in intervals:
            print low, high,ans
            if interval[0]>high:
                print "a",interval
                ans+=2
                low,high=interval[1]-1,interval[1]
            elif interval[0]>low:
                print "b", interval
                ans+=1
                low= high-1 if high==interval[1] else high
                high=interval[1]
        print low, high,ans
        return ans


a = Solution()
intervals = [[1, 2],  [100, 101]]
a.intersectionSizeTwo(intervals)
