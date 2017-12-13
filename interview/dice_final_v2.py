#globres = [0 for x in range(1000)]
#globres[0] =35000
def memoize(f):
    memo = {}
#    print x
    print memo
    def helper(x):
       # print "inner memo", memo
        if x not in memo:
            memo[x]=f(x)
	return memo[x]
    return helper
@memoize   	
def die_game_fair_value(rolls):
    #global globres
    die_ = [1,2,3,4,5,6]
    p_current_round=[]
    p_each_round = []
    win_strategy=[]
    res=0.0
    #if globres[rolls-1]>0:
     #   return globres[rolls-1]
    if rolls == 1:
        return int(10000*sum(die_)/6.0)
    else:
        for i in range(rolls-1):
            die_win = [x for x in die_ if x>= die_game_fair_value(rolls-i-1)/10000.0]
             #print die_win
            win_strategy.append(die_win)
            if die_win:
                 p_current_round.append(len(die_win)/6.0)
            else:
                 p_current_round.append(0.0)
            if i==0:
                 p_each_round.append(p_current_round[-1]) 
            else:
                 p=1.0
                 for j in range(i):
                     p=p*(1-p_current_round[j])
                 p_each_round.append(p*p_current_round[-1])
            if die_win:
                 res+=p_each_round[i]*sum(die_win)/float(len(die_win))
                 
        res+=(1-sum(p_each_round))*3.50
        res = int(10000*res)
       # if rolls<=1000:
        #    globres[rolls-1]=res
        return  res


if __name__=="__main__":
    n= int(input("please input a positive integer:"))
    #die_game_fair_value = memoize(die_game_fair_value)
    print die_game_fair_value(n)
