# [정올 167/Python] 배열2 - 형성평가8
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=67&sca=10a0

arr = []
for i in range(4): 
    arr.append(list(map(int, input().split())))

total = 0
for i in range(4): # get sum of each row
    r_tot = 0 
    for j in range(2):
        r_tot+=arr[i][j]
        total+=arr[i][j]
    print(r_tot//2, end = " ")

print()
for j in range(2): # get sum of each column
    c_tot = 0   
    for i in range(4):
        c_tot += arr[i][j]
    print(c_tot//4, end = " ")

print("\n{}".format(total//8))

