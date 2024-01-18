from collections import deque

#  Use deque as we only care about adding and removing head/tail elements: no re-allocation

# Assume graph is an adjaceny list
def dfs(graph, node):
    visited = set()
    stack = deque()


    visited.add(node)
    stack.append(node)

    while stack:
        n = stack.pop()
        print(n, end=" ")
        for adj in graph[n]:
            if adj not in visited:
                visited.add(adj)
                stack.append(adj)

def bfs(graph, node):
    visited = set()
    queue = deque()

    visited.add(node)
    queue.append(node)

    while queue:
        n = queue.popleft()
        print(n, end=" ")
        for adj in graph[n]:
            if adj not in visited:
                visited.add(adj)
                queue.append(adj)

graph = {
    "a": ["b", "c"],
    "b": ["d", "e", "f"],
    "c": ["g"],
    "d": [],
    "e": [],
    "f": ["h"],
    "g": ["i"],
    "h": [],
    "i": [],
}

dfs(graph, "a")
print("")
bfs(graph, "a")

