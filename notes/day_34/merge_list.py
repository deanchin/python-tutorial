# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    ''' Solution bitch '''
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        l1_ptr = l1
        l2_ptr = l2
        merge_list = ListNode()
        merge_ptr = merge_list
        #  set first value, then always update next
        if l1_ptr.val <= l2_ptr.val:
            merge_ptr.val = l1_ptr.val
            l1_ptr = l1_ptr.next
        else:
            merge_ptr.val = l2_ptr.val
            l2_ptr = l2_ptr.next

        while l1_ptr and l2_ptr:
            if l1_ptr.val <= l2_ptr.val:
                merge_ptr.next = ListNode(l1_ptr.val)
                l1_ptr = l1_ptr.next
            else:
                merge_ptr.next = ListNode(l2_ptr.val)
                l2_ptr = l2_ptr.next
            merge_ptr = merge_ptr.next

        while l1_ptr:
            merge_ptr.next = ListNode(l1_ptr.val)
            l1_ptr = l1_ptr.next
            merge_ptr = merge_ptr.next

        while l2_ptr:
            merge_ptr.next = ListNode(l2_ptr.val)
            l2_ptr = l2_ptr.next
            merge_ptr = merge_ptr.next

        return merge_list

    def print_list(self, l):
        ''' Prints a list '''
        p = l

        while p:
            print(p.val, end='')
            if p.next:
                print('->', end='')
            p = p.next
        print("")


l1 = ListNode(1, ListNode(2, ListNode(4, ListNode(5, ListNode(7)))))
l2 = ListNode(1, ListNode(3, ListNode(4, ListNode(6))))

Solution().print_list(l1)
Solution().print_list(l2)
Solution().print_list(Solution().mergeTwoLists(l1, l2))

# l1 = ListNode(0, ListNode(1, ListNode(2)))

# l2 = ListNode(5)
# print(f'l2={l1}, l2.val={l2.val}, l2.next={l2.next}')
# print("-----------------------------")
# p = l2
# p.next = ListNode(6)
# print(f'p={p}, p.val={p.val}, p.next={p.next}')
# print(f'l2={l2}, l2.val={l2.val}, l2.next={l2.next}')
# print("-----------------------------")
# p = p.next
# print(f'l2={l2}, l2.val={l2.val}, l2.next={l2.next}')
# p.next = ListNode(7)
# print(f'l2={l2}, l2.val={l2.val}, l2.next={l2.next}')

# # print(f'l1={l1}, l1.val={l1.val}, l1.next={l1.next}')
# # l1 = l1.next
# # print(f'l1={l1}, l1.val={l1.val}, l1.next={l1.next}')
# # l1 = l1.next
# # print(f'l1={l1}, l1.val={l1.val}, l1.next={l1.next}')
# # l1 = l1.next
# # print(f'l1={l1}, l1.val={l1.val}, l1.next={l1.next}')

# # print("============================")
# # while l1:
# #     print(f'val={l1.val}')
# #     l1 = l1.next
# print("============================")

# while l2:
#     print(f'val={l2.val}')
#     l2 = l2.next
# print("============================")

# while p:
#     print(f'val={p.val}')
#     p = p.next
# print("============================")

# # OUTPUT
# # ============================
# # 5
# # 6
# # 7
# # ============================
# # 5
# # 6
# # ============================



# # l2 = ListNode()
# # test = Solution().mergeTwoLists(l1, l2)
# # print(f'{test}')