import math

# --------- Geometry Helpers ---------
def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def triangle_cost(p, i, j, k):
    return dist(p[i], p[j]) + dist(p[j], p[k]) + dist(p[k], p[i])


# --------- Sort Points into a Proper Polygon (CCW) ---------
def sort_points_as_polygon(points):
    # centroid
    cx = sum(p[0] for p in points) / len(points)
    cy = sum(p[1] for p in points) / len(points)

    # sort by angle around centroid
    return sorted(points, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))


# --------- Triangulation DP ---------
def min_triangulation_dp(points):
    n = len(points)
    dp = [[0.0] * n for _ in range(n)]

    for L in range(3, n + 1):  # L = polygon length
        for i in range(n - L + 1):
            j = i + L - 1
            dp[i][j] = float("inf")

            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + triangle_cost(points, i, k, j)
                dp[i][j] = min(dp[i][j], cost)

    return dp


# --------- Print DP Table ---------
def print_dp_table(dp):
    n = len(dp)
    print("\n=== DP TABLE ===")
    for i in range(n):
        row = []
        for j in range(n):
            if dp[i][j] == float("inf"):
                row.append(" INF ")
            else:
                row.append(f"{dp[i][j]:6.2f}")
        print(" ".join(row))
    print("================\n")


# --------- MAIN ---------
def main():
    # Read file
    with open("lab6/testcase/4.txt", "r") as f:
        lines = f.read().strip().splitlines()

    n = int(lines[0])
    points = []

    for i in range(1, n + 1):
        x, y = map(float, lines[i].split())
        points.append((x, y))

    # 1) Sort points into proper polygon order
    poly = sort_points_as_polygon(points)

    print("Ordered polygon points (CCW):")
    for p in poly:
        print(p)

    # 2) Run DP triangulation
    dp = min_triangulation_dp(poly)

    # 3) Print DP Table
    print_dp_table(dp)

    # 4) Final answer
    print(f"Minimum triangulation cost = {dp[0][n-1]:.4f}")


if __name__ == "__main__":
    main()
