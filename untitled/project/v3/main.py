import sys
from . import sjvo, sjsrv


class SungJukV3Main :

   # 성적 처리서비스 객체 생성
   sjsrv = sjsrv.SungJukService()

   # 메뉴 표시
   def displayMenu(self):
       str_list = []
       str_list.append(' -= 성적 처리 프로그램v3 =-\n\n')
       str_list.append('**********************\n')
       str_list.append('1 : 새로운 성적데이터 추가 \n')
       str_list.append('2 : 전체 성적데이터 조회 \n')
       str_list.append('3 : 상세 성적데이터 조회 \n')
       str_list.append('4 : 성적 데이터 수정 \n')
       str_list.append('5 : 성적 데이터 삭제 \n')
       str_list.append('0 : 성적처리 프로그램 종료 \n')
       str_list.append('**********************\n\n')
       str_list.append('실행할 작업을 선택하세요 >>')

       print(''.join(str_list))

   #메뉴 분기에 따른 함수 정의
   def newSungJuk(self):
       str_list = []
       str_list.append('\n\n 추가할 성적데이터를 입력')
       str_list.append('\n\n 데이터 입력순은 이름/국어/영어/수학 순')
       str_list.append('\n\n 예) 수지 99 55 66')

       print(''.join(str_list))

       n, k, e, m = input('').split()
       #성적데이터 한줄로 공백을 활용해서 입력

       #입력받은 성적데이터로 성적 객체 생성
       sj = sjvo.SungJuk(n, int(k), int(e), int(m))

       #성적객체 추가함
       self.sjsrv.addSungJuk(sj)

       print('\n\n 성적데이터가 추가되었습니다!! \n\n')


   def showSungJuk(self):
       def getSungJuk(self):
           str_list = []
           str_list.append('\n\n -= 전체 데이터 출력 =- \n')

           for sj in self.sjsrv.getSungJuk():
               # 리스트 형태로 Return 된 결과를 for문으로 다시 하나씩 순환하며 출력
               str_list.append(sj)
           str_list.append('\n\n')

           print(''.join(str_list))

   def showOneSungJuk(self):
       no = input('\n 검색할 학생번호 입력 \n>>')

       str_list = []
       str_list.append('-= 상세 성적데이터 =- \n')
       str_list.append(self.sjsrv.getOneSungJuk(int(no)))
       str_list.append('\n\n')


       print(''.join(str_list))

   def updateSungJuk(self):
       no = input('수정할 학생의 번호 입력하세요\n>>')

       str_list = []
       str_list.append('\n\n 수정할 성적데이터를 입력')
       str_list.append('\n\n 데이터 입력순은 이름/국어/영어/수학 순')
       str_list.append('\n\n 예) 수지 99 55 66')
       print(''.join(str_list))

       n, k, e, m = input('').split()
       sj = sjvo.SungJuk(n, int(k), int(e), int(m))
       sj.sjno = int(no)  # 수정할 번호 설정

       self.sjsrv.modifySungJuk(sj)
       print('\n\n 수정 완료!! \n\n')

   def deleteSungJuk(self):
       str_list = []
       no = input('삭제할 성적번호를 입력하세요\n>>')

       self.sjsrv.removeSungJuk(int(no))

       print('\n\n 삭제 성공!!\n\n')

   def exitSungJuk(self):
       sys.exit(True)

   # 파이썬 자료구조중 dictionary를 이용해서
   # 메뉴 분기시 실행할 함수를 객체형태로 저장
   menus = {'1':newSungJuk,'2':showSungJuk,
            '3':showOneSungJuk,'4':updateSungJuk,
            '5':deleteSungJuk,'0':exitSungJuk}



   # 메뉴 선택후 처리
   def selectMenu(self):
       menu = input('')
       # if (menu == 1 ) newSungJuk()
       # elif (menu == 2 ) showSungJuk()
       # elif (menu == 3 ) showOneSungJuk()
       # elif (menu == 4 ) updateSungJuk()
       # elif (menu == 5 ) deleteSungJuk()
       # elif (menu == 0 ) exitSungJuk()
       self.menus[menu](self)

