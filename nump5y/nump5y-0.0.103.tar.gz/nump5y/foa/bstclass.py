Ans='''"""

DESCRIPTION:
The binary search tree is implemented using a node class and methods to print and traverse through it are also defined.
a class method no_of_nodes() is implemented to return and print the no. of nodes in the BST . this function actually counts the length of the list of nodes formed using the treepaths function .

PROGRAM:
class node:
    """a node class with a constructor setting the node and left and
    right child to None by default"""
    def __init__(self, data):
        self.data = data
        self.right = self.left = None

    def insert(self, x):
        """insert hte new data in a node based on the value comparision with root
        if the root value is greater than new node then it is stored in left subtree
        and if the root is less than new value , the data is stored in right subtree"""
        if self.data:
            if self.data > x:
                if self.left is None:
                    self.left = node(x)
                else:
                    self.left.insert(x)
            elif self.data < x:
                if self.right is None:
                    self.right = node(x)
                else:
                    self.right.insert(x)
        else:
            self.data = x

    def print_tree(self):
        """printing of tree in inorder fashion"""
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def tree_values(self):
        """getting a list of all the nodes in the BST by calling the treevalues
        function ."""
        my_list = []
        return self.treevalues(my_list)

    def treevalues(self, my_list):
        if self.left:
            self.left.treevalues(my_list)
        my_list.append(self.data)
        if self.right:
            self.right.treevalues(my_list)

        return my_list

    def no_of_nodes(self):
        """calls the tree_values() function and gets its length"""
        print(len(self.tree_values()))

def main():
    root = node(5)
    root.insert(2)
    root.insert(6)
    root.insert(3)
    print("the tree is-->")
    root.print_tree()
    print("\n the no. of nodes-->")
    root.no_of_nodes()

if __name__=='__main__':
    main()


"""
'''
