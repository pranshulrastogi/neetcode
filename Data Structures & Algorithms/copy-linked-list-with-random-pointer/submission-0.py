"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = None

        p = head
        addr = {}
        q = None
        old_node_loc = {}
        new_loc_node = {}
        count = 0
        new_head = None
        while p:
            new_node = Node(p.val)
            new_loc_node[count] = new_node
            old_node_loc[p] = count
            count += 1 
            if new_head is None:
                new_head = new_node
                q = new_head
            else:
                q.next = new_node
                q = q.next
            p = p.next
        p = head
        q = new_head
        count = 0
        # print(f"{old_node_loc=}")
        while p:
            # print(f"{p.random=}")
            if p.random is not None:
                old_location = old_node_loc[p.random]
                new_random = new_loc_node[old_location]
                q.random = new_random
            else:
                q.random = None
            p = p.next
            q = q.next
            count += 1
        return new_head 
            