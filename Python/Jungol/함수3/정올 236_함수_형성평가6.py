# [정올 236/Python] 함수3 - 형성평가6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=136&sca=10d0

answer = 1 # 최종 결과 저장할 변수 -> 곱해야 함으로 1로 초기화
def Digit(n):
    global answer
    if n<0: # range(len(mul)) 만큼 반복시
        print(answer) # 최종 결과 출력
        return # 함수 종료
    elif int(mul[n]) != 0: # 자리의 수가 0이 아닐 때
        answer *= int(mul[n]) # 결과값에 곱하기
        Digit(n-1) # 전 자리수에 대해 함수 재귀호출
    else: # 자리의 수가 0일 때
        Digit(n-1) # 이전 자리수에 대해 재귀함수 호출

x, y, z = map(int, input().split()) # 자연수 3개 입력
mul = str(x*y*z) # 수 곱하기 -> str로 형변환
Digit(len(mul)-1) # 자리수 만큼 재귀함수 반복
