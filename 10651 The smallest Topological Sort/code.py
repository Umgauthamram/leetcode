from collections import defaultdict, deque
import sys


def eventualSafeNodes():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  n = int(input_data[0])

  idx = 1
  reversed_adj = defaultdict(list)
  in_degree = [0] * n

  for u in range(n):
    for v in range(n):
      val = int(input_data[idx])
      idx += 1
      if val == 1:
        reversed_adj[v].append(u)
        in_degree[u] += 1

  queue = deque([i for i in range(n) if in_degree[i] == 0])
  safe_nodes = []
  
  while queue:
    node = queue.popleft()
    safe_nodes.append(node)

    for neighbor in reversed_adj[node]:
      in_degree[neighbor] -= 1
      if in_degree[neighbor] == 0:
        queue.append(neighbor)

  safe_nodes.sort()
  print(*(safe_nodes))


if __name__ == "__main__":
  eventualSafeNodes()