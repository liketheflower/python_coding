class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 0
        if n==2:
            return 1
        res =[]
        def go_left_or_right(m):
             left,right = m+1, m-1
             tem_res_l, tem_res_r = [], []
             while left%2==0 and left >0:
                 tem_res_l.append(left)
                 left/=2
             while right%2 ==0 and right >0:
                 tem_res_r.append(right)
                 right/=2
             print tem_res_r, tem_res_l
             if tem_res_r[-1]<=tem_res_l[-1]:
                 return right, tem_res_r
             else: 
                 return left, tem_res_l
        while n!=1:
            res.append(n)
            if n%2==0:
                n=n/2
            else:
                n, tem = go_left_or_right(n)
                res+=tem
        return len(res)-1 if res[-1]==1 else len(res)

a=Solution()
                
print a.integerReplacement(3)
print a.integerReplacement(7)
print a.integerReplacement(10)
print a.integerReplacement(21)
               

