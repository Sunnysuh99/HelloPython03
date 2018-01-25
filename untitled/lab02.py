

#19. 윤년계산 (2012년은 윤년)
year = int(input('알고싶은 윤년 년도를 입력하세요'))
if((year % 4 == 0 and year %100 != 0) or (year % 400 == 0)):
    print('%d 는 윤년입니다' % year)
else:
    print('%d는 윤년이 아닙니다' % year)

#20. 복권 빌행
import random

lotto = str(random.randint(100, 999))
print(lotto)
lucky = str(input('복권 숫자 3자리를 입력하세요! \n'))

match = 0;

if lotto[0] == lucky[0] or lotto[0] == lucky[1] or lotto[0] == lucky[2]:
    match += 1
if lotto[1] == lucky[0] or lotto[1] == lucky[1] or lotto[1] == lucky[2]:
    match += 1
if lotto[2] == lucky[0] or lotto[2] == lucky[1] or lotto[2] == lucky[2]:
    match += 1

msg = '꽝이군요! 다음 기회에!'
if match == 3:
    msg = '모두 일치! 상금 1백만원!'
if match == 2:
    msg = '2개 일치! 상금 1만원!'
if match == 1:
    msg = '1개 일치! 상금 1천원!'

print(msg)

#21. 구구단 입력
number = int(input('1 - 9 숫자 하나를 입력하세요'))

if(lotto == a):
    print('축하합니다!! 상금 1백만원에 당첨되었습니다.')
else:
    print('잘못 입력하셨습니다.')

#22. 소문자 --> 대문자
if(lotto == a):
    print('')
else:
    print('잘못 입력하셨습니다.')

#23. 숫자 맞추기
num1 = int(input('1 - 100 사이의 숫자를 입력하세요'))
num2 = int number

if(num1 > num2):
    print('추측한 숫자가 큽니다')
if(num1 > num2):
    print('추측한 숫자가 작습니다')
if(num1 = num2):
    print('빙고, 숫자를 맞췄습니다')
if(num1 > num2 or num1 < num2):
    print('빙고, 숫자를 맞췄습니다')
else:
    print('1 - 100 사이의 숫자를 입력하세요')


#24. Multiplication Table


#25. 신용카드 조회 및 은행정보 출력

35(JCB카드)
3563 17 NH농협카드
3569 01 신한카드
3569 12 KB국민카드

4(비자카드)
4048 25 비씨카드
4386 76 신한카드
4579 73 국민은행

5(마스타카드, Maestro)
5155 94 신한카드
5243 53 외환카드
5409 26 국민은행

#26 주민등록번호 유효성 검사

