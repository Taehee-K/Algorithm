# [정올 590/Python] 함수3 - 자가진단5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=227&sca=10d0

# 다른 분의 코드를 참고해서 다시 한 풀이.. (사실 아직도 잘 모르겠다)
def output():
    for i in range(1, n+1): # arr 에 저장되어 있는 값 n 개 만큼 출력
        print("%d"%(arr[i]), end = " ")
    print()

def Case(level): # 주사위를 n 번 던졌을 때
    if n < level : # n 보다 레벨 값이 크다면 
        output()   # 값 출력
        return
    for i in range(arr[level-1], 7): # 이전 레벨의 값 ~6까지
        arr[level] = i  # 현재 레벨에 담을 값 이전 레벨에 담겨있는 값으로 
        Case(level +1)  # 레벨 증가시켜 재귀적으로 함수 호출

arr = [0]*100
arr[0]=1

n = int(input()) # 주사위 던진 횟수 입력받기
Case(1) # 현재 레벨 1로 지정해 Case 시작