# [정올 169/Python] 배열2 - 형성평가A
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=69&sca=10a0

arr = []
for i in range(3):  # 3 행의 대문자들 입력받기
    row = list(input().lower().split()) # lower() 함수 통해 소문자로 변환
    arr.append(row)

for i in range(3):
    for j in range(5):
        print(arr[i][j], end = " ")
    print()