# [정올 591/Python] 함수3 - 자가진단6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=228&sca=10d0

def Recursive(num):
    if num > N: # num 값이 수의 개수보다 클 때
        print(arr[num-1]) # num-1 인덱스의 숫자 출력 (배열의 마지막 수)
        return
    arr.append(arr[num//2] + arr[num-1]) # num번째 인덱스에 수 추가
    Recursive(num+1) # 재귀적으로 함수 호출
    

N = int(input()) 
arr = [1, 1] # arr[1] = 1
Recursive(2)