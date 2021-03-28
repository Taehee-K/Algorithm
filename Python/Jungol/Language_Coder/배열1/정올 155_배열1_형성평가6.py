# [정올 155/Python] 배열1 - 형성평가6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=55&sca=1090

char = ['J', 'U', 'N', 'G', 'O', 'L']

letter = input()
if letter[0] in char: # check whether it exists in list
    for i in range(len(char)):
        if letter[0]==char[i]:
            print(i)
else:
    print("none")