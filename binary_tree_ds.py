class treenode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return treenode.to_tuple(self.left),self.key,treenode.to_tuple(self.right)
    def __repr__(self):
        return "{}".format(self.to_tuple())

#tree_funtions
def tree_height(node):
    if node is None:
        return 0
    else:
        return 1+max(tree_height(node.left),tree_height(node.right))
def tree_size(node):
    if node is None:
        return 0
    else:
        return 1+tree_size(node.left)+tree_size(node.right)
def parse_tree(data):
    """
    :rtype: treenode
    """
    if isinstance(data,tuple) and len(data)==3:
        node=treenode(data[1])
        node.left=parse_tree((data[0]))
        node.right=parse_tree((data[2]))
    elif data is None:
        node=None
    else:
        node=treenode(data)
    return node
def display_tree(node,space="\t",level=0):
    if node is None:
        print(space*level+"#")
        return
    #if node is leaf node
    if node.left==None and node.right==None:
        print(space*level+str(node.key))
        return
    #if node has children
    display_tree(node.right,space,level+1)
    print(space*level+str(node.key))
    display_tree(node.left,space,level+1)
def traverse_in_order(node):
    if node is None:
        return []
    return (traverse_in_order(node.left)+[node.key]+traverse_in_order(node.right))
def traverse_pre_order(node):
    if node is None:
        return []
    return ([node.key]+traverse_in_order(node.left)+traverse_in_order(node.right))
def traverse_post_order(node):
    if node is None:
        return []
    return (traverse_in_order(node.left) + traverse_in_order(node.right)+[node.key])

input_tree1=((1,3,None),2,((None,3,4),5,(6,7,8)))
tree1=parse_tree(input_tree1)
print(tree1)

print(tree_height(tree1))
print(tree_size(tree1))
display_tree(tree1,"\t",0)
print(traverse_in_order(tree1))
print(traverse_pre_order(tree1))
print(traverse_post_order(tree1))
tree_tuple1=tree1.to_tuple()
print(tree_tuple1)
