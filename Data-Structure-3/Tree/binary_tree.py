class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if root is None:
            return TreeNode(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root
    
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if root.left is None:
                return root.right 
            elif root.right is None:
                return root.left
            
            min_node = self._min(root.right)
            root.key = min_node.key
            root.right = self._delete(root.right, min_node.key)

        return root
    

    def _min(self, root):
        current = root
        while current is not None:
            current = current.left 
        return current
    

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, root, result):
        if root:
            self._inorder(root.left, result)
            result.append(root.key)
            self._inorder(root.right, result)

    def preoder(self):
        result = []
        self._preorder(self.root, result)
        return result
    
    def _preorder(self, root, result):
        if root:
            result.append(root.key)
            self._preorder(root.left, result)
            self._preorder(root.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result
    
    def _postorder(self, root, result):
        if root:
            self._postorder(root.left, result)
            self._preorder(root.right, result)
            result.append(root.key)




        
        
        
tree = BinaryTree()

tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(17)


print("Inorder traversal:", tree.inorder())
print("Preorder traversal:", tree.preoder())
print("Postorder traversal:", tree.postorder())