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

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 递归调用
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        def dfs(index,r):
			# 假设res是[ [1],[2,3] ]， index是3，就再插入一个空list放到res中
            if len(res)<index:
                res.append([])
			#  将当前节点的值加入到res中，index代表当前层，假设index是3，节点值是99
			# res是[ [1],[2,3] [4] ]，加入后res就变为 [ [1],[2,3] [4,99] ]
            res[index-1].append(r.val)
			# 递归的处理左子树，右子树，同时将层数index+1
            if r.left:
                dfs(index+1,r.left)
            if r.right:
                dfs(index+1,r.right)
        dfs(1,root)
        return res
