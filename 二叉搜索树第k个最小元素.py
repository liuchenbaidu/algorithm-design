# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack:
            while root:            #每次先遍历左子树，
                stack.append(root)
                root = root.left
            root = stack.pop()

            k = k - 1
            if k == 0:
                return root.val
            root = root.right # 右子树 从后面一个个给入栈出栈