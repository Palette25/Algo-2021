class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs_path(root: TreeNode, path: str):
            if root:
                path += str(root.val)
                # Judge if is the leaf node
                if not root.left and not root.right:
                    res.append(path)
                else:
                    path += '->'
                    # Recursion
                    dfs_path(root.left, path)
                    dfs_path(root.right, path)

        res = []
        dfs_path(root, '')
        
        return res