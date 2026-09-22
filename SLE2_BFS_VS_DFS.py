from collections import deque
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


# ---------------- BFS ----------------
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    nodes_expanded = 0

    while queue:
        node, path = queue.popleft()

        if node in visited:
            continue

        visited.add(node)
        nodes_expanded += 1

        if node == goal:
            return path, nodes_expanded

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append((neighbour, path + [neighbour]))

    return None, nodes_expanded


# ---------------- DFS ----------------
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


# Number of runs
runs = 3


# ---------------- BFS PROFILING ----------------
bfs_times = []
bfs_nodes = []

for i in range(runs):
    start_time = time.perf_counter()

    bfs_path, bfs_node_count = bfs(graph, 'A', 'G')

    end_time = time.perf_counter()

    execution_time = (end_time - start_time) * 1000

    bfs_times.append(execution_time)
    bfs_nodes.append(bfs_node_count)


# ---------------- DFS PROFILING ----------------
dfs_times = []
dfs_nodes = []

for i in range(runs):
    start_time = time.perf_counter()

    dfs_path, dfs_node_count = dfs(graph, 'A', 'G')

    end_time = time.perf_counter()

    execution_time = (end_time - start_time) * 1000

    dfs_times.append(execution_time)
    dfs_nodes.append(dfs_node_count)


# ---------------- CALCULATIONS ----------------

bfs_average = sum(bfs_times) / len(bfs_times)
bfs_best = min(bfs_times)
bfs_worst = max(bfs_times)
bfs_average_nodes = sum(bfs_nodes) / len(bfs_nodes)

dfs_average = sum(dfs_times) / len(dfs_times)
dfs_best = min(dfs_times)
dfs_worst = max(dfs_times)
dfs_average_nodes = sum(dfs_nodes) / len(dfs_nodes)


# ---------------- OUTPUT ----------------

print("\n==============================================")
print("          BFS vs DFS PROFILING")
print("==============================================")

print("\nBFS PATH:", bfs_path)
print("DFS PATH:", dfs_path)


print("\n------------- INDIVIDUAL RUNS ---------------")

print("\nBFS:")
print("Run 1 :", round(bfs_times[0], 6), "ms")
print("Run 2 :", round(bfs_times[1], 6), "ms")
print("Run 3 :", round(bfs_times[2], 6), "ms")

print("\nDFS:")
print("Run 1 :", round(dfs_times[0], 6), "ms")
print("Run 2 :", round(dfs_times[1], 6), "ms")
print("Run 3 :", round(dfs_times[2], 6), "ms")


print("\n------------- COMPARISON TABLE --------------")

print("+----------------------+---------------+---------------+")
print("| Metric               | BFS           | DFS           |")
print("+----------------------+---------------+---------------+")
print("| Average Time (ms)    | {:>13.6f} | {:>13.6f} |".format(
    bfs_average, dfs_average))
print("| Best Time (ms)       | {:>13.6f} | {:>13.6f} |".format(
    bfs_best, dfs_best))
print("| Worst Time (ms)      | {:>13.6f} | {:>13.6f} |".format(
    bfs_worst, dfs_worst))
print("| Nodes Expanded       | {:>13.2f} | {:>13.2f} |".format(
    bfs_average_nodes, dfs_average_nodes))
print("+----------------------+---------------+---------------+")


# ---------------- ANALYSIS ----------------

print("\n------------- ANALYSIS ---------------------")

if bfs_average < dfs_average:
    print("Lower average execution time : BFS")
else:
    print("Lower average execution time : DFS")

if bfs_average_nodes < dfs_average_nodes:
    print("Fewer nodes expanded         : BFS")
elif dfs_average_nodes < bfs_average_nodes:
    print("Fewer nodes expanded         : DFS")
else:
    print("Nodes expanded               : Same")


print("\n------------- CONCLUSION -------------------")

if bfs_average < dfs_average:
    print("For this graph, BFS had the lower average execution time.")
else:
    print("For this graph, DFS had the lower average execution time.")

print("The comparison is based on the measured execution")
print("time and number of nodes expanded.")