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
