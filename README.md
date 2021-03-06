# python_coding


# 1. itertools.combinations(a, i)
```python
>>> import itertools
>>> a = [1,2,3,4]
>>> for element in itertools.combinations(a,3):
...     print element
... 
(1, 2, 3)
(1, 2, 4)
(1, 3, 4)
(2, 3, 4)
>>> 
```
# 2. zip(*grid)

```python
>>> grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
>>> zip(*grid)
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
>>> grid + zip(*grid)
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], (1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
>>> grid + map(list, zip(*grid))
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

```

# 3. is convex?
```python
class Solution(object):
    def isConvex(self, points):
        neg, pos = False,False
        N = len(points)
        def cross_product(a,b,c):
            x_ab,y_ab = a[0]-b[0],a[1]-b[1]
            x_bc,y_bc = b[0]-c[0],b[1]-c[1]
            return (x_ab * y_bc - y_ab * x_bc)
        points +=points[0:2]
        for i in xrange(N):
            if cross_product(points[i],points[i+1],points[i+2]) >0: neg=True
            if cross_product(points[i],points[i+1],points[i+2]) <0: pos=True
        return False if neg and pos else True
```
# 4. itertools.product():
```python
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        db = collections.defaultdict(list)
        for allow in allowed:
            db[allow[:2]] += [allow[-1]]
        memo = {}
        def dfs(bottom):
            if bottom not in memo:
                if len(bottom)==2 and bottom in db:
                    memo[bottom] = True
                    return True
                candidates = []
                for i in range(len(bottom)-1):
                    if bottom[i:i+2] not in db:
                        memo[bottom] = False
                        return False
                    candidates.append(db[bottom[i:i+2]])
                for candid in itertools.product(*candidates):
                    if dfs(''.join(candid)):
                        memo[bottom] = True
                        return True
                memo[bottom] = False
            return memo[bottom]
        return dfs(bottom)

```
```python
>>> import itertools
>>> a = [[1,2,3],[4,5,6]]
>>> for _ in itertools.product(*a):
...     print _, type(_)
... 
(1, 4) <type 'tuple'>
(1, 5) <type 'tuple'>
(1, 6) <type 'tuple'>
(2, 4) <type 'tuple'>
(2, 5) <type 'tuple'>
(2, 6) <type 'tuple'>
(3, 4) <type 'tuple'>
(3, 5) <type 'tuple'>
(3, 6) <type 'tuple'>
>>> 
```


# 5.collections.defaultdict(lambda: collections.defaultdict(list)) 

```python
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        f = collections.defaultdict(lambda: collections.defaultdict(list))
        for a, b, c in allowed: f[a][b].append(c)
            
        def pyramid(bottom):
            if len(bottom) == 1:
                return True
            for i in itertools.product(*(f[a][b] for a, b in zip(bottom, bottom[1:]))):
                if pyramid(i):
                    return True
            return False
        return pyramid(bottom)
```

```python
def pyramid(bottom):
            return len(bottom) == 1 or any(pyramid(i) for i in product(*(f[a][b] for a, b in zip(bottom, bottom[1:]))))
```

```python
>>> import collections
>>> allowed = ["ABC","BCD","CDE"]
>>> f = collections.defaultdict(lambda: collections.defaultdict(list))
>>> for a, b, c in allowed: f[a][b].append(c)
... 
>>> f
defaultdict(<function <lambda> at 0x101d25c08>, {'A': defaultdict(<type 'list'>, {'B': ['C']}), 'C': defaultdict(<type 'list'>, {'D': ['E']}), 'B': defaultdict(<type 'list'>, {'C': ['D']})})
>>> f['A']
defaultdict(<type 'list'>, {'B': ['C']})
>>> f['A']['B']
['C']
>>> type(f)
<type 'collections.defaultdict'>
>>> type(f['A'])
<type 'collections.defaultdict'>
>>> type(f['A']['B'])
<type 'list'>
>>> 
```

# 6. Collections.Counter

```python
>>> from collections import Counter
>>> counter = Counter('hellooo i am a potato!!!!!')
>>> counter.most_common(2)
[('o', 5), ('!', 5)]
```


# 7 time complexity

https://wiki.python.org/moin/TimeComplexity
https://stackoverflow.com/questions/27073596/what-is-the-cost-complexity-of-insert-in-list-at-some-locations = 'pining for the fjords'

# 8 sort by begin or sort by end of two intervals


```python
#1) sort by end:  after sorting we know: s1<e1<e2   and s2<e2
#(in order to make it be easier, we do not consider about "="). 
#Then s2 has three possible positions. I am giving those three possibilities by "@". :     @s1@e1@e2 
#Then we have 3 cases.
       #case 1: s2<s1<e1  @<e2 (replace the first "@"by s2 and remove the rest "@")   
                         #s1****e1
         #s2*****************************e2


        #case 2:s1<s2<e1 <e2 
         #s1*****************e1
                      #s2*******************e2
        

       #case 3:s1<e1< s2 <e2 
        #s1************e1
                                     #s2**************e2
       
#2) sort by start(similar as sort by end):   s1@s2@e2@
        #case1:    s1 <e1 <s2< e2
         #s1******e1
                                     #s2************e2


        #case2:    s1<s2<e1<e2
         #s1***************e1
                     #s2**********************e2


        #case3:s1<s2<e2<e1
          #s1************************************e1
                          #s2********e2

```

# 9 relative location info of two intervals:
s1<e1, s2<e2:
all conbination is 4! = 4*3*2=24
24/4 = 6 which are:

s1 e1 s2 e2
s1 s2 e1 e2
s2 s1 e1 e2
s2 e2 s1 e1


up long , down short
1.
----------
        ----

_________
