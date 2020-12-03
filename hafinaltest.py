'''
1) 비대면 환경임을 고려하여 오픈북으로 진행됨
2) 문제 주제는 기존과 동일하나 기존의 암기형 손코딩 문제에서, 서술형 문제 or 실제 프로그래밍 문제로 변경됨

<문제 구성>

-서술형 문제 1개
컴퓨팅 사고 관련 서술형 문제

-프로그램 문제 1~2개
11강 14강 3번째 시간에 소개되는 예제들 (예제코드--선 시리즈)을 부분적으로 수정하여 제출할 예정입니다.
-->객관식 문제 / 손코딩 문제는 출제하지 않습니다. 제한된 시간 내에 본인의 PC 에서 직접 프로그래밍하여 실행해본 py파일을 제출하는 형태로 변경됩니다.

-서술형 문제 & 프로그래밍 융복합 문제 1개
컴퓨팅 사고 및 이와 연계한 프로그래밍 문제
'''
#--------- 11강 예제----------
#예제 1 : BMI 지수 계산하기
def bmi():
    name = input("what your name?")
    age = int(input("what your age?"))
    height = float(input("typing your height.\n"))
    weight = float(input("typing your weight.\n"))

    height = height / 100
    bmi = weight / (height * height)
    print("%s, your bmi is %f." % (name, bmi))

#예제 2 :BMI 계산 공식을 함수로 구현
def Getbmi(height, weight):
    height = height / 100
    return weight / (height * height)
#print(" %s BMI percent is %f." %('hong',Getbim(178,77))

#예제 3 : 스무고개 게임
def game20():
    number = int(input("1부터 20까지의 수 중 아무 수를 입력하세요. \n"))
    while(1):
        guess = int(input("수를 입력하세요.\n"))
        
        if guess > number:
            print("추측한 수보다 적습니다.")
        if guess < number:
            print("추측한 수보닥 많습니다.")
        if guess == number:
            print("PASS!!!!")
            break

#예제 4 : 장바구니 추가
#list(5주차)를 활용해서 장바구니 추가를 구현해 봅시다.
def shopping():
    cart = []

    while(1):
        item = input("add your item.\n")
        cart.append(item)
        print(cart)

#예제 5 : 장바구니 삭제
#list(5주차)를 활용해서 장바구니 추가를 구현해 봅시다.
def rmshopping():
    
while(1):
    bmi()
