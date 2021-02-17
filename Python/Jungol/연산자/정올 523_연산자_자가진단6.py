# [정올 523/Python] 연산자 - 자가진단6
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=160&sca=1030

x, y = map(int, input().split())

if x>y:
    print(x,'>',y,'---',1)
else:
    print(x,'>',y,'---',0)

if x<y:
    print(x,'<',y,'---',1)
else:
    print(x,'<',y,'---',0)

if x>=y:
    print(x,'>=',y,'---',1)
else:
    print(x,'>=',y,'---',0)

if x<=y:
    print(x,'<=',y,'---',1)
else:
    print(x,'<=',y,'---',0)
