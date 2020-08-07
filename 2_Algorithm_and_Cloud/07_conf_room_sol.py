n = int(input())
meet_list = []

for _ in range(n):
    meet_list.append(list(map(int, input().split())))

# 끝나는 시간으로 오름차순 정렬, 시작 시간으로 오름차순 정렬
meet_list.sort(key=lambda row: [row[1], row[0]]) 

result_meet_cnt = 1
book_end_time = meet_list[0][1]
book_meet_list = [meet_list[0]]

for idx in range(1, len(meet_list)):
    if book_end_time <= meet_list[idx][0]:
        book_end_time = meet_list[idx][1]
        result_meet_cnt += 1
        book_meet_list.append(meet_list[idx])

print(result_meet_cnt)
print(book_meet_list)