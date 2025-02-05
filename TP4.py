from heapq import heappush, heappop

def create_weighted_graph():
    num_nodes = 9
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    edges = [
        (1, 2, 4), (1, 5, 2),
        (2, 3, 7), (2, 6, 5),
        (3, 4, 1), (3, 6, 8),
        (4, 7, 4), (4, 8, 3),
        (5, 6, 9), (5, 7, 10),
        (6, 7, 2), (6, 4, 5),
        (7, 8, 8), (7, 9, 2),
        (8, 9, 1)
    ]

    for u, v, w in edges:
        adjacency_matrix[u - 1][v - 1] = w
        adjacency_matrix[v - 1][u - 1] = w  

    return adjacency_matrix

def prims_algorithm(graph, start_node):
    num_nodes = len(graph)
    visited = [False] * num_nodes
    mst_edges = []
    total_weight = 0

    priority_queue = [(0, start_node - 1, None)]  
    while priority_queue:
        weight, current_node, parent_node = heappop(priority_queue)

        if visited[current_node]:
            continue

        visited[current_node] = True

        if parent_node is not None:
            mst_edges.append((parent_node + 1, current_node + 1, weight))
            total_weight += weight

        for neighbor in range(num_nodes):
            if graph[current_node][neighbor] > 0 and not visited[neighbor]:
                heappush(priority_queue, (graph[current_node][neighbor], neighbor, current_node))

    return mst_edges, total_weight

def find_root(parent, vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find_root(parent, parent[vertex])  
    return parent[vertex]

def union_sets(parent, rank, vertex1, vertex2):
    root1 = find_root(parent, vertex1)
    root2 = find_root(parent, vertex2)

    if rank[root1] < rank[root2]:
        parent[root1] = root2
    elif rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root2] = root1
        rank[root1] += 1

def kruskals_algorithm(graph):
    num_nodes = len(graph)
    edges = []

    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if graph[i][j] > 0:
                edges.append((graph[i][j], i, j))
    edges.sort()  

    parent = list(range(num_nodes))
    rank = [0] * num_nodes

    mst_edges = []
    total_weight = 0

    for weight, u, v in edges:
        if find_root(parent, u) != find_root(parent, v):
            union_sets(parent, rank, u, v)
            mst_edges.append((u + 1, v + 1, weight))
            total_weight += weight

    return mst_edges, total_weight

if __name__ == "__main__":
    graph = create_weighted_graph()

    try:
        root = int(input("Enter root node (1-9): "))
        if not (1 <= root <= 9):
            raise ValueError("Node out of range")

        print("\nPrim's Algorithm Results:")
        prim_edges, prim_weight = prims_algorithm(graph, root)
        print("MST Edges:", prim_edges)
        print("Total Weight:", prim_weight)

        print("\nKruskal's Algorithm Results:")
        kruskal_edges, kruskal_weight = kruskals_algorithm(graph)
        print("MST Edges:", kruskal_edges)
        print("Total Weight:", kruskal_weight)

    except ValueError as e:
        print(f"Invalid input: {e}")