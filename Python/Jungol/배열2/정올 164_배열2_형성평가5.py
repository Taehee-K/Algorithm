# [정올 164/Python] 배열2 - 형성평가5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=64&sca=10a0

class_tot = [] # 각 반별 합산 점수 저장할 list

for i in range(4):
    num = list(map(int, input("{}class? ".format(i+1)).split()))
    total = 0
    for j in range(3):
        total+=num[j]
    class_tot.append(total)

for i in range(4):
    print("{}class : {}".format(i+1, class_tot[i]))
