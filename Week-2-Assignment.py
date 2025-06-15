# Week 2 Task
# Implemented a Singly Linked List in Python using Object-Oriented Programming
# Features: Add Node, Print List, and Delete Nth Node with proper edge case handling

class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Manages operations on the singly linked list."""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Adds a node with the given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        """Prints all nodes in the list."""
        if not self.head:
            print("List is empty")
            return

        current = self.head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """
        Deletes the node at position n (1-based index).

        Raises:
            IndexError: If the list is empty or n is out of range.
        """
        if n <= 0:
            raise IndexError("Position must be >= 1")

        if not self.head:
            raise IndexError("Cannot delete from an empty list")

        if n == 1:
            print(f"Deleted node at position {n}: {self.head.data}")
            self.head = self.head.next
            return

        current = self.head
        prev = None
        count = 1

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError(f"Position {n} is out of range")

        print(f"Deleted node at position {n}: {current.data}")
        prev.next = current.next


# Test Cases
if __name__ == "__main__":
    ll = LinkedList()

    print("Adding nodes: 10, 20, 30, 40, 50")
    for value in [10, 20, 30, 40, 50]:
        ll.add_node(value)
    ll.print_list()

    print("\nDeleting 3rd node")
    try:
        ll.delete_nth_node(3)
        ll.print_list()
    except IndexError as e:
        print(f"Error: {e}")

    print("\nAttempting to delete 10th node (invalid)")
    try:
        ll.delete_nth_node(10)
    except IndexError as e:
        print(f"Error: {e}")

    print("\nDeleting 1st node")
    try:
        ll.delete_nth_node(1)
        ll.print_list()
    except IndexError as e:
        print(f"Error: {e}")

    print("\nDeleting remaining nodes")
    try:
        ll.delete_nth_node(1)
        ll.delete_nth_node(1)
        ll.delete_nth_node(1)
        ll.print_list()
    except IndexError as e:
        print(f"Error: {e}")

    print("\nTrying to delete from an empty list")
    try:
        ll.delete_nth_node(1)
    except IndexError as e:
        print(f"Error: {e}")


"""
OUTPUT:

Adding nodes: 10, 20, 30, 40, 50
10 -> 20 -> 30 -> 40 -> 50 -> None

Deleting 3rd node
Deleted node at position 3: 30
10 -> 20 -> 40 -> 50 -> None

Attempting to delete 10th node (invalid)
Error: Position 10 is out of range

Deleting 1st node
Deleted node at position 1: 10
20 -> 40 -> 50 -> None

Deleting remaining nodes
Deleted node at position 1: 20
Deleted node at position 1: 40
Deleted node at position 1: 50
List is empty

Trying to delete from an empty list
Error: Cannot delete from an empty list
"""