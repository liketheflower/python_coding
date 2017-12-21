#definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def get_sum(node):
            if node not in mem:
                if not node:
                    mem[node] = 0
                    return mem[node]
                if not (node.left or node.right):
                    mem[node] = node.val
                    return mem[node]
                else:
                    mem[node] = node.val+get_sum(node.left) + get_sum(node.right)
                    return mem[node]
            return mem[node]
        mem = {}
        return get_sum(root)
