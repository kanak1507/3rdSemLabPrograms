from queue import PriorityQueue
def best_first_search(graph, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start))
    while not pq.empty():
        cost, node = pq.get()
        if node in visited:
            continue
        visited.add(node)
        print(node)
        if node == goal:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                pq.put((graph[node][neighbor], neighbor))
    return False
graph = {
    'A': {'B': 3, 'C': 6},
    'B': {'D': 2, 'E': 1},
    'C': {'F': 5},
    'D': {},
    'E': {'F': 4},
    'F': {}
}
start_node = 'A'
goal_node = 'F'
result = best_first_search(graph, start_node, goal_node)
print(f"Path found: {result}")