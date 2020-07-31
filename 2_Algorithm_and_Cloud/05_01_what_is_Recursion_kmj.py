# pass
def whatisRF(now_depth, max_depth):
    
    text1 = f'{"_"*4*now_depth}"재귀함수가 뭔가요?"\n'
    text2 = f'{"_"*4*now_depth}"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n'
    text3 = f'{"_"*4*now_depth}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n'
    text4 = f'{"_"*4*now_depth}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."\n'
    text5 = f'{"_"*4*now_depth}라고 답변하였지.\n'
    
    if now_depth == max_depth:
        answer = f'{"_"*4*now_depth}"재귀함수는 자기 자신을 호출하는 함수라네"\n'
        return text1 + answer + text5
    
    return text1 + text2 + text3 + text4 + whatisRF(now_depth+1, max_depth) + text5

n = int(input())

print(f'''어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
{whatisRF(0, n)}''')