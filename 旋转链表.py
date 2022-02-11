# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head or not head.next:
            return head

        cur = head
        n = 1  # 链表的长度  注意初始值是1开始
        while cur.next:    #注意的cur.next 不是cur
            cur = cur.next
            n = n + 1

        add = n - k % n
        if add == n:
            return head
        # print('cur',cur,n)
        cur.next = head  # 建立循环链表
        # print(add,'add')
        while add:
            cur = cur.next
            add = add - 1

        newhead = cur.next # 返回的新链表是下一个节点

        cur.next = None
        return newhead