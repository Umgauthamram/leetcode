Problem Explanation
You have numCourses courses labeled 0 to numCourses - 1. Some courses have prerequisites: 
[a, b] means you must take course b before course a (b -> a).

Your goal is to return a valid sequence to take all courses. If there is a cycle (e.g., A -> B -> A), it's impossible to finish, so return [].

def findOrder(self, numCourses, prerequisites):
    adj = defaultdict(list)
    indegree = [0] * numCourses

    for dest, src in prerequisites:
      adj[src].append(dest) 
      indegree[dest] += 1

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []


    while queue:
      node = queue.popleft()
      order.append(node)

      for neighbor in adj[node]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
          queue.append(neighbor)

    return order if len(order) == numCourses else []