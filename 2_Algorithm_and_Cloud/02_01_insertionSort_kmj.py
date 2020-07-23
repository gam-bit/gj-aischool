# https://www.acmicpc.net/problem/2750


def insertionSort(N, array):
    for i in range(N):
        num = array[i]
        for j in range(i)[::-1]:
            if array[j] > num:
                array[i] = array[j]
                array[j] = num
                i = i-1
            else:
                break
        # print(array)
    return array



n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)

print("---Sort 후---")
for i in insertionSort(n, arr):
    print(i)

#==========================================================
print("="*20)
print(">> solution") # index를 사용

def insertionSort_sol(N, array):
    for i in range(len(array)):
        focus_idx = i
        while focus_idx >=1 and array[focus_idx-1] > array[focus_idx]:
            array[focus_idx-1], array[focus_idx] = array[focus_idx], array[focus_idx-1]
            focus_idx -= 1
    return array


n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    arr.append(a)
print("---Soltution Sort 후---")
for i in insertionSort_sol(n, arr):
    print(i)