from collections import defaultdict, deque
import sys

def eventualSafeNodes():
  input_data = sys.stdin.read().split()
  if not input_data:
    return

  n = int(input_data[0])

  x = 1
  reversedadj = defaultdict(list)
  indegree = [0] * n

  for u in range(n):
    for v in range(n):
      val = int(input_data[x])
      x += 1
      if val == 1:
        reversedadj[v].append(u)
        indegree[u] += 1

  queue = deque([i for i in range(n) if indegree[i] == 0])
  safe = []
  
  while queue:
    node = queue.popleft()
    safe.append(node)

    for y in reversedadj[node]:
      indegree[y] -= 1
      if indegree[y] == 0:
        queue.append(y)

  safe.sort()
  print(*(safe))


if __name__ == "__main__":
  eventualSafeNodes()