class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True

    if root.value <= min_val and root.value >= max_val:
        return False
    
    return (is_bst(root.left, min_val, root.value) and is_bst(root.right, root.value, max_val))


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)


result = is_bst(root)
print("Is the tree a binary search tree?", result)