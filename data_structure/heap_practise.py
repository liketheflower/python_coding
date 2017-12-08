
# heapify(), heappush() and heappop()
#Python code to demonstrate working of 
 
# importing "heapq" to implement heap queue
"""
import heapq

# initializing list
li = [5, 7, 9, 1, 3,1,2,4,5,8,7,7]
 
# using heapify to convert list into heap
heapq.heapify(li)
print "heapq",li
# printing created heap
print "The created heap is : ",
print (list(li))
 
# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)
 
# printing modified heap
print "The modified heap after push is : ",
print (list(li))
 
# using heappop() to pop smallest element
print "The popped and smallest element is : ",
print (heapq.heappop(li))

"""

import heapq

salary = [100,2,300,4,1,2,3,45,56,67]
print type(salary)
heapq.heapify(salary)
print type(salary)

