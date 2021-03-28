# [정올 234/Python] 함수3 - 형성평가4
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=134&sca=10d0

arr = [1, 2] # 수열 저장할 배열
def Arr(num):
    if num==0:
        print(arr[-1]) # 마지막 수 출력
    else: 
        arr.append((arr[-1]*arr[-2])%100) # 앞의 두 수의 곱 100으로 나눈 나머지 추가
        Arr(num-1) # 재귀적으로 반복

n = int(input())
Arr(n-2) # n-2번 수를 append 