# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 广度优先排序
# 关键 从一个栈去动态存储每一层的节点，然后遍历取出来，放入list

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root]

        res = []
        while queue:
            temp = []
            size = len(queue)
            for _ in range(size):
                r = queue.pop(0)
                temp.append(r.val)

                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            res.append(temp)

        return res