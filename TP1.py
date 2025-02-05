from collections import defaultdict, deque

def path_exists(graph, start, end):
    queue = deque([start])
    visited = set()

    while queue:
        current = queue.popleft()

        if current == end:
            return True

        visited.add(current)

        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append(neighbor)

    return False

graph = {
    1: [2],
    2: [1,5],
    3: [6],
    4: [6, 7],
    5: [2],
    6: [3, 4, 7],
    7: [6, 4]
}

start_node = int(input("Input the start node: "))
end_node = int(input("Input the end node: "))

if path_exists(graph, start_node, end_node):
    print("True")
else:
    print("False")