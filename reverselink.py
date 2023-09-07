'''list1=[1,4,3,5,2]
left=4
right=2
index=None
for i in range(len(list1)):
    if list1[i] == left:
        index = i
        break

if index is not None:
    list1[index] = right

print(list1)'''
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not (head and left < right):
            return head

        def helper(node, m):
            nonlocal left, right
            if m == left:
                prev = None
                current = node
                while m <= right:
                    current.next, prev, current = prev, current, current.next
                    m += 1
                node.next = current
                return prev
            elif m < left:
                node.next = helper(node.next, m + 1)
            return node

        return helper(head, 1)

        
        
