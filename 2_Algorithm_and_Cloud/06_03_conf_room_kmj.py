# 1931번
# 시간초과 -- solution보고 고쳐서 pass함. 아래 코드는 pass 못한 코드.
# idea는 ok, 코드 최적화가 문제
# import sys
# input = sys.stdin.readline

n = int(input())

conf_list = []
for _ in range(n):
    conf_list.append(list(map(int, input().split())))
    
conf_list = sorted(conf_list, key=lambda x: x[1]) ## --[x[1], x[0]]
# print(conf_list)

max_conf_cnt = 0 
# selected_conf_list = []

while conf_list:
    selected_conf = conf_list.pop(0)
    # selected_conf_list.append(selected_conf)
    max_conf_cnt += 1

    removed_conf = []
    for conf in conf_list:  ## --idx로 돌려야 함
        end_time = selected_conf[1]
        start_new_time = conf[0]
        if end_time > start_new_time:
            removed_conf.append(conf)
    
    conf_list = [x for x in conf_list if x not in removed_conf]

print(max_conf_cnt)
# print(selected_conf_list)