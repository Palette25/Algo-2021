class Solution:
    def getHeight(self, root: TreeNode) -> int:
        # Empty Node
        if not root: 
            return 0
        # Leaf Node
        if root.left == None and root.right == None:
            return 1

        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        # Empty Node
        if not root: 
            return True
        # Leaf Node
        if root.left == None and root.right == None:
            return True
        # First check children's balance
        leftBalanced = self.isBalanced(root.left)
        rightBalanced = self.isBalanced(root.right)

        if not leftBalanced or not rightBalanced:
            return False
        
        # Then check root node's balance
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False
        else:
            return True