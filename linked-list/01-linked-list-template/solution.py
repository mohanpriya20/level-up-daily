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

    def append(self, data):
        """Add node with data at the end."""
        new = Node(data)
        if not self.head:
            self.head = new
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new

    def prepend(self, data):
        """Add node with data at the beginning."""
        new = Node(data)
        new.next = self.head
        self.head = new

    def insert_at(self, index, data):
        """Insert node with data at position index (0-based)."""
        # your code here
        pass

    def delete_at(self, index):
        """Remove node at position index (0-based). Return deleted data or None."""
        # your code here
        pass

    def get_at(self, index):
        """Return data at position index, or None if out of range."""
        curr = self.head
        for _ in range(index):
            if not curr:
                return None
            curr = curr.next
        return curr.data if curr else None

    def __len__(self):
        """Return number of nodes."""
        n = 0
        curr = self.head
        while curr:
            n += 1
            curr = curr.next
        return n

    def to_list(self):
        """Return list of all data (head to tail)."""
        out = []
        curr = self.head
        while curr:
            out.append(curr.data)
            curr = curr.next
        return out

    @staticmethod
    def from_list(arr):
        """Build linked list from a list. Returns new LinkedList."""
        ll = LinkedList()
        for x in arr:
            ll.append(x)
        return ll


if __name__ == "__main__":
    ll = LinkedList.from_list([1, 2, 3])
    print("List:", ll.to_list())   # [1, 2, 3]
    print("Length:", len(ll))     # 3
    print("At 1:", ll.get_at(1))  # 2
