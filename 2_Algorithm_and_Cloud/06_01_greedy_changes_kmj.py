# 5585번



def num_changes(price, coins_list):
    total_num = 0
    balance = 1000 - price
    for coin in coins_list:
        # if balance >= coin: # 안 써도 됨
            total_num += balance // coin
            # balance -= (balance // coin) * coin
            balance %= coin
    
    return total_num



p = int(input())

coins = [500, 100, 50, 10, 5, 1]
print(num_changes(p, coins))