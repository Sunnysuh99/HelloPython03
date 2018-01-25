
# 성적 처리프로그램 V1
name = input('이름을 입력하세요\n')
kor = int(input('국어 점수를 입력하세요\n'))
eng = int(input('영어 점수를 입력하세요\n'))
mat = int(input('수학 점수를 입력하세요\n'))

def getTotal(kor, eng, mat):
   return kor + eng + mat

def getAverage(tot):
   return tot / 3

def getGrade(avg):
   grd = '가'
   if avg >= 90:
       grd = '수'
   elif avg >= 80:
       grd = '우'
   elif avg >= 70:
       grd = '미'
   elif avg >= 60:
       grd = '양'
   return grd

tot = getTotal(kor, eng, mat)
avg = getAverage(tot)
grd = getGrade(avg)

print('%s %d %d %d %d %.2f %s' % (name, kor, eng, mat, tot, avg, grd))


def getTotal(kor, eng, mat):
    tot = kor + eng + mat
    return tot

def getAverage(tot):
    pass  # pass: DummyCode
    avg = getTotal()/3
    return avg

def getGrade():
   avg = getAverage()
   grd = '가'
   if avg >= 90:
       grd = '수'
   elif avg >= 80:
       grd = '우'
   elif avg >= 70:
       grd = '미'
   elif avg >= 60:
       grd = '양'
   return grd


print('--성적처리 프로그램v2--')
name = input('이름을 입력하세요\n')
kor = int(input('국어 점수를 입력하세요\n'))
eng = int(input('영어 점수를 입력하세요\n'))
mat = int(input('수학 점수를 입력하세요\n'))

fmt = '%s %d %d %d %d %.2f %s'
print(fmt % (name, kor, eng, mat, getTotal(), getAverage(), getGrade()))

# 이름 짖기
# 파스칼 표기법: 첫 단어의 첫머리를 대문자로 (Employees, Departments, InfraStructure, JoinMember) - Class 작명 時
# 카멜 표기법: 두개의 단어중 첫단어를 소문자로 시작, 두번째 단어 첫머리를 대문자로(registerEmployee) -
# 스네이크 표기법: 소문자와 기호를 이용하여 작명 (somthing_special, time_table) - 변수
# 헝가리언 표기법: 자료형을 의미하는 접두사를 이용해서 작명 (strName, isMarried, boolMarried)

## 함수로 재 작성 하기

#8. 자취방 가성비
def comparaRoom(width, height, price):
    return (width * height)/price

roomA = comparaRoom(2.5, 3, 27)
roomB = comparaRoom(4, 2, 30)

if (roomA > roomB):
    print('방 A가 더 낫네요')

else:
    print('방 A가 더 낫네요')


#10 선박 중공업 순익계산 - 도메인 문제(지문만으로 해결할 수 없음, 배경지식 필요)
# 가변 자본 = 15, 불변자본 = 30, 잉여가치 = 45
# 이윤율 = 잉여가치 / (불변자본/+가변자본)

def computeProfit():
    c = int(input('불변자본을 입력하세요'))    # c: constant capital
    v= int(input('가변자본을 입력하세요'))     # v: variable capital
    s = int(input('잉여가치액을 입력하세요'))  # surplus value

    return (c + v) / s

print(computeProfit())


#11. 노트북 구매
  # 달라: 1071, 유로화: 1309

def getExchangeRate(country):
    rate = 0
    if country == 'us':
        rate = 1071
    elif country == 'euro':
        rate = 1309
    return rate

buyUS = 780 * getExchangeRate('us')
buyEuro = 650 * getExchangeRate('euro')

if buyUS > buyEuro:
    print('유로화로 구입하면 더 쌉니다')
else:
    print('달라로 구입하면 더 쌉니다')



#12. 운동장 둘레 계산
   # 원둘레 계산식 pi * 지름

def howManyRun(radius):
    pi = 3.14
    return radius * pi

studentA = howManyRun(100)
studentB = howManyRun(90)

print('학생A는 학생B 보다 %d m만큼 더 달린다' \
          % (studentA - studentB ))


#17. 사칙연산프로그램 - input 함수 이용

def intCalu():
    num1 = int(input('좌변값 정수를 입력하세요'))
    num2 = int(input('우변값 정수를 입력하세요'))

    fmt = "%d + %d \n %d = %d \n"
    fmt += "%d + %d \n %d = %.5f \n"
    fmt += "%d + %d = %d"

    print(fmt % (num1, num2, num1 + num2, \
                 num1, num2, num1 - num2, \
                 num1, num2, num1 * num2, \
                 num1, num2, num1 / num2, \
                 num1, num2, num1 ** num2))
intCalu()

# 연봉 세금 산출
def computeTax():
   salary = int(input('연봉을 입력하세요\n'))
   isMarried = input('결혼여부를 입력하세요 (Y/N)\n')
   tax = 0;

   if isMarried.upper() == 'N':
       if salary < 3000:
           tax = salary * 0.1
       else:
           tax = salary * 0.25
       isMarried = "아니오"
   else:
       if salary < 6000:
           tax = salary * 0.1
       else:
           tax = salary * 0.25
       isMarried = "예"

   fmt = "연봉 : %d, 결혼여부 : %s, 세금 : %.1f"
   print( fmt % (salary, isMarried, tax) )

computeTax()

#19. 윤년계산 (2012년은 윤년)

def isLeapYear():
    year = int(input('윤년여부를 알고 싶은 년도를 입력하세요'))
    isleap = '윤년이 아닙니다'

    if((year % 4 == 0 and year %100 != 0) or (year % 400 == 0)):
    isleap = '윤년입니다'

    print("%d는 %s" % (year, isleap))

isLeapYear()

#20. 복권 당첨

import random
def rouletteLotto():
   lotto = str(random.randint(100, 999))
   lucky = input('복권번호를 입력하세요\n')
   match = 0  # 일치여부

   for i in [0,1,2]:
       for j in [0,1,2]:
           if (lucky[i] == lotto[j]):
               match += 1

   if match == 3:
       prize = '1등 당첨! 상금 백만원!'
   elif match == 2:
       prize = '2등 당첨! 상금 만원!'
   elif match == 1:
       prize = '3등 당첨! 상금 천원!'

   print(lucky, lotto, prize)

rouletteLotto()