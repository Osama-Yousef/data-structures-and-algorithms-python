class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

class BinaryTree:

    def __init__(self):
        self.root=None

    def preorder(self): ## root left right 
        try :
            output=[]
            def _walk(node):
                if not node:
                    return
                output.append(node.value)
                _walk(node.left)
                _walk(node.right)
            _walk(self.root)
            return output 
        except ValueError:
            return ("there is something wrong")
    

    def postorder(self): ##  left right  root 
        try :
            output=[]
            def _walk(node):
                if not node:
                    return
                _walk(node.left)   
                _walk(node.right) 
                output.append(node.value)
                
                
            _walk(self.root)
            return output 
        except ValueError:
            return ("there is something wrong")
    
    def inorder(self): ##  left root right 
        try :
            output=[]
            def _walk(node):
                if not node:
                    return
                _walk(node.left)    
                output.append(node.value)
                
                _walk(node.right)
            _walk(self.root)
            return output 
        except ValueError:
            return ("there is something wrong")

class BinarySearchTree(BinaryTree):
    def add(self,value):
        if not self.root:
            self.root=Node(value)
        current=self.root
        while current:
            if value < current.value:  ## go to left
                if not current.left: ## if there is no lift so we will create a lift node then it will be current
                    current.left=Node(value)
                    break
                current=current.left ## go to  left of node if it has left node

            else:
                
                if not current.right: ## there is no right 
                    current.right=Node(value) ## create node and it will be current
                    break
                current=current.right

    def cont(self,value):
        curr = self.root
        if curr.value == value: ## check first for the root
            return True
        while curr: ## walk through all nodes below the root
            if value == curr.value: ## this is our condition
                return True
            elif value < curr.value: ## go to left 
                curr = curr.left
            elif value >curr.value: ## go to right 
                curr = curr.right
        return False
    
    
    def max_val(self):
        try:    
            """
            Pre-order: root >> left >> right
            """
            maxx = [self.root.value]
            def _walk(node):
                
                if not node:
                    return
                if node.value > maxx[0]:
                    maxx[0] = node.value
                _walk(node.left)
                _walk(node.right)
            _walk(self.root)
            return maxx[0]
        except ValueError as e:
            print(f"error : {e}")
    
    def breadth_first(self,root=None):
   
        try:
            temp_list = []
            results = []
            if not self.root:
                return 'empty tree'
            else:    
                if self.root:
                    temp_list.append(self.root)
                while temp_list:
                    current = temp_list.pop(0)
                    results.append(current.value)
                    if current.left:
                        temp_list.append(current.left)
                    if current.right:
                        temp_list.append(current.right)
            return results
        except:
            raise ValueError('something wrong')
    
    def rev_breadth_first(self,root=None):
        ## the idea is :changing  right > left & left >right  in the breadth first function 
                       ## then reverse the resulted list 

                       ## our sol : we did the lift and right idea , then we used insert to put 
                       ## each value in the front (at index 0) of the results array 
                       ## insert will do the reverseng process
    
        try:
            temp_list = []
            results = []
            if not self.root:
                return 'empty tree'
            else:    
                if self.root:
                    temp_list.append(self.root)
                while temp_list:
                    current = temp_list.pop(0)
                    results.insert(0,current.value) ## we did insert instead of append
                    if current.right:  ## we put right here
                        temp_list.append(current.right)
                    if current.left: ## we put left here
                        temp_list.append(current.left)
                
            return results
        except:
            raise ValueError('something wrong')
    
    def breadth_first_rev_2(self,root=None):
        ## other solution 
        ## we change right and left 
        ## then before ending function we added some lines to reverse the results list 
        ## and return the reversed list that we want 
        try:
            temp_list = []
            results = []
            if not self.root:
                return 'empty tree'
            else:    
                if self.root:
                    temp_list.append(self.root)
                while temp_list:
                    current = temp_list.pop(0)
                    results.append(current.value)
                    if current.right: ## put right here
                        temp_list.append(current.right)
                    if current.left: ### put left here
                        temp_list.append(current.left)
                ## before finishing the function 
                ## we added these lines to reverse the results array then return the reversed list (required)
                length=len(results)
                solution=[None]*length
                for item in results :
                    length=length-1
                    solution[length]=item
                return solution


        except:
            raise ValueError('something wrong')
    
    def fizzbuzz(self): ## this is my solution depending on preorder function
                        ### i checked for each node value , and uesd some conditions 
                        ## if node achieves ine condition then it will be added to array with new value

                        ## Note : when i have some if conditions below each other , if one if achieves so the other if will not be done and will go directly to else , so i did the function like this to do the idea correctly 
                        
                        ## i have other idea is that after i did the preorder function and got an array
                        ## then i will add new array and do a loop to walk through the old array 
                        ## and checks dependng on the conditions , then if it achieves any condition
                        ## value will be changed and  added to new array 
                        ## keep doing that .... , then return the new array 
        try :
            output=[]
            def _walk(node):
                if not node:
                    return

                elif node.value %3==0 or node.value %5==0:

                    if node.value %3==0 and node.value %5==0:
                        node.value='fizzbuzz'
                    elif node.value %3==0:
                        node.value='fizz'
                    elif node.value %5==0:
                        node.value='buzz'
                    
                else:
                    node.value=node.value
                output.append(node.value)
                _walk(node.left)
                _walk(node.right)
            _walk(self.root)
            return output 
        except ValueError:
            return ("there is something wrong")



    def sum_numbers(self): ## this function will return the sum of all values in binary tree
                           ## thiis is my solution
                           ## my idea is to use preorder function to get array of all values in tree
                           ## make sum = 0
                           ## do a loop walk through the array and add each value to sum then return sum
        try :
            output=[]
            def _walk(node):
                if not node:
                    return
                output.append(node.value)
                _walk(node.left)
                _walk(node.right)
            _walk(self.root)



            sum=0
            for item in output:
                sum +=item
            return sum

        except ValueError:
            return ("there is something wrong")


    
    def sum_numbers_2(self): ## this is my second solution depending on pre order function and added some edits
        try :
            
            sum=[0]
            def _walk(node):
                if not node:
                    return
                sum[0]+=node.value
                _walk(node.left)
                _walk(node.right)
            _walk(self.root)

            return sum[0]

        except ValueError:
            return ("there is something wrong")
## شششششششششششششغغغغغغغغغغغغغاااااااااااااااال
# def common(tree1,tree2): ## this is my solution
#                      ## idea : apply oreorder function for tree 1 and get tree 1 values 
#                      ## then apply preorder fun for tree 2 to walk through each value in tree 2 
#                      ## instead of append in tree 2 ,i added a condition to check if each value in tree 2 is exist in tree 1 values array
#                      ## if it is not exist --keep going 
#                      ## if it exists then i made a new array and append this value to it
#                      ## return rhe new array which have common values in both trees  
        
#         tree1_values=[]
#         common_values=[]
#         def _walk_tree_1(node):
#             if not node:
#                 return
#             tree1_values.append(node.value)
#             _walk_tree_1(node.left)
#             _walk_tree_1(node.right)
#         _walk_tree_1(tree1.root)
        

        
#         def _walk_tree_2(node):
#             if not node:
#                 return
#             if node.value in tree1_values:
#                 common_values.append(node.value)
#             _walk_tree_2(node.left)
#             _walk_tree_2(node.right)
#         _walk_tree_2(tree2.root)
#         return common_values
    ## مششششششش ششششششغغغغغغاااااااااال
# def merge(tree1,tree2,root=None):
   
#         try:
#             temp_list = []
#             results = []
#             if not tree1.root :
#                 return 'there is empty tree'
#             if not tree2.root :
#                 return 'there is empty tree'
#             else:    
#                 if tree1.root and tree2.root:
#                     temp_list.append(tree1.root)
#                     temp_list.append(tree2.root)

#                 while temp_list:
#                     current1 = temp_list.pop(0)
#                     current2= temp_list.pop(0)
#                     results.append(current1.value + current2.value)
#                     if current1.left:
#                         temp_list.append(current1.left)
#                     if current2.left:
#                         temp_list.append(current2.left)
#                         if not current2.left:
#                             node=Node(0)
#                             temp_list.append(node)
#                     elif current1.right:
#                         temp_list.append(current1.right)
                    
#                         if not current1.right:
#                             node=Node(0)
#                             temp_list.append(node)
                    
#                     elif current2.right:
#                         temp_list.append(current2.right)
#             return results
#         except:
#             raise ValueError('something wrong')

    #######################################################################
    ### using recursion and it needs inorder method ####################333
    # def MergeTrees(tree1, tree2):
    #     if tree1 is None:   ## if no tree 1 so merging will be just tree2 
    #         return tree2
    #     if tree2 is None:  ## if no tree 2 , merging two trees will be jus tree 1
    #         return tree1
    #     tree1.value += tree2.value
    #     tree1.left = MergeTrees(tree1.left, tree2.left)
    #     tree1.right = MergeTrees(tree1.right, tree2.right)
    #     return tree1

    # def inorder(node): 
    #     if (not node): 
    #         return
    
    #     # first recur on left child  
    #     inorder(node.left)  
    
    #     # then print the data of node  
    #     print(node.value, end = " ")  
    
    #     # now recur on right child  
    #     inorder(node.right) 


        #######################################################################################################3
      #####################################################################################################



    def Height(self): ## this function calculate the num of levels in the tree
      
        # Base Case 
        if self.root is None: 
            return 0
        
        q = [] ## to store the nodes 
        
        q.append(self.root) 
        height = 0 ## in the beginning
    
        while(True): 
            
            nodeCount = len(q) ## its # of nodes in same level
            if nodeCount == 0 : ## no nodes in the same level so we are done
                return height  
        
            height += 1 ## coz in first level we have the root so we increae the height by 1 then enter the 
                        ## loop for noodes below the root 
    
            # remove all nodes of current level and adding all nodes of next level in the q in each iteration
            while(nodeCount > 0): ## this mean that there is node in same level
                node = q[0] 
                q.pop(0) 
                if node.left : 
                    q.append(node.left) 
                if node.right: 
                    q.append(node.right) 
    
                nodeCount -= 1 ## we decrease it by one coz we popped from q
                ## the idea in this loop : 
                ## the first iteration we take the nodes in the left of tree 
                ## the second iteration we take the nodes in right of tree in the same level 
                ## then when we will start a new level it exit from this loop

#######################################################################################################33
######################################################################################################3

# def mirror(root): ## make a function that convert a tree to mirrored one 
#                    ## idea is : the root eill be the same 
#                    ## then each sub tree i will swap children(right become left and left become right)
#                    ## now you got the mirrored one
  
#         if (root == None): 
#             return
    
#         q = [] 
#         q.append(root) 
    
#         while (len(q)): 
    
#             curr = q[0] 
#             q.pop(0) 
    
#             # swap left child with right child 
#             curr.left, curr.right = curr.right, curr.left 
    
#             # append left and right children 
#             if (curr.left): 
#                 q.append(curr.left) 
#             if (curr.right): 
#                 q.append(curr.right)
# """ Helper function to print Inorder traversal.""" ## we did this coz mirror function will just do the mission
#                        ## so we need method to print this , we used inorder for ex 
#                        ## it takes node , so it will take root and all the tree then traverse to print it 
# def inOrder( node): 
#     if (node == None): 
#         return
#     inOrder(node.left) 
#     print(node.value, end = " ") 
#     inOrder(node.right)  

####################################################################################################3
####################################################################################################333

# def swapEveryKLevelUtil(root, level, k): 
#       
#     if (root is None or (root.left is None and root.right is None )): 
#         return 
#   
# # If current level+1 is present in swap vector 
# # then we swap left and right node 
#     if (level+1)%k == 0: 
#         root.left, root.right = root.right, root.left 
#       
#     # Recur for left and right subtree 
#     swapEveryKLevelUtil(root.left, level+1, k) 
#     swapEveryKLevelUtil(root.right, level+1, k) 
#   
#       
# # This function mainly calls recursive function 
# # swapEveryKLevelUtil 
# def swapEveryKLevel(root, k): 
#       
#     # Call swapEveryKLevelUtil function with  
#     # initial level as 1 
#     swapEveryKLevelUtil(root, 1, k) 

# # Method to find the inorder tree travesal 
# def inorder(root): 
#       
#     # Base Case 
#     if root is None: 
#         return 
#     inorder(root.left) 
#     print root.data,  
#     inorder(root.right) 
#   




if __name__ == "__main__":
    # bt = BinarySearchTree()
    # bt.root = Node(8)
    # bt.root.left = Node(3)
    # bt.root.right = Node(10)
    # bt.root.right.right = Node(14)
    # bt.root.right.right.left = Node(13)


    # bt.root.left.left = Node(1)
    # bt.root.left.right = Node(6)
    # bt.root.left.right.left = Node(4)
    # bt.root.left.right.right= Node(7)

    # print(bt.inorder())
    # print(bt.postorder())
    # print(bt.preorder())
    # bt.add(15)
    # print(bt.cont(15))
    # print(bt.max_val())
    # print(bt.breadth_first_rev_2())

    # ## check for fizzbuzz 

    # bt = BinarySearchTree()
    # bt.root = Node(5) ## should give buzz
    # bt.root.left = Node(3) ## should give fizz
    # bt.root.right = Node(6) ## should give fizz
    # bt.root.right.right=Node(15) ## should give fizzbuzz
    # bt.root.left.right=Node(4) ## should give 4
    # print(bt.fizzbuzz())


    # # ## check for common 
    # tree1 = BinarySearchTree()
    # tree1.root = Node(8)
    # tree1.root.left = Node(6)
    # tree1.root.right = Node(10)
    # tree1.root.right.left = Node(9)

    # tree1.root.left.left = Node(4)
    # tree1.root.left.right = Node(7)
  
    # tree2 = BinarySearchTree()
    # tree2.root = Node(6)
    # tree2.root.left = Node(4)
    # tree2.root.right = Node(8)
    # tree2.root.right.right = Node(10)

    # tree2.root.left.right = Node(5)
  

    # # print(common(tree1,tree2))

    # ## check for merge
   
    # root1 = Node(1)  
    # root1.left = Node(2)  
    # root1.right = Node(3)  
    # root1.left.left = Node(4)  
    # root1.left.right = Node(5)  
    # root1.right.right = Node(6)  
  
   
    # root2 = Node(4)  
    # root2.left = Node(1)  
    # root2.right = Node(7)  
    # root2.left.left = Node(3)  
    # root2.right.left = Node(2)  
    # root2.right.right = Node(6)  
  
    # root3 = MergeTrees(root1, root2)  
    # print(root3) ## will return node object 
    # print(inorder(root3)) ## we did this to print it as array or values next to each other

##################################################3333
    # ## check for the height method 
    # bt = BinarySearchTree()
    # bt.root = Node(1)
    # bt.root.left = Node(3)
    # bt.root.right = Node(4)
    # bt.root.right.right = Node(5)
    # bt.root.left.left = Node(6)
    # bt.root.left.left.left = Node(7)

    
    # print(bt.Height())

# ########################################################33
# ########### For mirror method ####################
# ####################################################3
#     root = Node(1)  
#     root.left = Node(2)  
#     root.right = Node(3)  
#     root.left.left = Node(4)  
#     root.left.right = Node(5)

#     inOrder(root)  ## will do in order traversal just
  
#     """ Convert tree to its mirror """
#     mirror(root)  
  
#     """ Print inorder traversal of the mirror tree """
#     print("\nInorder traversal of the mirror tree is")  
#     inOrder(root)  

##########################################################################3
#########################################################################
    # ## check for swappin in kth level
    # """ 
    #           1 
    #         /   \ 
    #        2     3 
    #      /      /  \ 
    #     4      7    8  
    # """
    # root = Node(1) 
    # root.left = Node(2) 
    # root.right = Node(3) 
    # root.left.left = Node(4) 
    # root.right.right = Node(8) 
    # root.right.left = Node(7) 
    #   
    # k = 2 
    # print "Before swap node :" 
    # inorder(root) 
    #   
    # swapEveryKLevel(root, k) 
    #   
    # print "\nAfter swap Node : "
    # inorder(root) 

    ###################################################################################
    ##################################################################################3

    