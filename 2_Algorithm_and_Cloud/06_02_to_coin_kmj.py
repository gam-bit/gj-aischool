n, money = map(int, input().split())

coin_list = [] # 오름차순으로
for i in range(n):
    coin = int(input())
    coin_list.append(coin)

coin_list = coin_list[::-1]

coin_cnt = 0
for coin in coin_list:
    coin_cnt += money // coin
    money %= coin

print(coin_cnt)
