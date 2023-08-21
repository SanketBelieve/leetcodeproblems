#s=input("enter a list")
#list = s.split(",")
#print(list)
'''
# Taking a list of integers as input from the user
input_string = input("Enter elements of a list separated by spaces: ")

# Converting the input string to a list of integers
user_list = [int(num) for num in input_string.split()]

# Printing the list
print("List:", user_list)
'''
'''
def duplicate(head):
    if not head or not head.next:
        return head

    current = head
    while current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head
       
nums=[1,1,2]
list = duplicate(nums)
print(list)
'''
def deleteDuplicates(nums):
    if not nums:
        return nums

    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return nums[:i + 1]

s=[1,1,2]
p=deleteDuplicates(s)
print(p)