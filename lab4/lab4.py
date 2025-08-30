
#Brute Force
def brute_force(num_of_line, info):
    max_profit = 0
    buy_day = sell_day = 0
    buy_rate = sell_rate = 0.0
    
    for i in range(num_of_line):
        for j in range(i+1, num_of_line):
            profit = info[j] - info[i]
            if profit > max_profit:
                max_profit = profit
                buy_day = i + 1
                sell_day = j + 1
                buy_rate = info[i]
                sell_rate = info[j]
    holding_days = sell_day - buy_day

    return [buy_day, buy_rate, sell_day, sell_rate, max_profit, holding_days]

infos = [35.10,35.01,35.11,35.02,35.08,35.03,35.09,35.12,35.04,35.17,35.14,35.19,35.13,35.07,35.16,35.20,35.06,35.05,35.18,35.16]

brute_force(20, infos)
