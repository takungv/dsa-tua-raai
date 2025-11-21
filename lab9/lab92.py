def dfs1(node, G, visited, order):
    visited[node] = True
    for nxt in G[node]:
        if not visited[nxt]:
            dfs1(nxt, G, visited, order)
    order.append(node)

def dfs2(node, R, visited):
    visited[node] = True
    for nxt in R[node]:
        if not visited[nxt]:
            dfs2(nxt, R, visited)

# อ่านไฟล์ input.txt
with open("lab9/testcase/Extra9.6.txt", "r") as f:
    data = f.read().strip().split()

it = iter(data)

outputs = []

while True:
    N = int(next(it))
    M = int(next(it))

    if N == 0 and M == 0:
        break

    G = [[] for _ in range(N + 1)]
    R = [[] for _ in range(N + 1)]

    # อ่าน M เส้นทาง
    for _ in range(M):
        a = int(next(it))
        b = int(next(it))
        c = int(next(it))

        if c == 1:
            G[a].append(b)
            R[b].append(a)
        elif c == 2:
            G[a].append(b)
            G[b].append(a)
            R[b].append(a)
            R[a].append(b)

    # --- Kosaraju Step 1 ---
    visited = [False] * (N + 1)
    order = []

    for i in range(1, N + 1):
        if not visited[i]:
            dfs1(i, G, visited, order)

    # --- Kosaraju Step 2 ---
    visited = [False] * (N + 1)
    scc_count = 0

    for node in reversed(order):
        if not visited[node]:
            dfs2(node, R, visited)
            scc_count += 1

    outputs.append(str(scc_count))

# แสดงผลทั้งหมด
print("\n".join(outputs))
