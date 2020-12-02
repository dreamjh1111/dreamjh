def one():
  print("a")
  B=int(input("what your number? \n"))
  if B==1:
    print("one")
  elif B==2:
    print("two")
  else:
    print("what ever")
#one함수는 선택지를 불러오는 함수입니다.

nowYear = 2020
def GetBirthYear(age):
  return nowYear-age
memberName="홍종혁"
memberBirth=GetBirthYear(25)
#print(memberName,"님이 태어난 년도는",memberBirth,"년입니다.")
#GetBirthYear함수는 태어난 년도를 알려주는 함수입니다.

def GetMemberInfo(name,age,sex):
  print(name,"님은",age,"세이고",sex,"입니다.")
#GetMemberInfo("홍종혁","26","남자")
#GetMemberInfo함수는 이름,나이,성별을 알려주는 함수입니다.

def Hello(name):
  print("안녕하세요?",name,"님, 즐거운 하루 되세요!")
#Hello("dreamjh")
#Hello함수는 로그인 인사 함수입니다.

def npc():
  status = "휴식"
  status = input("현재 상태를 입력하세요(휴식/벌목/목재판패)")
  time=int(input("시간을 입력하세요"))
  if status=="휴식":
    if time>=9 and time <17:
      status="벌목"
  if status=="벌목":
    if time>=17 and time<18:
      status="목재판매"
  if status=="목재판매":
    if time>=18:
      status="휴식"
  print("현재 상태 :",status)
#npc함수는 농부npc 함수입니다.

def login():
  a=None
  passward="1234"
  print(" ---------------------------------")
  print("|                                 |")
  print("|    jonghyuck 님 환영합니다.     |")
  print("|      암호를 입력해 주세요.      |")
  print("|                                 |")
  print(" ---------------------------------")
  a=input("passward  :  ")
  if a==passward:
    print("로그인 성공")
  else:
    print("로그인 실패")
#login함수는 로그인 아이디를 쳐야 들어가지는 함수입니다.

def quiz():
  answer="사람"
  question="아침에 하나, 점심에는 둘, 저녁에는 세개인 것은?"
  print(question)
  user_answer=input("답을 입력하시오")

  if user_answer==answer:
    print("정답입니다.")
  else:
    print("오답입니다.")
#quiz함수는 문제를 내는 함수입니다.

def calculator(): 
  def sum(a, b):
	  return a + b
  def sub(a, b):
    return a - b
  def mul(a, b):
    return a * b
  def div(a, b):
    return a / b
  first = int(input("#첫번째 피연산자를 입력하세요.\n"))
  second = int(input("#두번째 피연산자를 입력하세요.\n"))
  while (1):
    print("# 계산기 메뉴")
    print("# [1] 더하기")
    print("# [2] 빼기")
    print("# [3] 곱하기")
    print("# [4] 나누기")

    menu = input("#메뉴를 선택하세요\n")

    if (menu == "1"):
      print("더하기 메뉴를 선택하셨습니다.")
      print("result:", sum(first, second))
    elif (menu == "2"):
      print("빼기 메뉴를 선택하셨습니다.")
      print("result:", sub(first, second))
    elif (menu == "3"):
      print("곱하기 메뉴를 선택하셨습니다.")
    elif (menu == "4"):
      print("나누기 메뉴를 선택하셧습니다.")
      print("result:", div(first, second))
    elif (menu == "5"):
      print("계산기를 종료합니다.")
      break
    else:
      print("잘못된 메뉴를 선택하셨습니다.")
#calculator함수는 계산기 함수입니다.

def pinokio():
  time=0
  item=False
  nose=0
  while (1):
    ans=input("어디로 가시겠습니까 [마을/시장]")
    if ans == "마을":
      print("이야기1")
      time = time+1
    if ans == "시장":
      print("이야기2")
      time = time+2
      print("피노키오야 학교에 갔니?")
      ans2=int(input("학교에 갔다 왔다(1), 학교에 안 갔다(2)"))
      if ans2==1:
        nose=nose+1
        print("피노키오는 거짓말을 했습니다.")
      if ans2==2:
        print("착한아이구나. 거짓말을 안하다니.")
      #item=True  
    if time>=2 and nose>=1:
      print("이벤트 발생")
      break
#pinokio함수는 이야기 푸는데 필요한 좋은 예시입니다.

while(1):
    login()
    
