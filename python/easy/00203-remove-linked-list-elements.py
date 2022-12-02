"""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

1 -> 2 -> 6 -> 3 -> 4 -> 5 -> 6
1 -> 2 -> 3 -> 4 -> 5

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []



Constraints:
The number of nodes in the list is in the range [0, 104].
1 <= Node.val <= 50
0 <= val <= 50
"""



class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_end(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def insert(self, vals):
        for v in vals:
            self.insert_end(v)
    
    def __str__(self):
        result = list()
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return str(result)



def removeElements(head, val):
    if not head:
        return head
    
    elif head.next is None:
        if head.val == val:
            head = head.next
        return head
    
    else:
        prev = None
        curr = head
        
        while curr:
            if curr.val != val:
                prev = curr
            else:
                if curr == head:
                    head = head.next
                else:
                    prev.next = curr.next
            curr = curr.next
        
        return head



if __name__ == '__main__':
    for nums, val in [  ([1,2,6,3,4,5,6], 6),
                        ([], 1),
                        ([7,7,7,7], 7)  ]:
        sll = SLL()
        sll.insert(nums)
        print(f'head={sll}\tval={val}\t', end='')
        sll.head = removeElements(sll.head, val)
        print(f'Output head={sll}')