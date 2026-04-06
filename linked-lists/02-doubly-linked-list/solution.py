# Doubly linked list — template
class Node:
    """Node with previous and next pointers."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Doubly linked list. Implement methods as needed."""
    def __init__(self):
        self.head = None
        self.tail = None  # optional: maintain tail for O(1) add_last

    def add_first(self, data):
        # your logic here
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def add_last(self, data):
        # your logic here
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            new_node.prev = current
            current.next = new_node
            self.tail = new_node
            
    
    def add_at(self, index, data):
        # your logic here
        if index<0 or index>self.length():
            return "Invalid index"
        if index == 0:
            self.add_first(data)
            return
        else:
            new_node = Node(data)
            current = self.head
            prev = None
            while(index > 0 and current is not None):
                prev = current
                current = current.next
                index-=1
            new_node.next = current
            new_node.prev = prev
            prev.next = new_node
            if current is not None:
                current.prev = new_node
            

    def delete_first(self):
        # your logic here
        pass

    def delete_last(self):
        # your logic here
        pass
    
    def delete_at(self, index):
        # your logic here
        pass
    
    def get_first(self):
        # your logic here
        pass
    
    def get_last(self):
        # your logic here
        pass
    
    def length(self):
        length = 0
        current = self.head
        while current is not None:
            current = current.next
            length +=1
        return length

    def get_at(self, index):
        """Value at 0-based index (or None / raise if out of range)."""
        # your logic here
        pass

    

    def __str__(self):
        parts = []
        cur = self.head
        while cur:
            parts.append(str(cur.data))
            cur = cur.next
        return " <-> ".join(parts) if parts else "(empty)"


if __name__ == "__main__":
    dll = DoublyLinkedList()
    # add tests when you implement
