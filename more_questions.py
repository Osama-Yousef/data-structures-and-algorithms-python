"""Iterative function to check if two trees are identical(the same) """
"""
def isIdentical(x, y):

	# if both trees are empty, return true
	if x is None and y is None:
		return True

	# if first tree is empty (& second tree is non-empty), return false
	if x is None:
		return False

	# if second tree is empty (& first tree is non-empty), return false
	if y is None:
		return False

	# create a stack to hold pairs
	stack = deque()
	stack.append((x, y))

	# loop till stack is empty
	while stack:
		# pop top pair from the stack and process it
		x, y = stack.pop()

		# if value of their root node don't match, return false
		if x.key != y.key:
			return False

		# if left subtree of both x and y exists, push their addresses
		# to stack else return false if only one left child exists
		if x.left and y.left:
			stack.append((x.left, y.left))
		elif x.left or y.left:
			return False

		# if right subtree of both x and y exists, push their addresses
		# to stack else return false if only one right child exists
		if x.right and y.right:
			stack.append((x.right, y.right))
		elif x.right or y.right:
			return False

	# if we reach here, both binary trees are identical
	return True

    ## time : O(1)
"""
#######################################################################################################33
######################################################################################################33
"""
Determine if given binary tree is a subtree of another binary tree or not"""

"""
# Function to store in-order traversal of the tree in a list
def inorder(node, list):
	if node is None:
		return

	inorder(node.left, list)
	list.append(node)
	inorder(node.right, list)


# Function to store post-order traversal of the tree in a list
def postorder(node, list):
	if node is None:
		return

	postorder(node.left, list)
	postorder(node.right, list)
	list.append(node)


# Utility function to convert the list to a string and remove opening & 
# closing Brackets from it
def toString(s):
	return str(s).replace("[", "").replace("]", "")


# Function to check if given binary tree is a subtree of another
# binary tree or not
def checkSubtree(tree, subtree):

	# base case: both trees are same
	if tree == subtree:
		return True

	# base case: if first tree is empty but second tree is non-empty
	if tree is None:
		return False

	# store in-order traversal of both trees in first and second respectively
	first = []
	second = []

	inorder(tree, first)
	inorder(subtree, second)

	# return false if second list is not a sub-list of first list
	if toString(first).find(toString(second)) == -1:
		return False

	# reset both lists
	first.clear()
	second.clear()

	# Now store post-order traversal of both trees in first and second respectively
	postorder(tree, first)
	postorder(subtree, second)

	# return false if second list is not a sub-list of first list
	if toString(first).find(toString(second)) == -1:
		return False

	return True

Time :
"""
""" otherrrrrrrrrrrrrrrrrrrrrr solllllllllllllllutionnnnnnnnnnnnnnnnnnnnnnn""""
"""

Algorithm:

Declare a stack, to keep track of left and right child of the nodes.
Push the root node of the tree T.
Run a loop while the stack is not empty and then check that if the 
pre-order traversal of the top node of the stack is the same, then return true.
If the pre-order traversal does not match with the tree then pop the top node from 
the stack and push its left and right child of the popped node.




"""
""" Lowest Common Ancestor in a Binary Tree"""
"""
# Finds the path from root node to given root of the tree. 
# Stores the path in a list path[], returns true if path  
# exists otherwise false 
def findPath( root, path, k): 
  
    # Baes Case 
    if root is None: 
        return False
  
    # Store this node is path vector. The node will be 
    # removed if not in path from root to k 
    path.append(root.key) 
  
    # See if the k is same as root's key 
    if root.key == k : 
        return True
  
    # Check if k is found in left or right sub-tree 
    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right!= None and findPath(root.right, path, k))): 
        return True 
  
    # If not present in subtree rooted with root, remove 
    # root from path and return False 
       
    path.pop() 
    return False
  
# Returns LCA if node n1 , n2 are present in the given 
# binary tre otherwise return -1 
def findLCA(root, n1, n2): 
  
    # To store paths to n1 and n2 fromthe root 
    path1 = [] 
    path2 = [] 
  
    # Find paths from root to n1 and root to n2. 
    # If either n1 or n2 is not present , return -1  
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)): 
        return -1 
  
    # Compare the paths to get the first different value 
    i = 0 
    while(i < len(path1) and i < len(path2)): 
        if path1[i] != path2[i]: 
            break
        i += 1
    return path1[i-1] 

    Time : O(n). The tree is traversed twice, and then path arrays are compared.
"""

#################################################################################################
#################################################################################################
""" print-all-paths-from-root-to-leaf-nodes-binary-tree"""

"""
### recursive method
def printRootToLeafPathIterative(root):

    # create an empty stack to store a pair of tree node and
    # its path from the root node
    stack = deque()

    # push root node
    stack.append((root, ""))

    # loop till stack is empty
    while stack:

        # we pop a node from the stack and push the data to output stack
        curr, path = stack.pop()

        # add current node to the existing path
        path += (" -> " if path else "\n") + str(curr.data)

        # if leaf node, print the path
        if curr.left is None and curr.right is None:
            print(path, end='')

        # push left and right child of popped node to the stack
        if curr.right:
            stack.append((curr.right, path))

        if curr.left:
            stack.append((curr.left, path))
"""
#####################################################################################################3
#####################################################################################################
"""Convert given binary tree to full tree by removing half nodes """

"""
# Function to perform inorder traversal of the tree
def inorder(root):

    if root is None:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)


# Function to check if given node is a leaf node or not
def isLeaf(node):
    return node.left is None and node.right is None


# Function to convert a binary tree to full tree by removing half nodes
# i.e. remove nodes having one children
def truncate(root):

    # base case: empty tree
    if root is None:
        return None

    # recursively truncate the left subtree and subtree first
    root.left = truncate(root.left)
    root.right = truncate(root.right)

    # if current node has two children or it is leaf node,
    # not hing needs to be done
    if (root.left and root.right) or isLeaf(root):
        return root

    # if current node has exactly one child, then delete it and replace
    # the node by the child node
    child = root.left if root.left else root.right
    return child


"""
""" other solutionnnnnnnnnnnnnnn"""
"""
# For inorder traversal 
def printInorder(root): 
    if root is not None: 
        printInorder(root.left) 
        print root.data, 
        printInorder(root.right) 
  
# Removes all nodes with only one child and returns 
# new root(note that root may change) 
def RemoveHalfNodes(root): 
    if root is None: 
        return None
  
    # Recur to left tree 
    root.left = RemoveHalfNodes(root.left) 
      
    # Recur to right tree 
    root.right = RemoveHalfNodes(root.right) 
      
    # if both left and right child is None  
    # the node is not a Half node 
    if root.left is None and root.right is None: 
        return root 
  
    # If current nodes is a half node with left child 
    # None then it's right child is returned and    
    # replaces it in the given tree 
    if root.left is None: 
        new_root = root.right  
        temp = root  
        root = None
        del(temp) 
        return new_root 
  
    if root.right is None: 
        new_root = root.left 
        temp = root 
        root = None
        del(temp) 
        return new_root 
      
    return root 
"""
####################################################################################################3
########################################################################################################
""" find-maximum-sum-root-to-leaf-path-binary-tree""" 

"""
# Function to print root-to-leaf path having given sum in a binary tree
def printPath(root, sum):

    # base case
    if sum == 0:
        return True

    # base case
    if root is None:
        return False

    # recur for left and right subtree with reduced sum
    left = printPath(root.left, sum - root.data)
    right = printPath(root.right, sum - root.data)

    # print current node if it lies on path having given sum
    if left or right:
        print(root.data, end=' ')

    return left or right


# Function to calculate maximum root-to-leaf sum in a binary tree
def rootToLeafSum(root):

    # base case: tree is empty
    if root is None:
        return 0

    # calculate maximum node-to-leaf sum for left child
    left = rootToLeafSum(root.left)

    # calculate maximum node-to-leaf sum for right child
    right = rootToLeafSum(root.right)

    # consider maximum sum child
    return (left if left > right else right) + root.data


# Function to print maximum sum root-to-leaf path in a given binary tree
def findMaxSumPath(root):

    sum = rootToLeafSum(root)
    print("Maximum sum is", sum)
    print("Maximum sum path is: ", end='')

    printPath(root, sum)


"""


##################################################################################################
##################################################################################################333
""" print right view of tree iteratively""" 

"""
# Iterative function to print right view of given binary tree
def rightView(root):

	# return if tree is empty
	if root is None:
		return

	# create an empty queue and enqueue root node
	queue = deque()
	queue.append(root)

	# loop till queue is empty
	while queue:

		# calculate number of nodes in current level
		size = len(queue)
		i = 0

		# process every node of current level and enqueue their
		# non-empty right and right child to queue
		while i < size:
			i = i + 1
			curr = queue.popleft()

			# if this is last node of current level, print it
			if i == size:
				print(curr.key, end=' ')

			if curr.left:
				queue.append(curr.left)

			if curr.right:
				queue.append(curr.right)

"""
###############################################################################################3333
############################################################################################3
""" print path to given node in tree"""

""" 
def hasPath(root, arr, x): 
      
    # if root is None there is no path  
    if (not root): 
        return False
      
    # push the node's value in 'arr'  
    arr.append(root.data)      
      
    # if it is the required node  
    # return true  
    if (root.data == x):      
        return True
      
    # else check whether the required node  
    # lies in the left subtree or right  
    # subtree of the current node  
    if (hasPath(root.left, arr, x) or 
        hasPath(root.right, arr, x)):  
        return True
      
    # required node does not lie either in  
    # the left or right subtree of the current  
    # node. Thus, remove current node's value   
    # from 'arr'and then return false      
    arr.pop(-1)  
    return False
  
# function to print the path from root to  
# the given node if the node lies in 
# the binary tree  
def printPath(root, x): 
      
    # vector to store the path  
    arr = []  
      
    # if required node 'x' is present  
    # then print the path  
    if (hasPath(root, arr, x)): 
        for i in range(len(arr) - 1): 
            print(arr[i], end = "->")  
        print(arr[len(arr) - 1]) 
      
    # 'x' is not present in the  
    # binary tree  
    else: 
        print("No Path") 
"""
##################################################################################################3
####################################################################################################
""" How to determine if a binary tree is height-balanced?""" 
"""

# function to find height of binary tree 
def height(root): 
      
    # base condition when binary tree is empty 
    if root is None: 
        return 0
    return max(height(root.left), height(root.right)) + 1
  
# function to check if tree is height-balanced or not 
def isBalanced(root): 
      
    # Base condition 
    if root is None: 
        return True
  
    # for left and right subtree height 
    lh = height(root.left) 
    rh = height(root.right) 
  
    # allowed values for (lh - rh) are 1, -1, 0 
    if (abs(lh - rh) <= 1) and isBalanced( 
    root.left) is True and isBalanced( root.right) is True: 
        return True
  
    # if we reach here means tree is not  
    # height-balanced tree 
    return False
"""