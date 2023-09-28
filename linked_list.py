import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def plot(self):
        current = self.head
        node_size = 0.2
        spacing = 0.3

        plt.figure(figsize=(len(self) * spacing, 1))
        pos = 0
        while current:
            plt.gca().add_patch(plt.Rectangle((pos, 0), node_size, node_size, fc='lightblue', ec='black'))
            plt.text(pos + node_size / 2, node_size / 2, str(current.data), ha='center', va='center')
            if current.next:
                plt.arrow(pos + node_size, node_size / 2, spacing - node_size, 0, head_width=0.05, head_length=0.05, fc='black', ec='black')
            current = current.next
            pos += spacing

        plt.title("Linked List Visualization")
        plt.axis('off')
        plt.show()

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    
    print("Linked List:")
    linked_list.display()
    
    linked_list.plot()