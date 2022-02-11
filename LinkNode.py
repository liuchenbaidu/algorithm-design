### 删除链表倒数第n个节点，
# 用栈解决，

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)

        stack = []
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next

        for i in range(n):  #第n个节点出栈
            stack.pop()

        pre = stack[-1]
        pre.next = pre.next.next # 倒数n+1个元素指向下一个元素
        return dummy.next