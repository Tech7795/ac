#@title q6) Dispalying Modular node in link list
class Node:
    def __init__(self, data,next=None):
        self.data = data
        self.next = next

def find_modular_node(head, k):
    if not head or k <= 0:
        return None

    current, modular_node, count = head, None, 0

    while current:
        count += 1
        if count % k == 0:
            modular_node = current
        current = current.next

    return modular_node

# Example usage:
head = Node(1,Node(2,Node(3,Node(4))))

k = 2  # Change this to the desired value of k

modular_node = find_modular_node(head, k)

if modular_node:
    print(f"The {k}-th modular node from the end is: {modular_node.data}")
else:
    print(f"No modular node found for k = {k}")
