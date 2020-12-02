#컴퓨터프로그래밍 과제

#제출자 : B976090 박 하 

#제출일 : 2020/11/30

#==============================================







#선언문=========================================



#about_딜레이

import time

def delay(a):

    time.sleep(a)

    

#about_도어락 비밀번호 시도 횟수

count = 0



#==============================================













#==================START=======================





#=======[ Chapter 1 ]=========











print("==============================================")

print("으랏차차 M동 방탈출!!")

print("==============================================")





delay(2)

print("\n\n밤샘 과제 후, M동 7층 실습실에서 잠이 든 나.")

print("쿵!!! 하는 소리에 놀라 일어나보니 주위가 어둡다.")



delay(2)

print("\n\n뭐지...?")







while (True):

    delay(2)

    sel1 = int(input("\n[ 제자리에 앉아있는다 (1) / 스위치를 찾아서 불을 켠다. (2) ]"))



    

    if sel1 == 1:

        delay(2)

        print("\n쿠웅---!")

        print("어두운 실습실에 혼자 있으려니 점점 더 무서워진다")

        print("설상가상 밖에서 이상한 소리가 가까워지고 있다.")



        delay(3)

        print("\n\n불을 켜볼까?")



        

    elif sel1 == 2:

        delay(2)

        print("\n딸깍,딸깍...!")

        print("불이 켜지지 않는다...")



        delay(3)

        print("\n아, 맞다! 휴대폰!!")

        break





    else:

        print("\n잘못 고르셨어요. 1 / 2번 중 골라주세요.")









        

#=======[ Chapter 2 ]=========









        

delay(2)

print("\n주머니에서 폰을 꺼냈지만 전화가 안 터지네......")

print("우선 휴대폰 불빛에 의지해 여기저기 둘러본다.")







while (True):

    delay(2)

    sel2 = int(input("\n[ 창문을 열고 밖의 상황을 확인한다 (1) / 문을 열고 복도로 나간다 (2) ]"))

    

    if sel2 == 1:

        delay(2)

        print("\nM동 밖은 평소와 다를 바가 없다.")

        print("아무래도 정전인 것 같다.")

        

        delay(2)

        print("\n\n문을 열고 복도로 나가보자.")

        break

  

              

    elif sel2 == 2:

        break

    

    

    else:

        print("\n 잘못 고르셨어요. 1 / 2번 중 골라주세요.")







        



#=======[ Chapter 3 ]=========









        

delay(3)

print("\n덜컹, 덜컹!" )

print("문에 도어락이 설치되어 있다!")

        

delay(2)

print("\n비밀번호가 뭘까?")

print("실습실 안에 힌트가 있을 거야. 찾아보자!")



delay(3)

print("\n\n . . . . . . ")



delay(3)

print("\n\n 실습실 안에는 사물함과 책상, 노트북이 있다.")



delay(2)

print("\n\n어디를 찾아볼까?")







while (True):

    sel3 = int(input("\n[ 사물함(1) / 책상(2) / 노트북(3) ]"))

    

    if sel3 == 1:

        delay(3)

        print("\n\n사물함 안에 쪽지가 있다!")

        print("<<< qwer1234 >>>")



        delay(2)

        print("\n\n좋아, 도어락을 열어보자!!")



    

        while (True):

            sel3a = input("\n도어락 __ 비밀번호를 입력하세요. : ")



            if sel3a == "KSJ":

                sel3 = 4

                break

        

            else:

                count=count+1

                sel3 = 56

                if count == 3:

                    while (True):

                        print("방탈출에 실패하였습니다........")

                break





            

    if sel3 == 2:

        delay(3)

        print("\n\n책상 밑에는 아무것도 없네...")

        

        delay(2)

        print("\n\n어디를 찾아볼까?")







    if sel3 == 3:

        delay(3)

        print("\n\n노트북 화면이 잠겨 있다.")

        

        while (True):

            print("\n노트북을 활성화 시키려면 사용자 암호를 입력하세요.")

            sel3b = input(": ")



            if sel3b == "qwer1234":

                delay(3)

                print("\n\n환영합니다-!")

                print("노트북 메모장에 힌트가 나타났다.")



                delay(2)

                print("\n\n<< 도어락 힌트 >>")

                print("1. 컴퓨터 프로그래밍 교수님의 성함")

                print("2. 이니셜을 입력하시오.")



                delay(2)

                print("\n\n좋아, 도어락을 열어보자!!")

         

                while (True):

                    sel3d = input("\n도어락 __ 비밀번호를 입력하세요. : ")



                    if sel3d == "KSJ":

                        sel3 = 45

                        break

                

                    else:

                        count=count+1

                        if count == 3:

                            while (True):

                                print("방탈출에 실패하였습니다........")

                                

                        elif count !=3:

                                

                            print("\n\n삐-빅!!")

                            print("비밀번호를 바르게  입력하세요.\n")

                            print("[시도 횟수 : ",count,"]  3회 누적시 방탈출에 실패합니다.")



                            delay(2)                    

                            print("\n\n이 비밀번호는 아닌것 같다. 다시 시도해보자.")



                        

                if sel3d == "KSJ":

                    break

                      





            if sel3b != "qwer1234":

                print("\n\n사용자 암호가 일치하지 않습니다.")

                

                delay(2)

                sel3c = int(input("\n\n[ 다시 입력한다 (1) / 다른 곳을 찾아본다 (2) ]"))

                

                if sel3c == 1:

                    print("")

                    

                elif sel3c == 2:

                    print("\n\n어디를 찾아볼까?")

                    break

                

                else:

                    print("\n\n잘못 입력하셨습니다. 초기 선택 화면으로 돌아갑니다.")

                    break

                



              

    if sel3 == 45:

        print("\n\n띠리릭~!")

        print("도어락이 열렸다! 탈출 성공!!!")

    

        while (True):

            i=1



           

    if sel3 == 56:

        print("\n\n삐-빅!!")

        print("비밀번호를 바르게 입력하세요.\n")

        print("[시도 횟수 : ",count,"]  3회 누적시 방탈출에 실패합니다.")



        delay(2)

        print("\n\n사물함 속 쪽지에 적힌 힌트는 도어락 비밀번호가 아니었다...")

        print("그렇다면 다른 곳에 도어락 비밀번호에 대한 힌트가 있을 거야!")

        

        delay(2)

        print("\n\n어디를 찾아볼까?")





    

    elif sel3 != 1  and sel3 != 2 and sel3 != 3 and sel3 != 45:

        print("\n 잘못 고르셨어요. 1 / 2 / 3 번 중 골라주세요.")

















        


