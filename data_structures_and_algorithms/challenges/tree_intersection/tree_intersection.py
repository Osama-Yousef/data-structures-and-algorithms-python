def tree_intersection(left_tree, right_tree):
    '''Takes two binary trees, then returns the set of values that found in both trees.'''

    # Elements from each set
    union = set()
    # Elements exist in both sets 
    intersection = set()

    if left_tree.root == None or right_tree.root == None:
        return intersection

    def walk(node, union=union, intersection=intersection):
        '''
         updating respective sets as we go.
        '''
        if node.left:
            walk(node.left, union, intersection)
        if node.data in union:
            intersection.add(node.data)
        else:
            union.add(node.data)
        if node.right:
            walk(node.right, union, intersection)

    walk(left_tree.root)
    walk(right_tree.root)

    return intersection