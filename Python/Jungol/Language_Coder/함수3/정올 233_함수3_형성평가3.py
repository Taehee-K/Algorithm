# [정올 233/Python] 함수3 - 형성평가3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=133&sca=10d0

## 시간초과 오류 남.. 
value = [0]*10 # N 10 보다 작은 수 -> 주사위 던졌을 때 나온 값 저장
index = 0 # 주사위 던진 횟수
def Dice(N, M):
    global value
    global index
    for i in range(1, 7): # 1~6 주사위
        value[index] = i # 현재 index i로 낮춤
        if(index == (N-1)): # 주사위 N번 던졌을 때 
            total = sum(value[:N])  # 던진 값들의 합 구하기
            if (total == M): # 합이 M과 같을 때
                for k in range(N): # 주사위 N번 던졌을 때의 값 구하기
                    print(value[k], end = " ")
                print()
                return
        else: # 주사위 던진 횟수 < N일 때
            index+=1 # 인덱스 증가
            Dice(N,M) # 재귀 호출
            index-=1 # 6번 다 반복 시 인덱스 감소

N, M = map(int, input().split())
Dice(N, M)