class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class BinarySearchTree:

    def __init__(self):
        self.root=None
    
    def second_max(self):

            # base case
        if not self.root:
            return None
        current=self.root
        max=self.root.value
        max_values=[]
        while current:
            if current.value>max:
                max=current.value 
                max_values.append(max) 
            if current.right:
                current=current.right
            elif current.left:
                current=current.left
        length=len(max_values)
        return max_values[length-2]

if __name__ == "__main__":
    bt=BinarySearchTree()
    bt.root = Node(1)  
    bt.root.left = Node(2)  
    bt.root.right = Node(3)  
    bt.root.left.left = Node(4)  
    bt.root.left.right = Node(5)



    print(second_max())
