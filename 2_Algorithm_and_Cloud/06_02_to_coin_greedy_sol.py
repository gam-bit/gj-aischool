n, k = map(int, input().split())
coin_list = [] 
min_coin_cnt = 0

for _ in range(n):
    coin_list.append(int(input()))


for coin in reversed(coin_list):
    min_coin_cnt += k // coin
    k %= coin

print(min_coin_cnt)
