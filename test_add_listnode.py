
class ListNode():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def print_list(l1:ListNode):
    answer = []
    head = l1

    while head :
        answer.append(head.val)
        head = head.next
    return answer


class Solution():

    def addTwoNumbers(self,l1:ListNode,l2:ListNode)->ListNode:

        carry = 0  # 进位
        state = 0
        temp_node = None

        while l1 !=None or l2!=None or carry != 0:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            sum = a + b + carry

            p = ListNode(sum%10)
            carry = sum//10
            print('sum', sum,carry)
            if state == 0:
                state =1
                head = p
                temp_node = head

            else:
                temp_node.next = p
                temp_node = temp_node.next

            l1 = l1.next
            l2 = l2.next

        return head



if __name__ == '__main__':
    app = Solution()
    l1 = [2, 4, 3]
    l2 = [5, 6, 9]
    p1_head  = ListNode(l1[0])
    temp_node = p1_head
    for i in range(1,len(l1)):
        temp_node.next = ListNode(l1[i])
        temp_node = temp_node.next

    p2_head = ListNode(l2[0])
    temp_node = p2_head
    for i in range(1, len(l2)):
        temp_node.next = ListNode(l2[i])
        temp_node = temp_node.next


    print(p1_head, type(p1_head), print_list(p1_head))
    result = app.addTwoNumbers(p1_head,p2_head)
    print(result,type(result))
    print(print_list(result))
