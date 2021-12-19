"""
File: add2.py
Name: Elaine Chu
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    cur_1 = l1
    cur_2 = l2
    ans = None
    while cur_1 or cur_2 is not None:
        if cur_1 is None:
            new_node = ListNode(cur_2.val, None)
            cur_2 = cur_2.next
        elif cur_2 is None:
            new_node = ListNode(cur_1.val, None)
            cur_1 = cur_1.next
        else:
            new_node = ListNode(cur_1.val + cur_2.val, None)
            cur_1 = cur_1.next
            cur_2 = cur_2.next
        if ans is None:
            ans = new_node
        else:
            cur_ans = ans
            while cur_ans.next is not None:
                cur_ans = cur_ans.next
            cur_ans.next = new_node
    cur_ans = ans  # The next node
    last_node = cur_ans  # The previous node
    a = 0  #
    while cur_ans is not None:
        cur_ans.val = cur_ans.val + a
        if cur_ans.val >= 10:
            a = cur_ans.val // 10
            cur_ans.val = cur_ans.val % 10
        else:
            a = 0
        last_node = cur_ans
        cur_ans = cur_ans.next
    if a != 0:
        new_node = ListNode(a, None)
        last_node.next = new_node
    return ans


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()
