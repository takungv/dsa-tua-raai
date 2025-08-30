
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

#divide_conquer
def divide_conquer(num_of_line, rate):

    def solve(price, left, right):
        if left == right :
            return (left, right, 0, price[left], price[right])
        
        mid = (left + right) // 2

        #solve left
        left_result = solve(price, left, mid)
        #solve right
        right_result = solve(price, mid+1, right)
        #cross
        min_left_idx = min(range(left, mid+1), key=lambda i: price[i])
        max_right_idx = max(range(mid+1, right+1), key=lambda i: price[i])
        cross_profit = price[max_right_idx] - price[min_left_idx]
        cross_result = (min_left_idx, max_right_idx, cross_profit, price[min_left_idx], price[max_right_idx])

        best = max([left_result, right_result, cross_result], key=lambda x: x[2])
        return best
    
    buy_idx, sell_idx, profit, buy_rate, sell_rate = solve(rate, 0, num_of_line-1)
    holding_day = sell_idx - buy_idx

    return [buy_idx+1, buy_rate, sell_idx+1, sell_rate, profit, holding_day]
                   

rates = [35.10,35.01,35.11,35.02,35.08,35.03,35.09,35.12,35.04,35.17,
         35.14,35.19,35.13,35.07,35.16,35.20,35.06,35.05,35.18,35.16]

#brute_force(20, rates)
print(divide_conquer(20, rates))
