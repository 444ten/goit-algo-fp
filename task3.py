import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, u, v, weight):
        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
        # Undirected graph implementation
        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))

def dijkstra(graph, start_node):
    # Min-heap to store (distance, node). 
    # Distance is first for comparison by heapq.
    min_heap = [(0, start_node)]
    
    # Dictionary to store the shortest distance to each node
    distances = {node: float('infinity') for node in graph.edges}
    distances[start_node] = 0
    
    # To reconstruct the path (optional, but useful)
    previous_nodes = {node: None for node in graph.edges}

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        # If we found a shorter path to current_node previously, skip processing
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

# --- Testing ---
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)
    
    start = 'A'
    shortest_paths = dijkstra(g, start)

    print(f"Shortest paths from {start}:")
    for node, distance in shortest_paths.items():
        print(f"Distance to {node}: {distance}")
