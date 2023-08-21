'''
input1 = input("Enter list 1 separated by commas: ").split(",")
input2 = input("Enter list 1 separated by commas: ").split(",")
list1 = [int(x) for x in input1]
list2 = [int(x) for x in input2]

merged_list = list1 + list2
print(merged_list)'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # create a dummy node to serve as the head of the new list
    dummy = ListNode(0)
    # create a pointer to the current node in the new list
    current = dummy
    
    # iterate through the input lists and compare their values
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # if one list is longer than the other, append the remaining nodes to the new list
    if l1:
        current.next = l1
    else:
        current.next = l2
    
    # return the head node of the new list (skip the dummy node)
    return dummy.next


print(mergeTwoLists([1,2,3],[2,23]))