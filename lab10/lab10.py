import os
INF = float('inf')

with open("lab10/testcase/10.1.txt", "r", encoding="utf-8") as f:
    data = list(map(int, f.read().split()))

n, m, q = data[0:3]
index = 3

# เริ่มต้นตารางเสียงสูงสุด
dist = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dist[i][i] = 0

# ใส่ข้อมูลเส้นเชื่อม
for _ in range(m):
    u, v, w = data[index:index+3]
    dist[u][v] = min(dist[u][v], w)
    dist[v][u] = min(dist[v][u], w)
    index += 3

print("===== INITIAL TABLE (Before update) =====")
for i in range(1, n + 1):
    row = []
    for j in range(1, n + 1):
        if dist[i][j] == INF:
            row.append("INF")
        else:
            row.append(str(int(dist[i][j])))
    print(" ".join(f"{x:>4}" for x in row))
print("=========================================================\n")

# Floyd–Warshall แบบ Minimax
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dist[i][j] = min(dist[i][j], max(dist[i][k], dist[k][j]))

    # แสดงตารางหลังอัปเดตแต่ละ k
    print(f"===== TABLE AFTER k = {k} =====")
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            if dist[i][j] == INF:
                row.append("INF")
            else:
                row.append(str(int(dist[i][j])))
        print(" ".join(f"{x:>4}" for x in row))
    print("=========================================================\n")


#OUTPUT
print("===== QUERY RESULTS =====")
for _ in range(q):
    s, t = data[index:index+2]
    index += 2
    if dist[s][t] == INF:
        print(f"{s} -> {t} : No path")
    else:
        print(f"{s} -> {t} : {int(dist[s][t])}")