from binarytree import _build_tree_string


class Node:
    def __init__(self, val, left=None, right=None, level=None):
        self.left = left
        self.right = right
        self.val = val
        self.level = left
        
    def insert(self, data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.val = data
    
    def __str__(self):
        lines = _build_tree_string(self, 0, False, '-')[0]
        return '\n' + '\n'.join((line.rstrip() for line in lines))

    def __repr__(self):
        return f'Node: {self.val}'

    def find_value(self, val):
        if val < self.val:
            if self.left is None:
                return False
            return self.left.find_value(val)
        elif val > self.val:
            if self.right is None:
                return False
            return self.right.find_value(val)
        else:
            return True

    @staticmethod
    def get_node_by_value(root, value):
        while root:
            if root.val > value:
                root = root.left
                continue
            elif root.val < value:
                root = root.right
                continue
            else:
                return root
        return None

    @staticmethod
    def build_from_array(arr: list) -> Node:
        if arr:
            for i in range(len(arr)):
                if i == 0:
                    root = Node(arr[i])
                else:
                    root.insert(arr[i])
        return root
    
    @staticmethod
    def maxDepth(node: Node) -> int: 
        if node is None: 
            return 0
        else : 
            # Compute the depth of each subtree 
            left_depth = maxDepth(node.left) 
            right_depth = maxDepth(node.right) 
    
            # Use the larger one 
            if (left_depth > right_depth): 
                return left_depth+1
            else: 
                return right_depth+1

    @staticmethod
    def bft(self):
        self.root.level = 0 
        queue = [self.root]
        out = []
        current_level = self.root.level

        while len(queue) > 0:
                
            current_node = queue.pop(0)

            if current_node.level > current_level:
                current_level += 1
                out.append("\n")

                out.append(str(current_node.info) + " ")

            if current_node.left:

                current_node.left.level = current_level + 1
                queue.append(current_node.left)
                

            if current_node.right:

                current_node.right.level = current_level + 1
                queue.append(current_node.right)
                        
        print ("".join(out))

    @staticmethod
    def inorder(self,node):
        if node is not None:
            self.inorder(node.left)
            print (node.val)
            self.inorder(node.right)

    @staticmethod
    def preorder(self,node):
        if node is not None:
            print (node.val)
            self.preorder(node.left)
            self.preorder(node.right)

    @staticmethod
    def postorder(self,node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print (node.val)
