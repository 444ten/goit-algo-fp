import uuid
import networkx as nx
import matplotlib.pyplot as plt

# --- Provided Code Class ---
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Use id as unique identifier, store value in label
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def build_heap_tree(heap_array, index=0):
    """
    Recursively builds a tree structure from a heap array.
    """
    if index >= len(heap_array):
        return None

    node = Node(heap_array[index])
    
    # Left child index: 2*i + 1
    node.left = build_heap_tree(heap_array, 2 * index + 1)
    
    # Right child index: 2*i + 2
    node.right = build_heap_tree(heap_array, 2 * index + 2)

    return node

if __name__ == "__main__":
    # Example binary heap (min-heap) array
    heap_list = [1, 3, 5, 7, 9, 10, 12]
    
    print("Visualizing Binary Heap:", heap_list)
    
    heap_root = build_heap_tree(heap_list)
    draw_tree(heap_root)
