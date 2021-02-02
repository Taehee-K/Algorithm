#정올 1086
#성적 관리 프로그램

#해당 과목의 점수(0~100)입력
#입력 값 해당 범위 만족하지 않을 경우 그 점수만 다시 입력받음
#하나의 출력 마친 후 프로그램 종료

#국어, 영어, 수학, 물리, 화학, 사회, 컴퓨터 점수
#총점, 평균, 최대 점수, 최소 점수
#평균은 정수로 출력, 소수점 버림
#출력 후 값들 기준으로 막대그래프로 표현(과목별 점수, 평균, 최대점수, 최소점수)
#막대그래프 -> 10점당 '*'으로 표현, 10의 단위 이하 자리숫자 고려X
#그래프 그릴 시, 각 과목에 해당하는 값 영문자로 대
#평균: H, 최대점수: I, 최소점수: J

grade = input().split()
total = 0
maximum = 0
minimum = 100
#점수 정수형으로 변환
for i in range(len(grade)):
grade[i] = int(grade[i])
total+= grade[i]
if(maximum<grade[i]): maximum = grade[i]
if(minimum>grade[i]): minimum = grade[i]

avg = total//len(grade)

print("TOT :", total)
print("AVG :", avg)
print("MAX :", maximum)
print("MIN :", minimum)

##for i in range(len(grade)):
##    grade[i] = (grade[i]//10)*10
##    print(grade[i], end = ' ')
##print()

for i in range(10):
print("%3d" %(100-10*i), end = '  ')
for j in range(10):
if (j<len(grade) and grade[j]>=(100-10*i)): print(' * ', end = ' ')
elif (j==len(grade) and avg>=(100-10*i)): print(" * ", end = ' ')
elif (j==len(grade)+1 and maximum>=(100-10*i)): print(" * ", end = ' ')
elif (j==len(grade)+2 and minimum>=(100-10*i)): print(" * ", end = ' ')     
else: print('   ', end = ' ')
print()
print("      A   B   C   D   E   F   G   H   I   J")
    
