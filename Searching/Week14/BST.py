import utillity
class Node:
    def __init__(self, data):
        self.l_child = None
        self.r_child = None
        self.data = data

def bin_search_tree_insert(root, node):
    if (root is None):
        root = node
    else:
        if (root.data > node.data):
            root.l_child = bin_search_tree_insert(root.l_child, node)
        else:
            root.r_child = bin_search_tree_insert(root.r_child, node)
    return root

def find_min(node):
    current = node
    while (current.l_child):
        current = current.l_child
    return current

def bin_search_tree_delete(root, node):
    if (root is None):
        return root

    if (node.data < root.data):
        root.l_child = bin_search_tree_delete(root.l_child, node)
    elif (node.data > root.data):
        root.r_child = bin_search_tree_delete(root.r_child, node)
    else:
        if root.l_child is None:
            return root.r_child
        elif root.r_child is None:
            return root.l_child

        root.data = find_min(root.r_child).data

        root.r_child = bin_search_tree_delete(root.r_child, Node(root.data))

    return root

if __name__ == "__main__":
    r = Node(7)
    bin_search_tree_insert(r, Node(9))
    bin_search_tree_insert(r, Node(1))        
    bin_search_tree_insert(r, Node(3))        
    bin_search_tree_insert(r, Node(12))

    bin_search_tree_delete(r, Node(9))

    utillity.print_inOrder(r)
    print()
    utillity.print_preOrder(r)
