# 둘 다 pass

def trans_to_deci(n, b):
    alpha_to_num = {'A':10, 'B':11, 'C':12, 'D':13,
                    'E':14, 'F':15, 'G':16, 'H':17,
                    'I':18, 'J':19, 'K':20, 'L':21,
                    'M':22, 'N':23, 'O':24, 'P':25,
                    'Q':26, 'R':27, 'S':28, 'T':29,
                    'U':30, 'V':31, 'W':32, 'X':33,
                    'Y':34, 'Z':35}

    m = len(n)
    result = 0
    for i in range(m):
        try:
            result += int(n[i]) * (b**(m-i-1))
        except:
            result += alpha_to_num[n[i]] * (b**(m-i-1))
        
    return result 
    



[n, b] = input().split()

b = int(b)

    
print(trans_to_deci(n, b))


#--------------------------
# 재귀 이용
def trans_to_deci_rf(n, b, k):
    alpha_to_num = {'A':10, 'B':11, 'C':12, 'D':13,
                    'E':14, 'F':15, 'G':16, 'H':17,
                    'I':18, 'J':19, 'K':20, 'L':21,
                    'M':22, 'N':23, 'O':24, 'P':25,
                    'Q':26, 'R':27, 'S':28, 'T':29,
                    'U':30, 'V':31, 'W':32, 'X':33,
                    'Y':34, 'Z':35}

    m = len(n) 
    if k == m-1:
        try:
            return int(n[-1])
        except:
            return alpha_to_num[n[-1]]
    
    else:
        try:
            result = int(n[k]) * (b**(m-k-1))
        except:
            result = alpha_to_num[n[k]] * (b**(m-k-1))


    return  result + trans_to_deci_rf(n, b, k+1)

[n, b] = input().split()

b = int(b)

print(trans_to_deci_rf(n, b, 0))

    