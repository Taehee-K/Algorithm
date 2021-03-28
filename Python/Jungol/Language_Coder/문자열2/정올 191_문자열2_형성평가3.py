# [정올 191/Python] 문자열2 - 형성평가3
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=91&sca=10f0

words = []
while True:
    word = input()
    if word == "0":
        break
    else:
        words.append(word)
print(len(words)) # 입력 받은 단어 개수 출력
for i in range(len(words)):
    if i%2==0: # 홀수 번째 단어 출력
        print(words[i])