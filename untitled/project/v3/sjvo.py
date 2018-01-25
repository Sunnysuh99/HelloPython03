from datetime import datetime


class SungJuk:

   #생성자

   def __init__(self,name,kor,eng,mat):
       self.sjno = 0
       self.name = name
       self.kor = kor
       self.eng = eng
       self.mat = mat
       self.tot = 0
       self.avg = 0
       self.grd = '가'
       self.regdate = str(datetime.now())

   def to_str(self):
       fmt ='[%d %s %d %d %d %d %2.f %s %s]'
       return fmt % (self.sjno,self.name,self.kor,
                     self.eng,self.mat,self.tot,
                     self.avg,self.grd,self.regdate[:19]) # str로 선언후 [:19] 가능

   #부분정도 출력 - 번호,이름,국어,영어,수학,등록일
   def to_str_list(self):
       fmt = '[%d %s %d %d %d %s]'
       return fmt % (self.sjno, self.name, self.kor,
                     self.eng, self.mat, self.regdate[:10])

   # 전체 성적 조회
   def getSungJuk(self):
       str_list = []
       str_list.append('\n\n -= 전체 데이터 출력 =- \n')

       for sj in self.sjsrv.getSungJuk():
           #리스트 형태로 Return 된 결과를 for문으로 다시 하나씩 순환하며 출력
           str_list.append(sj)
       str_list.append('\n\n')

       print(''.join(str_list))

