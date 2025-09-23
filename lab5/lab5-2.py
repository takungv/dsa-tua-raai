def min_coins_chang(coins, N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0

    for amount in range(1, N + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])

    amount = N
    used_coins = []
    while amount > 0:
        for coin in coins:
            if coin <= amount and dp[amount] == 1 + dp[amount - coin]:
                used_coins.append(coin)
                amount -= coin
                break

    return dp[N], used_coins


#----------------อ่านไฟล์----------------
with open("lab5/testcase/5.10.txt", 'r') as file:
    lines = file.readlines()

N = int(lines[0].strip())
coins = list((map(int, lines[1].strip().split())))


min_coins, uses_coins = min_coins_chang(coins, N)
print(uses_coins)
print(min_coins)