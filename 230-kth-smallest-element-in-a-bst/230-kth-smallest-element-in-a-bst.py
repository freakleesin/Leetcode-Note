# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        store = []
        def dfs(root):
            if not root:return
            store.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return sorted(store)[k-1]