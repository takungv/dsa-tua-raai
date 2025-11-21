import os
INF = float('inf')

# อ่านข้อมูล
with open("lab10/testcase/testtest.txt", "r", encoding="utf-8") as f:
    data = [int(x) for x in f.read().split() if x.strip()]

n, m, q = data[0:3]
index = 3

# เริ่มต้นตาราง
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0

# ใส่ edge
for _ in range(m):
    u, v, w = data[index:index + 3]
    dist[u][v] = min(dist[u][v], w)
    dist[v][u] = min(dist[v][u], w)
    index += 3

# Floyd–Warshall (Minimax)
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], max(dist[i][k], dist[k][j]))

# Debug index
print(f"\n>>> index after edges: {index}")
print(f"Remaining data (queries): {data[index:]}\n")

# Output
print("===== LOWEST DECIBEL TABLE =====")
for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        val = "INF" if dist[i][j] == INF else str(int(dist[i][j]))
        row.append(f"{val:>4}")
    print(" ".join(row))
print("=========================================================\n")

for _ in range(q):
    s, t = data[index:index + 2]
    index += 2
    if dist[s][t] == INF:
        print(f"{s} -> {t} : No path")
    else:
        print(f"{s} -> {t} : {int(dist[s][t])}")