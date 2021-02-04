# [정올 105/Python] 출력 - 형성평가5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=5&sca=10

seoul = ['Seoul', '10,312,545', "+91,375"]
pusan = ['Pusan', '3,567,910', "+5,868"]
incheon = ['Incheon', '2,758,296', '+64,888']
daegu = ['Daegu', '2,511,676', '+17,230']
gwangju = ['Gwangju', '1,454636', '+29,774']

list = [['Seoul', '10,312,545', "+91,375"],['Pusan', '3,567,910', "+5,868"],
['Incheon', '2,758,296', '+64,888'],['Daegu', '2,511,676', '+17,230'],
['Gwangju', '1,454636', '+29,774']]

for i in range(5):
    for j in range(3):
        print("{:>15}".format(list[i][j]), end = '')
    print()