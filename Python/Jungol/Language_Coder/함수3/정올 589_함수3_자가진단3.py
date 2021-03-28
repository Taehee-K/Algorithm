# [정올 589/Python] 함수3 - 자가진단3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=226&sca=10d0
 
def Recursive(n):
    if n>0:
        return n + Recursive(n-1)
    else: return 0
    # TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
    # 오류 난 이유: n<=0 일 때 return 값이 없어서(NoneType)
 
n = int(input())
print(Recursive(n))