# Singly linked list — template

## Node

Each node has:
- **data** — value stored in the node
- **next** — reference to the next node (or `None` at the tail)

## LinkedList

- **head** — reference to the first node; empty list has `head is None`.
- **append(data)** — add a node at the end (O(n) to find tail).
- **prepend(data)** — add a node at the beginning (O(1)).
- **insert_at(index, data)** — insert at position (implement as needed).
- **delete_at(index)** — remove node at position (implement as needed).
- **get_at(index)** — return data at index (O(index)).
- **len(ll)** — number of nodes (O(n)).
- **to_list()** — return Python list of all data.
- **from_list(arr)** — build a singly linked list from a list (class method).

Use this template for singly linked list problems; copy or import as needed.
