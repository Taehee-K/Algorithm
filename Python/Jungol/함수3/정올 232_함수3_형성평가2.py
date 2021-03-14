# [정올 232/Python] 함수3 - 형성평가2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=132&sca=10d0

def Recursive(n):
    if n>0: # 전달받은 수가 0보다 클 때
        arr.append(n) # 넘겨받은 숫자 array에 append
        Recursive(n-2) #해당 숫자로부터 2를 빼준 숫자 함수에 넣어줌
    else: 
        arr.reverse() # 순서 바꾸어준다(오름차순으로)
        for i in arr: print(i, end = " ") # 출력
arr = []
n = int(input())
Recursive(n)