class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        db = [[0 for i in range(n)] for j in range(k**n)]
        for j in range(k**n):
            a = j
            for i in range(n):
                a,db[j][-(i+1)] = a//k,a%k 
        print 'db', db
        res=[0 for _ in range(n)]
        close =[[0 for _ in range(n)]]
        while len(close)<k**n:
            for kk in range(k):
               tem = res[-n:]+[kk]
               tem = tem[1:]
               print 'tem', tem
               if tem not in close:
                  res.append(kk)
                  close.append(tem)
                  break
                  print 'close',close
               if kk==k-1:
                  res.append(0)
        print 'res',res
        return res 
        




a=Solution()
print a.crackSafe(2,2)
