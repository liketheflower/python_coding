
def do_it(trees):
    import collections
    a = collections.defaultdict(list)
    non_leaf = collections.defaultdict(int)
    for i in xrange(len(trees)):
        a[trees[i]].append(i+2)
        non_leaf[trees[i]] = 1

    for tr in a:
        tem_sum = 0
        for val in a[tr]:
            tem_sum += non_leaf[val]
        number_of_child_leaf = len(a[tr])-tem_sum
        if number_of_child_leaf <3: return "No"
    return "Yes"
    
n = int(raw_input())
trees = []
for i in range(n-1):
   trees.append(int(raw_input()))
print do_it(trees)
