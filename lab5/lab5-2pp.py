def min_coin_change_dp(amount, coins):
    n = len(coins)
    INF = float('inf')

    # dp[i][j] = จำนวนเหรียญน้อยที่สุด ที่ใช้ทอน j โดยใช้เหรียญ coins[0..i]
    dp = [[INF] * (amount + 1) for _ in range(n + 1)]

    # base case: amount = 0 ใช้เหรียญ 0
    for i in range(n + 1):
        dp[i][0] = 0

    # fill dp table
    for i in range(1, n + 1):
        coin = coins[i - 1]
        for j in range(1, amount + 1):
            # ไม่ใช้เหรียญ coin
            dp[i][j] = dp[i - 1][j]
            # ใช้เหรียญ coin อย่างน้อย 1 เหรียญ
            if j >= coin and dp[i][j - coin] + 1 < dp[i][j]:
                dp[i][j] = dp[i][j - coin] + 1

    # trace back 
    res = []
    i, j = n, amount
    while j > 0 and i > 0:
        if dp[i][j] == dp[i-1][j]:
            i -= 1  # !useeee
        else:
            res.append(coins[i-1])  # usesssssssss
            j -= coins[i - 1]

    return dp[n][amount], res[::-1], dp


with open("lab5/testcase/5.1.txt", 'r') as file:
    lines = file.readlines()

amount = int(lines[0].strip())
coins = list((map(int, lines[1].strip().split())))


min_coins, path, table = min_coin_change_dp(amount, coins)



# DP Table
print("\nDP Table (rows=coins used, cols=amount):")
header = ["Amt"] + [str(j) for j in range(amount + 1)]
print("  ".join(header))
for i in range(len(coins) + 1):
    row = [f"{coins[i-1]}" if i > 0 else "0"]
    for j in range(amount + 1):
        val = table[i][j]
        row.append(str(val if val != float('inf') else "∞"))
    print("  ".join(row))


print("\n=== Minimum Coin Change Problem (DP Table) ===")
print(f"Minimum coins needed = {min_coins}")
print(f"Coins used = {path}")