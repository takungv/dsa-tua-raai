import math

def min_triangulation_cost(points):
    # points: list[(x, y)] เรียงรอบรูป และรูปต้องนูน
    n = len(points)
    if n < 3:
        return 0.0

    def dist(a, b):
        return math.hypot(a[0]-b[0], a[1]-b[1])

    def peri(i, j, k):
        return (dist(points[i], points[j]) +
                dist(points[j], points[k]) +
                dist(points[k], points[i]))

    INF = float("inf")
    dp = [[0.0]*n for _ in range(n)]

    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            best = INF
            for k in range(i+1, j):
                best = min(best, dp[i][k] + dp[k][j] + peri(i, k, j))
            dp[i][j] = best
    return dp[0][n-1]

# ตัวอย่างจากโจทย์
pts = [(0,0), (1,0), (2,1), (1,2), (0,2)]
ans = min_triangulation_cost(pts)
print(f"{ans:.4f}")   # 15.3006
