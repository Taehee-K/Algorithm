# [정올 194/Python] 문자열2 - 형성평가6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=94&sca=10f0

A, B, n = input().split() # 문자열 A, B, 정수 n 입력
n = int(n) # n 정수로 변환
A += B # A에 B 연결 
B = A[:n]+B[n:] #A에서 n개의 문자를 B에 복사
print(A)
print(B)