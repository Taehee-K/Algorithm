# [정올 529/Python] 선택제어문 - 자가진단2
# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=166&sca=1050
 
# 비만수치 공식: “몸무게+100-키”
# 키와 몸무게를 자연수로 입력
height, weight = map(int, input().split())
ob = weight+100-height

# 첫 번째 줄에 비만수치를 출력
print(ob)
# 비만수치가 0보다 크면 비만("Obesity")이라는 메시지를 출력
if(ob>0): print("Obesity")