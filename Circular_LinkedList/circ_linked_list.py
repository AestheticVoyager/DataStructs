# DomirScire

# Circular Linked List
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node

    def append(self, data):
        # If there are no Nodes
        if not self.head:
            self.head=Node(data)
            self.head.next=self.head
        else:
            new_node=Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def remove(self, key):
        if self.head.data == key:
            cur=self.head
            while cur.next != self.head:
                cur=cur.next
            cur.next=self.head.next
            self.head=self.head.next
        else:
            cur=self.head
            prev=None
            while cur.next != self.head:
                prev=cur
                cur=cur.next
                if cur.data == key:
                    prev.next=cur.next
                    cur=cur.next

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def is_circular_linked_list(self, input_list):
        cur=input_list.head
        while cur.next:
            cur=cur.next
            if cur.next == input_list.head:
                return True
        return False

if __name__ == "__main__":
    test = CircularLinkedList()
    test.append("A")
    test.append("B")
    test.append("C")
    test.append("D")
    test.prepend("0")
    test.print_list()
    print('\n')
    test.remove("D")
    test.print_list()
