#@title q5) BST to LINKEDLIST
class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root):
        if not root:
            return None

        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root

def print_linked_list(root):
    while root:
        print(root.val, '->', end='')
        root = root.right
    print("\b\b")

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.right.left = TreeNode(7)

    s1= Solution()
    s1.flatten(root)

    print("Flattened Linked List:")
    print_linked_list(root)
