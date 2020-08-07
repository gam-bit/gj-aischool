n = int(input())

conf_list = []

for _ in range(n):
    conf_list.append(list(map(int, input().split())))

conf_list.sort(key=lambda x: x[1], x[0]) # nlogn

max_conf_cnt = 1

first_conf = conf_list.pop(0) # n
end_time = first_conf[1]

for idx in range(len(conf_list)):
    
    conf = conf_list[idx]
    if end_time <= conf[0]:
        max_conf_cnt += 1
        end_time = conf[1]

print(max_conf_cnt)



        