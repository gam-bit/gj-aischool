# pass

def trans_base_rf(n, b):
    alpha_to_num = {'A':10, 'B':11, 'C':12, 'D':13,
                    'E':14, 'F':15, 'G':16, 'H':17,
                    'I':18, 'J':19, 'K':20, 'L':21,
                    'M':22, 'N':23, 'O':24, 'P':25,
                    'Q':26, 'R':27, 'S':28, 'T':29,
                    'U':30, 'V':31, 'W':32, 'X':33,
                    'Y':34, 'Z':35}

    q = n // b
    r = n % b
    if r >= 10:
        r = [k for k, v in alpha_to_num.items() if v == r][0]
    
    if n < b:
        if n >= 10:
            return [k for k, v in alpha_to_num.items() if v == n][0]
        else:
            return str(n)

    return trans_base_rf(q, b) + str(r)


n, b = map(int, input().split())

print(trans_base_rf(n, b))
