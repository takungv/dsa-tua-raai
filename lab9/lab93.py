def dfs1(node, G, visited, order):
    visited[node] = True
    for nxt in G[node]:
        if not visited[nxt]:
            dfs1(nxt, G, visited, order)
    order.append(node)

def dfs2_collect(node, R, visited, comp_id, cid):
    visited[node] = True
    comp_id[node] = cid
    for nxt in R[node]:
        if not visited[nxt]:
            dfs2_collect(nxt, R, visited, comp_id, cid)

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

    # --- Kosaraju Step 2 (เก็บหมายเลข SCC) ---
    visited = [False] * (N + 1)
    comp_id = [-1] * (N + 1)
    scc_count = 0

    for node in reversed(order):
        if not visited[node]:
            dfs2_collect(node, R, visited, comp_id, scc_count)
            scc_count += 1

    # ถ้ามีแค่ 1 SCC ไม่ต้องเพิ่มเส้นทาง
    if scc_count == 1:
        outputs.append("0")
        continue

    # หาค่า in-degree และ out-degree ของแต่ละ SCC
    indeg = [0] * scc_count
    outdeg = [0] * scc_count

    for u in range(1, N + 1):
        for v in G[u]:
            cu = comp_id[u]
            cv = comp_id[v]
            if cu != cv:
                outdeg[cu] += 1
                indeg[cv] += 1

    # นับ SCC ที่ไม่มี in และไม่มี out
    zero_in = sum(1 for i in range(scc_count) if indeg[i] == 0)
    zero_out = sum(1 for i in range(scc_count) if outdeg[i] == 0)

    # คำตอบคือ max(zero_in, zero_out)
    outputs.append(str(max(zero_in, zero_out)))

# แสดงผลทั้งหมด
print("\n".join(outputs))
