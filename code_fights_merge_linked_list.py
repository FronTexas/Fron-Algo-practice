# Definition forc singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None


def move_the_min_pointer_to_the_right(pointer_1, pointer_2, minimum_value):
    if pointer_1 and minimum_value == pointer_1.value: 
        pointer_1 = pointer_1.next
    elif pointer_2 and minimum_value == pointer_2.value: 
        pointer_2 = pointer_2.next 
    return pointer_1, pointer_2

def get_minimum_value_between_two_pointer(pointer_1, pointer_2):
    if pointer_1 and pointer_2:
        minimum_value = min(pointer_1.value, pointer_2.value)
    else: 
        minimum_value = pointer_1.value if pointer_1 else pointer_2.value
    return minimum_value

def mergeTwoLinkedLists(l1, l2):
    pointer_1 = l1 
    pointer_2 = l2 
    answer_head = None 
    answer_current_node = None
    while pointer_1 or pointer_2:
        minimum_value = get_minimum_value_between_two_pointer(pointer_1, pointer_2)

        if not answer_current_node:
            answer_current_node = ListNode(minimum_value)
            answer_head = answer_current_node
        else: 
            answer_current_node.next = ListNode(minimum_value)
            answer_current_node = answer_current_node.next

        pointer_1, pointer_2 = move_the_min_pointer_to_the_right(pointer_1, pointer_2, minimum_value)
    return answer_head


