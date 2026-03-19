# Singly linked list — explanation

## Node

Each node has:
- **data** — value stored in the node
- **next** — reference to the next node (or `None` at the tail)

## LinkedList

- **head** — reference to the first node; empty list has `head is None`.

### Add

- **add_first(data)** — Insert at the beginning. Create new node, set `new_node.next = self.head`, then `self.head = new_node`. O(1).
- **add_last(data)** — Insert at the end. If empty, set head to new node. Else traverse to the last node (`current.next is None`) and set `current.next = new_node`. O(n).
- **add_at_index(index, data)** — Insert at position `index` (0-based). Reject if `index < 0` or `index > size()`. If `index == 0`, link new node before head and update head. Otherwise walk with `prev` and `current` until `current` is the node at `index`, then set `new_node.next = current` and `prev.next = new_node`. Index equal to size() means append at end.

### Delete

- **delete_first()** — If non-empty, set `self.head = self.head.next`. O(1).
- **delete_last()** — If empty, return. If single node, set `self.head = None`. Else traverse to the second-to-last node (`prev`) and set `prev.next = None` so the last node is unlinked. O(n).
- **delete_at_index(index)** — Reject if empty or `index < 0`. If `index == 0`, call delete_first() and return. Else walk with `prev` and `current` until `current` is the node at that index (stop if `current` becomes None for out-of-range). Then set `prev.next = current.next` to skip the node. O(index).

### Get

- **get_first()** — Return `head.data` if head exists, else None.
- **get_last()** — Traverse to the last node and return its data; return None if empty.
- **get_at_index(index)** — Reject if `index < 0` or `index >= size()`. Traverse `index` steps from head and return that node’s data. O(index).

### Other

- **size()** — Traverse from head to end, count nodes. O(n).
- **print_list()** — Traverse and print each node’s data (space-separated).

## Edge cases

- **Empty list:** head is None; add_first / add_last / add_at_index(0) set head; get/delete methods return or do nothing as described.
- **Single node:** delete_last and delete_at_index(0) set `self.head = None`.
- **Out-of-range index:** add_at_index and delete_at_index return without changing the list; get_at_index returns None.

## Time summary

| Operation       | Time  |
| --------------- | ----- |
| add_first       | O(1)  |
| add_last        | O(n)  |
| add_at_index    | O(index) |
| delete_first    | O(1)  |
| delete_last     | O(n)  |
| delete_at_index | O(index) |
| get_first       | O(1)  |
| get_last        | O(n)  |
| get_at_index    | O(index) |
| size            | O(n)  |
