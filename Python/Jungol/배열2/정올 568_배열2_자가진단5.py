# [정올 568/Python] 배열2 - 자가진단5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=205&sca=10a0

first = [] # 첫 번째 배열 저장할 리스트
second = [] # 두 번째 배열 저장할 리스트

def save(table): # 입력값 배열에 저장해주는 함수
    line_1 = list(map(int, input().split()))
    line_2 = list(map(int, input().split()))
    table.append(line_1)
    table.append(line_2)

save(first) # first 배열에 저장
save(second)

print("first array")
print("second array")
for i in range(2):
    for j in range(4):
        print(first[i][j]*second[i][j], end=" ")
    print()