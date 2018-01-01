ii = 0
def find_max_value(inte, pages, p):
    global ii
    ii+=1
    print "inte", inte, ii
    if not inte or p<=0:
        return 0
    if 2*sum(pages)<=p:
        return sum(inte)
    if len(inte)==1:
        if p>=2*pages[0]:
            return inte[0]
        else:
            return 0
    return max(inte[0]+find_max_value(inte[1:],pages[1:],p-2*pages[0]),find_max_value(inte[1:],pages[1:] ,p)) if p-2*pages[0]>=0 else find_max_value(inte[1:],pages[1:] ,p)
#test 1:
inte = [1,4,2,5,3,100,20,34,5,2,199,30,40,200,400]
pages = [2,6,4,7,1,2,4,5,6,7,8,1,2,3,4]
combine =zip(inte,pages)
combine.sort(key=lambda x:x[1],reverse = True)
print combine
inte = [element[0] for element in combine]
pages = [element[1] for element in combine]

p=50
print find_max_value(inte, pages, p)
"""
#test 1:
inte = [3,2,2]
pages = [3,2,2]
p=9
print find_max_value(inte, pages, p)
"""



