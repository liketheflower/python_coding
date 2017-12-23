class TreeNode(object):
    def __init__(self,x):
        self.name = x
        self.parent = None
        self.child = []
        self.val = 1.0
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        equ_val = zip(equations, values)
        root = TreeNode('root')
        dict_ =set((root.name,))
        nodes = {'root':root}
        for equation, value in equ_val:
            if equation[0] not in dict_:
                dict_.add(equation[0])
                a = TreeNode(equation[0])
                a.parent = root
                root.child.append(a)
                if equation[0]!=equation[1]:
                    dict_.add(equation[1])
                    b  = TreeNode(equation[1])
                    b.parent = a
                    b.val = value
                    nodes[b.name] = b
                    a.child.append(b)
                    nodes[a.name] = a
            else:
                if equation[0]!=equation[1]:
                    dict_.add(equation[1])
                    tem_node  = TreeNode(equation[1])
                    tem_node.parent = nodes[equation[0]]
                    nodes[equation[0]].child.append(tem_node)
                    tem_node.val = value
                    nodes[equation[1]] = tem_node
        res = []
        for query in queries:
            if query[0] not in dict_ or query[1] not in dict_:
               res.append(-1.0)
               continue
            elif query[0]==query[1]:
               res.append(1.0)
               continue 
            else:
                tem_ = 1.0
                tem_*=nodes[query[1]].val
                print tem_
                parent_node = nodes[query[1]].parent
                while True:
                    if parent_node == root:
                        tem_ = 1.0
                        query = query[::-1]
                        tem_ =1.0
                        tem_*=nodes[query[1]].val
                        parent_node = nodes[query[1]].parent
                        while True:
                            #tem_*=parent_node.val
                            if parent_node == root:
                                res.append(-1.0)
                                break
                            if parent_node == nodes[query[0]]:
                                if tem_ != 0:
                                    res.append(1.0/tem_)
                                    break
                                else:
                                    res.append(-1.0)
                                    break
                            tem_*=parent_node.val
                            parent_node = parent_node.parent

                        break
                    if parent_node == nodes[query[0]]:
                        print 'tem___', tem_
                        res.append(tem_)
                        break
                    tem_*=parent_node.val
                    parent_node = parent_node.parent
        return res



equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
#queries = [ ["b", "c"] ]
#equations = [ ["a","b"],["b","c"] ]
#values = [2.0,3.0]
#queries = [ ["a","c"],["b","c"],["a","e"],["a","a"],["x","x"] ]
equations = [["a","b"],["b","c"],["bc","cd"]]
values = [1.5,2.5,5.0]
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
a= Solution()
print a.calcEquation(equations, values, queries[1:2])

               
