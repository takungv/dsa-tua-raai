def coin_change_ways(coins, N):
    result = []

    def backtrack(remaining, combo, start):
        if remaining == 0:
            result.append(list(combo))  # เจอวิธีสำเร็จ
            return
        for i in range(start, len(coins)):
            if coins[i] <= remaining:
                combo.append(coins[i])
                backtrack(remaining - coins[i], combo, i)  # ใช้ i เพื่ออนุญาตใช้เหรียญซ้ำ
                combo.pop()  # ลบเหรียญออกก่อนลองตัวถัดไป

    backtrack(N, [], 0)
    return result

with open("lab5/testcase/5.14(Extra).txt", 'r') as file:
    lines = file.readlines()

N = int(lines[0].strip())
coins = list((map(int, lines[1].strip().split())))

ways = coin_change_ways(coins, N)

for w in ways:
    print(w)
print(f"Total ways: {len(ways)}")