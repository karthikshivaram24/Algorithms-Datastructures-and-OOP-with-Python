"""
This class represents a binary Search Tree and all the implementations of its inbuilt methods.
And a few Traversal technique's like inorder, pre-order, post-order and depth first traversals
and breadth first traversals( Level Order Traversals)
"""
class Node(object):
    """
    """
    def __init__(self,value):
        self.Left = None
        self.Right= None
        self.value = value

    """
    Need to override comparison method here for the Node object where we check it the
    object is an instance of this class and we check whether the value fields are the same or not

    ** IMPORTANT **
    """
    def __eq__(self,other):
        if isinstance(other,Node):
            return self.value == other.value


class BST(object):
    """
    """

    def __init__(self,root):
        self.root = root

    def search(self,Node):
        """
        """
        def recurseSearch(root,Node):
            """
            This base case of comparison works because we override the comparison operator for the Node class.
            """
            if root == Node:
                return True
            else:
                if root != None:
                    if root < Node:
                        return recurseSearch(root.Right,Node)
                    elif root > Node:
                        return recurseSearch(root.Left,Node)
                else:
                    return False

        return recurseSearch(self.root,Node)

    def addNode(self,newNode):
        """
        """
        if self.root == None:
            self.root = newNode
        else:
            curr = self.root
            while(curr != None):
                if newNode.value < curr.value:
                    if curr.Left == None:
                        curr.Left = newNode
                    else:
                        curr = curr.Left
                else:
                    if curr.Right == None:
                        curr.Right = newNode
                    else:
                        curr=curr.Right

    def recursiveAdd(self,newNode):
        """
        """

        def recurse(curr,NewNode):
            """
            """
            if curr<=NewNode:
                if curr.Right == None:
                    curr.Right = NewNode
                else:
                    recurse(curr.Right,newNode)
            else:
                if curr.Left == None:
                    curr.Left = NewNode
                else:
                    recurse(curr.Left,newNode)
        if self.root == None:
            self.root = NewNode
        else:
            recurse(self.root,newNode)

    def min(self,startNode):
        """
        """
        def recurseMin(root):
            """
            """
            if root.Left == None:
                return root
            else:
                return recurseMin(root.Left)

        return recurseMin(startNode)

    def iterMin(self,startNode):
        """
        """
        if startNode.Left == None:
            return startNode
        else:
            curr = startNode
            result = None
            while(curr != None):
                if curr.Left == None:
                    result = curr
                    break
                else:
                    curr = curr.Left
            return result

    def max(self,startNode):
        """
        """
        def recurseMax(root):
            if root.Right == None:
                return root.Right
            else:
                recurseMax(root.Right)

        return recurseMax(startNode)

    def recursiveTraversals(self,traversal_No):
        """
        """
        if traversal_No == 1:

            def recurseInorder(root):
                if root != None:
                    recurseInorder(root.Left)
                    print(root)
                    recurseInorder(root.Right)

            recurseInorder(self.root)

        elif traversal_No == 2:

            def recursePreOrder(root):
                if root != None:
                    print(root)
                    recursePreOrder(root.Left)
                    recursePreOrder(root.Right)

            recursePreOrder(self.root)

        else:

            def recursePostOrder(root):
                if root != None:
                    recursePostOrder(root.Left)
                    recursePostOrder(root.Right)
                    print(root)

            recursePostOrder(self.root)

    def iterInorder(self):
        """
        LEFT  - ROOT - RIGHT or LEFT - PARENT - RIGHT
        """

        if self.root == None:
            print("No elements Exist in the tree")
        else:
            result = []
            curr = root
            stack = []
            stack.append(curr)
            while(curr.Left != None):
                stack.append(curr)
                curr = curr.Left

            while(len(stack)>0):
                # Everytime i pop off an element off the stack i check if it has a right , if
                # it does have a right i need to traverse down its left's till i get null for both left and right and pop after that
                curr = stack.pop()
                result.append(curr)
                if curr.Right != None:
                    curr = curr.Right
                    stack.append(curr)
                    while(curr.Left != None):
                        curr = curr.Left
                        stack.append(curr)

            print(a for a in result)


    def iterPreOder(self):
        """
        ROOT - LEFT - RIGHT
        """

        if self.root == None:
            print("No elements Exist in the tree")
        else:
            result = []
            curr = self.root
            stack = []
            result.append(curr)
            stack.append(curr)

            while(len(stack)>0):
                if curr.Left != None:
                    curr = curr.Left
                    result.append(curr)
                    stack.append(curr)
                else:
                    curr = stack.pop()
                    if curr.Right != None:
                        curr = curr.Right
                        result.append(curr)
                        stack.append(curr)

            print(a for a in result)

    def iterPostOrder(self):
        """
        LEFT - RIGHT - ROOT
        """
        if self.root == None:
            print("No elements Exist in the tree")
        else:
            stack1 = []
            stack2_result = []
            curr = self.root
            stack1.append(curr)

            while(len(stack1)>0):
                curr = stack1.pop()
                stack2.append(curr)
                if curr.Left != None and curr.Right != None:
                    stack1.append(curr.Left)
                    stack1.append(curr.Right)
                elif curr.Left != None and curr.Right == None:
                    stack1.append(curr.Left)
                elif curr.Left == None and curr.Right != None:
                    stack1.append(curr.Right)

            while(len(stack2)>0):
                print(stack2.pop())

    def findSuccessor(self,Node):
        """
        Succesor of a node in a given BST is the next largest element present in the tree, if we perform an inOrder traversal
        it would be the next element in that traversal order.

        Here ,
        I am doing a generalized version, if i were to do it the inorder way i think we would traverse it inOrder till we found the Node
        then we would traverse till the next , find the value break out of the traversal and return it.

        Conditions:
        a) If the node has no right subtree then we traverse up till we find a parent whose left branch contains this node.
                  x
                /   \
              a       z
            /   \   /   \
            b   c   h    k

        Here we see that the succesor of Node = "c" would be the root "x"
        since c is a right child and its parent has less value than it.

        b) if the node has a right subtree then its succesor would be the minimum value present in its right subtree
        """
        if self.root == None:
            return None
        else:
            if self.root.Right != None:
                return min(self.root.Right)
            else:
                # No right tree present
                succesor = root # Default Value
                curr = self.root.Left
                while(curr != None):
                    if curr < Node:
                        curr = curr.Right
                    elif curr > Node:
                        succesor = curr
                        curr = curr.Left
            return succesor

        def findPredeccessor(self,Node):
