# Find Eventual Safe States (Topological Sort / Reverse BFS)

## Core Idea: Reversing the Graph

Instead of starting from every node and walking forward to check for cycles, we reverse all edges and work backward using **Kahn's Algorithm (BFS)**:

- **Original Graph:** Terminal nodes have $0$ outgoing edges (`out_degree == 0`).
- **Reversed Graph:** When edges are reversed, these terminal nodes have $0$ incoming edges (`in_degree == 0`).
- **Backward Traversal:** Starting from terminal nodes, we traverse backward. Any node whose outgoing edges all lead to known safe nodes is also safe and can be added to the queue. Nodes that are part of cycles or point to cycles will never reach `in_degree == 0`.

---

## Code Breakdown Line by Line

### 1. Parse the N x N Matrix & Build Reverse Adjacency List

```python
idx = 1
reversed_adj = defaultdict(list)
in_degree = [0] * n

for u in range(n):
    for v in range(n):
        val = int(input_data[idx])
        idx += 1
        if val == 1:
            reversed_adj[v].append(u)  # Reverse edge: v -> u instead of u -> v
            in_degree[u] += 1          # Track u's outgoing edge count in the original graph
```

- Reads the adjacency matrix entry by entry.
- If `val == 1`, an original directed edge exists: $u \rightarrow v$.
- In the reversed graph, we store $v \rightarrow u$.
- We increment `in_degree[u]`, which tracks the number of **outgoing edges** node $u$ has in the original graph.

---

### 2. Initialize the Queue with Terminal Nodes

```python
queue = deque([i for i in range(n) if in_degree[i] == 0])
safe_nodes = []
```

- Any node with `in_degree[i] == 0` has $0$ outgoing edges in the original graph (it is a **terminal node**).
- These terminal nodes are inherently safe, so they are added to the BFS queue as the starting points.

---

### 3. BFS Traversal Backward

```python
while queue:
    node = queue.popleft()
    safe_nodes.append(node)

    for neighbor in reversed_adj[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)
```

- We dequeue a confirmed safe node (`node`) and append it to `safe_nodes`.
- We iterate over each `neighbor` that pointed to `node` in the original graph.
- We decrement `in_degree[neighbor]`.
- If `in_degree[neighbor] == 0`, all original outgoing paths from `neighbor` lead to verified safe nodes. Therefore, `neighbor` is safe and added to the queue.

---

### 4. Output Result

```python
safe_nodes.sort()
print(*(safe_nodes))
```

- Sort all collected safe nodes in ascending order as required.
- Print the nodes separated by spaces.

---

## Complexity Analysis

- **Time Complexity ($\mathcal{O}(V^2 + V + E)$ / $\mathcal{O}(N^2)$):**
  - Reading and parsing the $N \times N$ adjacency matrix takes $\mathcal{O}(N^2)$.
  - BFS traversal processes each vertex and reversed edge once in $\mathcal{O}(V + E)$.
  - Sorting safe nodes takes $\mathcal{O}(V \log V)$.
  - Overall Time Complexity: $\mathcal{O}(N^2)$ (dominated by reading the full adjacency matrix).

- **Space Complexity ($\mathcal{O}(V + E)$):**
  - Storing the reversed adjacency list and in-degree array takes $\mathcal{O}(V + E)$ space.
  - The BFS queue and result array take $\mathcal{O}(V)$ space.