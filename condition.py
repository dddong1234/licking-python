
#1 중간고사 점수와 기말고사 점수를 입력받아 평균이 80이상이면 A, 평균이 80보다 작고 60이상이면 B, 아니면 F를 출력한다.


mid= int(input("중간고사 점수 입력 : "))
fin= int(input("기말고사 점수 입력 : "))
avg=(mid+fin)/2
if avg>=80:
    score="A"
elif 80>avg>=60:
    score="B"
else:
    score="F"
print("중간고사= {0}         기말고사={1}         평균={2}           학점={3}".format(mid,fin,avg,score))

print("--------------------------------------------------")
#2 홀수/짝수를 판단하는 컴퓨터

num=int(input("수를 입력하세요: "))
if num%2==1:
    print("홀수 입니다.")
else:
    print("짝수 입니다.")

print("--------------------------------------------------")
#3 컴퓨터와 가위바위보 게임을 해 보자

import random as r

a=0
b=r.randint(0,2)
c=input("가위바위보 시작!. 가위, 바위, 보 중 한가지를 입력해주세요:")
if b==0:
    b="가위"
    if c=="가위":
        a=0
    elif c=="바위":
        a=1
    else:
        a=2
elif b==1:
    b="바위"
    if c=="가위":
        a=2
    elif c=="바위":
        a=0
    else:
        a=1
else:
    b="보"
    if c=="가위":
        a=1
    elif c=="바위":
        a=2
    else:
        a=0

if a==0:
    a="비겼습니다"
elif a==1:
    a="user 승!"
else:
    a="com 승!"

print("com: {0}    user: {1}     결과: {2}".format(b,c,a))

print("--------------------------------------------------")

#4 놀이동산 요금을 계산해 보자

a=0
age=int(input("나이를 입력해주세요: "))
if age<8:
    a="무료"
elif 8<=age<60:
    a="정가(5000원)"
else:
    a="정가의 50%(2500원)"

print("나이 {}세 이용객의 요금은 {}입니다".format(age,a))
