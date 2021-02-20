# [정올 126/Python] 반복제어문1 - 형성평가2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=26&sca=1060

num = list(map(int, input().split()))

i = 0
even = 0
odd = 0
while (num[i]!=0):
    if num[i]%2==0: even+=1
    else: odd+=1
    i+=1
print("odd :", odd)
print("even :", even)