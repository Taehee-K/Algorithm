# [정올 235/Python] 함수3 - 형성평가5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=135&sca=10d0

count = 0 # 연산 횟수 세주는 변수 
def Calc(n):
    global count # 연산 횟수 세기
    if n==1: # n==1일 때
        print(count) # 이제까지의 연산 횟수 출력
    elif n%2==0: # 짝수일 때
        count+=1 # 연산 횟수 증가
        Calc(n//2) # 2로 나누기
    else:
        count+=1 # 연산 횟수 증가
        Calc(n//3) # 3으로 나누기
        
n = int(input())
Calc(n)