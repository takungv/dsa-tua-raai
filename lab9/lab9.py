import sys

def dfs(start, graph, visited):
    stack = [start]
    visited[start] = True
    while stack:
        node = stack.pop()
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

with open("lab9/testcase/9.1.txt","r") as f:
    data = f.read().strip().split()

it = iter(data)

outputs = []
while True:
    try:
        N = int(next(it))
        M = int(next(it))
    except StopIteration:
        break
    if N == 0 and M == 0:
        break

    G = [[] for _ in range(N+1)]
    R = [[] for _ in range(N+1)]

    for _ in range(M):
        a = int(next(it)); b = int(next(it)); c = int(next(it))
        if c == 1:
            # ทางเดียว a -> b
            G[a].append(b)
            R[b].append(a)
        elif c == 2:
            # สองทาง a <-> b
            G[a].append(b)
            G[b].append(a)
            R[b].append(a)
            R[a].append(b)
        # c == 0 => ข้าม

    # ถ้ไม่มี node 1 อยู่ ให้ถือว่าไม่ครบ (แต่โจทย์มักเริ่ม index ที่ 1..N)
    # DFS บนกราฟจริง
    visited = [False] * (N+1)
    dfs(1, G, visited)
    if not all(visited[1:]):
        outputs.append("0")
        continue

    # DFS บนกราฟกลับทิศ
    visited = [False] * (N+1)
    dfs(1, R, visited)
    if not all(visited[1:]):
        outputs.append("0")
        continue

    outputs.append("1")

print("\n".join(outputs))
