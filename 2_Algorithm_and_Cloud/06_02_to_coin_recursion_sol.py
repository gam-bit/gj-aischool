
def calc_coin_cnt(remained_money, now_idx, coins_list):
    
    if remained_money == 0:
        return 0

    now_coin_cnt, k = divmod(remained_money, coins_list[now_idx])

    return now_coin_cnt + calc_coin_cnt(k, now_idx-1, coins_list)

n, k = map(int, input().split())
coins_list = [] 
min_coin_cnt = 0

for _ in range(n):
    coins_list.append(int(input()))

print(calc_coin_cnt(k, len(coins_list) - 1, coins_list))