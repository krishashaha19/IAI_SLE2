import time

# Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}


def dfs(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    nodes_expanded = 0

    while stack:
        node, path = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append((neighbour, path + [neighbour]))

    return None, nodes_expanded


# Profiling
runs = 3
times = []
nodes = []

for i in range(runs):
    start_time = time.perf_counter()

    path, node_count = dfs(graph, 'A', 'G')

    end_time = time.perf_counter()

    execution_time = (end_time - start_time) * 1000

    times.append(execution_time)
    nodes.append(node_count)


average_time = sum(times) / len(times)
average_nodes = sum(nodes) / len(nodes)

print("\n========== DFS ==========")
print("Path:", path)

print("\nIndividual Runs:")
for i, value in enumerate(times, 1):
    print(f"Run {i}: {value:.6f} ms")

print("\nAverage Time:", f"{average_time:.6f}", "ms")
print("Average Nodes Expanded:", f"{average_nodes:.2f}")
