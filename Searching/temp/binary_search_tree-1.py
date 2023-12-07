import utility
class Node:
    def __init__(self,data):
        self.l_child=None
        self.r_child=None
        self.data = data

# Generate binary search tree
def bin_search_tree_insert(root,node):
    if root is None or root.data == None:
        root=node
    else:
        if (root.data > node.data):
            root.l_child = bin_search_tree_insert(root.l_child, node)
        else:
            root.r_child = bin_search_tree_insert(root.r_child, node)
    return root

##########################################################################
##########################################################################

# Main
node_list = [9, 8, 12, 4, 2, 6, 11, 13, 1, 3, 5, 7, 10, 14]
r = Node(node_list[0])

for i in range(1, len(node_list)):
    bin_search_tree_insert(r, Node(node_list[i]))

utility.print_preOrder(r)
print()