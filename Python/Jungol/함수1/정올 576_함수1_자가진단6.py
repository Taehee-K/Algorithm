# [정올 576/Python] 함수1 - 자가진단6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=213&sca=10b0

def Exp(x, y, op):
    if op=='+':
        return x+y
    elif op=='-':
        return x-y
    elif op=='*':
        return x*y
    elif op=='/':
        return x//y # 정수 부분만 출력
    else: # 4칙연산 이외의 연산일 때
        return 0 # 0 반환

# 정수의 연산식 피연산자 2개와 연산자 1개 읽어들이기
x, op, y =input().split()
print(x, op, y, '=', Exp(int(x), int(y), op))