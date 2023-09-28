# Code for a doubly linked list and its graphical representation using matplotlib and networkx. 
# A doubly linked list has nodes that point both to the next node and the previous node.

# In this code, I added a search_and_highlight method that takes an element as input, 
# searches for it in the linked list, and then displays the list with the target element highlighted in green if found.
# If the element is not found, it informs the user.

import networkx as nx
import matplotlib.pyplot as plt

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DoublyNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def plot(self, target_data=None):
        G = nx.DiGraph()
        pos = {}
        labels = {}
        node_colors = []
        edge_colors = []
        current = self.head
        idx = 0

        while current:
            G.add_node(idx)
            pos[idx] = (idx, 0)
            labels[idx] = str(current.data)
            if current.data == target_data:
                node_colors.append('red')
                edge_colors.append('red')
            else:
                node_colors.append('lightblue')
                edge_colors.append('black')
            if current.next:
                G.add_edge(idx, idx + 1)
            if current.prev:
                G.add_edge(idx, idx - 1)
            idx += 1
            current = current.next

        plt.figure(figsize=(len(G) * 0.5, 1))
        nx.draw(G, pos, with_labels=True, labels=labels, node_size=500, font_size=10, font_color='black', node_color=node_colors, edge_color=edge_colors)
        plt.title("Doubly Linked List Visualization")
        plt.axis('off')
        plt.show()

    def search_and_highlight(self, element):
        current = self.head
        found = False
        while current:
            if current.data == element:
                found = True
                break
            current = current.next

        if found:
            print(f"Element {element} found in the list.")
            self.plot(element)
        else:
            print(f"Element {element} not found in the list.")

# Example usage:
if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.append(1)
    doubly_linked_list.append(2)
    doubly_linked_list.append(3)
    doubly_linked_list.append(4)
    
    print("Doubly Linked List:")
    doubly_linked_list.display()
    
    search_element = int(input("Enter an element to search and highlight: "))
    doubly_linked_list.search_and_highlight(search_element)
