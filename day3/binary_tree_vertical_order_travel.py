import collections

class TreeNode(object):
    def __init__(self,x):
        print "I am here"
        self.value = x
        self.left = None
        self.right =None

class Solution(object):
    def __init__(self):
        print "I am a cool programmer!"
    def vertical_order(self, root):
        """
        :type root: TreeNode
        :rtype:List[List(int)]
        """
        cols = collections.defaultdict(list)
        queue = [(root, 0)]
        for node, i in queue:
           if node:
               cols[i].append(node.value)
               queue  += (node.left, i-1), (node.right, i + 1)
        return [cols[i] for i in sorted(cols)]

def build_tree(list_):
    if not list_:
       print "list is empty"
    a = TreeNode(list_[0])
    if not list_[1:]:
       return a
    open_list =[a]
    for i in range(0,len(list_)-1):
       if list_[i+1] == None:
           continue
       if i%2==0:
           left_node = TreeNode(list_[i+1])
           open_list[i/2].left = left_node
           open_list.append(left_node)
       else:
           right_node = TreeNode(list_[i+1])
           open_list[i/2].right = right_node
           open_list.append(right_node)

    return a

a = Solution()
list_ = [3,9,8,4,0,1,7]
list_ = [3,9,8,4,0,1,7,None,None,None,2,5]
root = build_tree(list_)
print root.value
print "left and right"
print root.left.value, root.right.value
print root.value, root.left, root.right
print a.vertical_order(root)
