def memoize(f):
    memo={}
    def helper(x):
      if x not in memo:
          memo[x]=f(x)
      return memo[x]
    return helper



class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, args):
        if args not in self.memo:
          self.memo[args]=self.fn(args)
        return self.memo[args]
  

@Memoize
def fib(n):
    if n==0:
       return 0
    if n==1:
       return 1
    return fib(n-1)+fib(n-2)
m=int(input("input an integer:"))
for i in range(m):
   print fib(i)
