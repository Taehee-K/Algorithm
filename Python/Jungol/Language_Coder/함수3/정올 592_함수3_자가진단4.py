# [정올 592/Python] 함수3 - 자가진단4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=229&sca=10d0
 
def Recursive(n):
    if n==0: return 0
    return (n%10)**2 + Recursive(n//10)

n = int(input())
print(Recursive(n))