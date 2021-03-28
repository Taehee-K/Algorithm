# [정올 190/Python] 문자열2 - 형성평가2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=90&sca=10f0

words = ['flower', 'rose', 'lily', 'daffodil', 'azalea'] # 5개 단어 초기화
char = input().strip() # 한 개의 문자 입력받기
count = 0 # 출력한 문자 개수 저장할 변수
for word in words:
    if char[0] in word[1:3]: # 문자가 단어의 2, 3번째에 위치해 있을 때
        print(word)
        count+=1 
print(count)