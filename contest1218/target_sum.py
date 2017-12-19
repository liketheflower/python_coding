from collections import defaultdict
def find_target_sums(nums, S):
    count = defaultdict(int)
    count[0] = 1
    for x in nums:
        step = defaultdict(int)
        for y in count:
            #print "count", count
            step[y + x] += count[y]
            print y,"+",x, step
 #       for y in count:
            step[y - x] += count[y]
            #print "count", count
            print y,'-',x, step
        count = step
        print "step", step
        print "count", count

    return count[S]

nums = [1,1,1]
print find_target_sums(nums, 1)
