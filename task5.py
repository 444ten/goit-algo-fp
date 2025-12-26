import uuid
import networkx as nx
import matplotlib.pyplot as plt
import collections

class Node:
    def __init__(self, key, color="#CCCCCC"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
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

def draw_tree(tree_root, title="Tree"):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def generate_color_gradient(n_steps):
    """Generates a list of hex colors from dark blue to light blue."""
    colors = []
    for i in range(n_steps):
        # Interpolate between dark (#1230F0) and light (#CCEEFF)
        r = int(18 + (204 - 18) * i / max(1, n_steps - 1))
        g = int(48 + (238 - 48) * i / max(1, n_steps - 1))
        b = int(240 + (255 - 240) * i / max(1, n_steps - 1))
        colors.append(f"#{r:02x}{g:02x}{b:02x}")
    return colors


def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def visualize_dfs(root):
    if not root:
        return
    
    total_nodes = count_nodes(root)
    colors = generate_color_gradient(total_nodes)
    
    stack = [root]
    visited_order = []
    
    while stack:
        node = stack.pop()
        visited_order.append(node)
        
        # Push right then left so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    for i, node in enumerate(visited_order):
        node.color = colors[i]
        
    draw_tree(root, "DFS Traversal Visualization")

def visualize_bfs(root):
    if not root:
        return

    total_nodes = count_nodes(root)
    colors = generate_color_gradient(total_nodes)

    queue = collections.deque([root])
    visited_order = []

    while queue:
        node = queue.popleft()
        visited_order.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    for i, node in enumerate(visited_order):
        node.color = colors[i]

    draw_tree(root, "BFS Traversal Visualization")

if __name__ == "__main__":
    root_dfs = Node(0)
    root_dfs.left = Node(4)
    root_dfs.left.left = Node(5)
    root_dfs.left.right = Node(10)
    root_dfs.right = Node(1)
    root_dfs.right.left = Node(3)

    print("Visualizing DFS...")
    visualize_dfs(root_dfs)

    root_bfs = Node(0)
    root_bfs.left = Node(4)
    root_bfs.left.left = Node(5)
    root_bfs.left.right = Node(10)
    root_bfs.right = Node(1)
    root_bfs.right.left = Node(3)

    print("Visualizing BFS...")
    visualize_bfs(root_bfs)
