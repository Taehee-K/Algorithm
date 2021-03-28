# [정올 166/Python] 배열2 - 형성평가7
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=66&sca=10a0

def get_arr():
    array = []
    line_1 = list(map(int, input().split()))
    line_2 = list(map(int, input().split()))
    array.append(line_1)
    array.append(line_2)
    return array


print("first array")
first = get_arr()
print("second array")
second = get_arr()

new = [[0]*3 for _ in range(2)]
for i in range(2):
    for j in range(3):
        new[i][j] = first[i][j] * second[i][j]
        print(new[i][j], end = " ")
    print()