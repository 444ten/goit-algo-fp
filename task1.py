class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    # 1. Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    # 2. Sorting algorithm (Merge Sort)
    def merge_sort(self):
        self.head = self._merge_sort_recursive(self.head)

    def _merge_sort_recursive(self, head):
        if head is None or head.next is None:
            return head

        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        left = self._merge_sort_recursive(head)
        right = self._merge_sort_recursive(next_to_middle)

        sorted_list = self._sorted_merge(left, right)
        return sorted_list

    def _get_middle(self, head):
        if head is None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def _sorted_merge(self, a, b):
        if a is None:
            return b
        if b is None:
            return a

        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
        return result

# 3. Function to merge two sorted linked lists into one
def merge_two_sorted_lists(l1, l2):
    dummy = Node()
    tail = dummy
    
    current1 = l1.head
    current2 = l2.head

    while current1 and current2:
        if current1.data <= current2.data:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next
        tail = tail.next

    if current1:
        tail.next = current1
    elif current2:
        tail.next = current2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# --- Testing ---
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(20)
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(30)
    ll.insert_at_end(5)
    ll.insert_at_end(25)

    print("Original list:")
    ll.print_list()

    print("\nReversed list:")
    ll.reverse()
    ll.print_list()

    print("\nSorted list (Merge Sort):")
    ll.merge_sort()
    ll.print_list()

    # Create second sorted list
    ll2 = LinkedList()
    ll2.insert_at_end(2)
    ll2.insert_at_end(15)
    ll2.insert_at_end(35)
    print("\nSecond sorted list:")
    ll2.print_list()

    print("\nMerged sorted lists:")
    merged = merge_two_sorted_lists(ll, ll2)
    merged.print_list()
