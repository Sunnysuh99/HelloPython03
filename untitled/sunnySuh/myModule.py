# 모듈 사용하기
# 프로그램을 구성하는 독립적인 단위를 각각 정의하고 관라히는 방법
# 자주 사용하는 일반적인 기능을 모듈로 만들어주면 필요시 활용할 수 있다.
# 모듈: 관련성  있는 데이터들, 함수, 클래스

# 모듈을 사용하려면 import 명령으로 Interpriater에게 사용여부를 알려야 한다. (import random)

# import sunny  # 사용자 모듈

# import random
# import random as r  # 별칭으로 줄여쓰기
from random import randint # 모듈명을
# import lab03     #우리가 작성한 함수가 있는 화일
from math import pi, sqrt # 강추!
# from math import * # 쓰기 편하지만 읽기가 불편
# import sunny  # 내 모듈

# 모듈을
# from builtins import print

# print(random.randint(1,10))
# print(math.pi)
# print(math.sqrt(9))
# print(random.randint(1,10)

randint(1,10))
pi
sqrt(9)

# 모듈 호출시 이름을 별칭으로 바꿔 정의한다
# import 모듈이름 as 별칭

# 함수 호출시 모듈명까지 기술하는 것은 왠지 불편함
# from 모듈면 import 함수명

# 사용자가 만든 모듈을 다른 파일에서 참조하려면 두 파일이 모두 같은 위치에 잇어야 함.
# 즉, 프로잭트 내에서 서로 참조하려면 이 파일들은 같은 위치에 저장되어 있어야 함.

# 한편, python IDE나 다른 프로잭트에서 모듈을 참조하려면 pathonPath가 정의한 위치에 모듈을 저장해둔다
# 파이썬 설치위치나 '파이썬설치위치/lib'

# sunny.isLeapYear()

# 파이썬 패키지: 다수의 개발자가 만든 모듈의 이름이 서로 같을 경우 파이썬에서는
# '패키지'라는 개념을 이용해서 해결.
# . 연산자를 이용해서 모듈을 계층적(디렉토리)으로 관리 파이선에서 디랙토리가 패키지가
# 인식되려면  __int_.py가 있어야 함.



from sunnySuh.hello import sayHello

sayHello()

#성적  데이터 클래스
class SungjukV0:
    def __init__(self, name, kor, eng, mat):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat

#성적 처리용 클래스
class SungjukService:
    def getTotal(self, sj):
        tot = sj.kor + sj.eng + sj.mat
        return tot

    def getAverage(self, sj):
        avg = self.getTotal(sj) / 3
        return avg

    def getGrade(self, sj):
        grdlist = '가가가가가가미양우수수'
        var = int(self.getAverage(sj)/10)
        grd = grdlist[var]
        return grd

sjsrv = SungjukService()
sj1 = SungjukV0('미현', 100, 200, 100)
print(sj1.name)
print(sj1.kor)
print(sj1.eng)
print(sj1.mat)

print(sjsrv.getTotal(sj1))
print(sjsrv.getAverage(sj1))
print(sjsrv.getGrade(sj1))
