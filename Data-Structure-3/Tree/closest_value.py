class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

def find_closest_value(root, target):
    if not root:
        return None
    
    closest = root.value

    while root:
        if abs(root.value - target) < abs(closest - target):
            closest = root.value

        if target < root.value:
            root = root.left
        elif target > root.value:
            root = root.right
        else:
            return root.value
        
    return closest


root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

print(find_closest_value(root,4 ))