# [정올 193/Python] 문자열2 - 형성평가5
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=93&sca=10f0

words = [input() for _ in range(5)] # 5개의 단어 입력
char = input().strip() # 문자 입력
string = input().strip() # 문자열 입력
count = 0 # 출력된 단어 수
for word in words:
    if char in word or string in word: # 문자나 문자열 단어에 있을 시
        print(word) # 단어 출력
        count +=1
if count==0: print('none') # 해당하는 단어 없을 시 'none'출력