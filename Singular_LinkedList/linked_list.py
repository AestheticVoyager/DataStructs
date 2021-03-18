# DomirScire
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Head pointer always points to the first Node in the Linked List
    # So we will print the node that Head points to up to the point that
    # Next would point to NULL and stop printing there
    # cur_node will be our new pointer for his function
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    # Add a Node to the End of the LinkedList
    def append(self, data):
        new_node = Node(data)

        # For the edge case of having no nodes in the linked list
        if self.head is None:
            self.head = new_node
            return

        # Code Below will point the head pointer to the last Node in the list
        # Then will loop till the node.next is NULL, which means it is the Last node in the linked list
        # Then append the new Node to the next of the last Node, and we have the append sorted out
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Add a Node to the beggining of the LinkedList
    # The next of New Node must point to the old first Node of the LinkedList
    # and the header pointer must point to the new first node of the LinkedList
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Create a New Node, have its next pointer to point to the node we want it to be placed before
    # Change the next pointer of the Node before to the new Node we just placed in between
    # Obviously the previous next pointer should be removed
    def insert_after_node(self, prev_node, data):

        # Checking if the previous Node is even in the List
        if not prev_node:
            print("Previous node is NOT in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # The node we want to delete is either the Head or its NOT

    # Its head so we do these:
    # Change the head to the next Node, then remove the head's next pointer and set the head node to NULL

    # Its NOT head so do these:
    # Find the nodes after and before the node we want to delete
    # The next pointer of the prev node should point to the node after the node we are deleting
    # Remove the next pointer of the node we are deleting
    # make the node we wanted to delete NULL, by making it None
    def delete_node(self, key):
        cur_node = self.head
        # it is HEAD
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        # it is NOT head
        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        # If we are looking for a node that is NOT in the Linked List
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    # Deleting node at position
    # Just like before we will have 2 different cases, when the position is 0 and when it is NOT 0 
    def delete_node_at_pos(self, pos):
        cur_node = self.head

        # If the position is 0
        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        # in case the position is not in the linked list and over the count of elements
        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    # Length of the Linked List
    def len_iterative(self):
        count = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.next
            count += 1
        return count

    # pass in the head and it will count recursively from there
    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    # 2 cases: The two keys are NOT head node
    # Either of the keys is the head node
    def swap_nodes(self, key_1 , key_2):

        # swapping a node with itself
        if key_1 == key_2:
            return

        prev_1 = None
        cur_1 = self.head
        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        prev_2 = None
        cur_2 = self.head
        while cur_2 and cur_2.data != key_2:
            prev_2 = cur_2
            cur_2 = cur_2.next

        # when either key_1 or key_2 does NOT exist in Linked List
        if not cur_1 or not cur_2:
            return

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2

        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1

        cur_1.next, cur_2.next = cur_2.next, cur_1.next

    # Counting occurences iteratively
    def count_occurences_iterative(self, data):
        count = 0
        cur = self.head
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    # Counting occurences recursively
    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    # Function to remove duplicates
    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()
        while cur:
            if cur.data in dup_values:
                # Remove Node
                prev.next = cur.next
                cur = None
            else:
                # Have not encountered element before
                dup_values[cur.data] = 1
                prev = cur
            cur = prev.next

    # Function to help with understanding reverse_iterative function
    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            # nxt is temp pointer that keeps the value of cur.next before flipping to point to prev
            nxt = cur.next

            cur.next = prev
            # To HELP understand
            # self.print_helper(prev, "PREV")
            # self.print_helper(cur, "CUR")
            # self.print_helper(nxt, "NXT")
            # print(\n)
            prev = cur
            cur = nxt
        # one last thing to do is to change the head pointer to point to last node
        self.head = prev

    def reverse_recursive(self):
        # Helper function to the method
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self. head = _reverse_recursive(cur=self.head, prev=None)

    def move_tail_to_head(self):
        last = self.head
        second_to_last = None
        while last.next:
            second_to_last = last
            last = last.next
        last.next = self.head
        second_to_last.next = None
        self.head = last

# Driver Code
if __name__ == "__main__":
    ''''
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.prepend("E")

    llist.print_list()
    # Putting X in between B and C
    # Because E is the first node, head pointer points to that
    # Count how many nexts are required for you to select the prev_node
    llist.insert_after_node(llist.head.next.next, "X")
    llist.delete_node("X")
    llist.print_list()
    '''

    # test code for occurences
    '''
    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(1)
    llist.append(4)
    llist.append(4)
    llist.append(4)

    print(llist.count_occurences_iterative(4))
    print(llist.count_occurences_recursive(llist.head, 8))
    '''

    # test code for removnig duplicates
    '''
    llist = LinkedList()
    llist.append(1)
    llist.append(6)
    llist.append(1)
    llist.append(4)
    llist.append(2)
    llist.append(2)
    llist.append(4)
    llist.remove_duplicates()
    llist.print_list()
    '''

    # test code for reversing linked list
    '''
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")

    llist.reverse_iterative()
    llist.reverse_recursive()
    llist.print_list()
    '''

    # test code for len
    '''
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    print(llist.len_iterative())
    print(llist.len_recursive(llist.head))
    '''

    # test code for swap nodes
    '''
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    #llist.swap_nodes("B", "C")
    llist.swap_nodes("A", "D")
    llist.print_list()
    '''

    # test code for tail to head
    '''
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.move_tail_to_head()
    llist.print_list()
    '''
