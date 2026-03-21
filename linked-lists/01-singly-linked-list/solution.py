# Singly linked list — template


class Node:
    """Single node: data and next pointer."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Singly linked list with head. Implement methods as needed."""
    def __init__(self):
        self.head = None
         
    # add a node at the beginning of the list
    def add_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
    
    #add a node at the end of the list
    def add_last(self, data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
        else:
            current = self.head
            while(current.next is not None):
                current = current.next
            #add the new node to the end of the list
            current.next = new_node
    
    def add_at_index(self, index, data):
        prev = None
        current = self.head
        len = self.size()
        if(index < 0 or index > len):
            return
        if index == 0:
            self.add_first(data)
            return
        else:
            new_node = Node(data)
            while(index > 0):
                prev = current
                current = current.next
                index -= 1
            new_node.next = current 
            prev.next = new_node
            
    def delete_first(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            return
        
    def delete_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        prev = None
        while current.next is not None:
            prev = current
            current = current.next
        prev.next = None
        
    def delete_at_index(self, index):
        if self.head is None or index < 0:
            return
        if index == 0:
            self.delete_first()
            return
        prev = None
        current = self.head
        while index > 0 and current is not None:
            prev = current
            current = current.next
            index -= 1
        if current is None:
            return  # index out of range
        prev.next = current.next
        
    def get_first(self):
        if self.head is not None:
            return self.head.data
        else:
            return None
        
    def get_last(self):
        if self.head is not None:
            current = self.head
            while(current.next is not None):
                current = current.next
            return current.data
        else:
            return None
        
    def get_at_index(self, index):
        if index < 0 or index >= self.size():
            return None
        if index == 0:
            return self.get_first()
        current =  self.head
        while index > 0 and current is not None:
            current = current.next
            index -= 1
        return current.data
    
    def size(self):
        current = self.head
        length = 0
        while(current is not None):
            length += 1
            current = current.next
        return length
    
    def print_list(self):
        current = self.head
        while(current is not None):
            print(current.data, end="-->")
            current = current.next
        print()


if __name__ == "__main__":
    SLL = LinkedList()
    SLL.add_first(20)
    SLL.print_list()
    SLL.add_first(10)
    SLL.add_at_index(0, 5)
    SLL.add_last(30)
    SLL.add_at_index(1, 25)
    SLL.print_list()
    print(SLL.size())
    print(SLL.get_first())
    print(SLL.get_last())
    print(SLL.get_at_index(1))
    SLL.delete_first()
    SLL.delete_last()
    SLL.delete_at_index(1)
    SLL.print_list()