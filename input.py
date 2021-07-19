#이름 학교 전공 학
name=input("이름을 입력하시오:")
print("당신의 이름은 {}입니다.".format(name))

school=input("학교를 입력하시오:")
print("당신은 {}학교 학생 입니다.".format(school))

major=input("전공을 입력하시오:")
print("당신은 {}학과 입니다".format(major))

grade=int(input("학년을 입력하시오:"))
print("당신은 {}학년 입니다".format(grade))

print("당신은 {0}학교 {1}학과 {2}학년 {3}입니다".format(school,major,grade,name))


print("="*40)

#사칙연산 하기

a=int(input("0이 아닌 첫번째 수를 입력하시오: "))
b=int(input("0이 아닌 두번째 수를 입력하시오: "))

print("{0}+{1}={2}".format(a,b,a+b))
print("{0}-{1}={2}".format(a,b,a-b))
print("{0}*{1}={2}".format(a,b,a*b))
print("{0}/{1}={2:5.3f}...".format(a,b,a/b))

print("="*40)

#넓이 구하기

import math

print("삼각형의 넓이를 구하겠습니다")
print()
t_1=int(input("밑변의 길이를 정해주세요: "))
t_2=int(input("높이의 길이를 정해주세요: "))
S_1=(t_1 * t_2)/2
print("삼각형의 넓이는 {}입니다".format(S_1))
print()
print("사각형의 넓이를 구하겠습니다")
print()
s_1=int(input("한변의 길이를 정해주세요: "))
s_2=int(input("높이의 길이를 정해주세요: "))
S_2= s_1*s_2
print("사각형의 넓이는 {}입니다".format(S_2))
print()
print("원의 넓이를 구하겠습니다")
print()
c_1=int(input("반지름의 길이를 정해주세요: "))
S_3=(c_1**2) * math.pi
print("원의 넓이는 약 {0:5.2f}입니다".format(S_3))

print("="*40)

#패딩 스웨터-1

print("백화점 30% 세일중")
print("패딩은 230000원, 스웨터는 140000원 입니다")
a=int(input("패딩을 몇 개 구매 하시겠습니까? : "))
b=int(input("스웨터를 몇 개 구매 하시겠습니까? : "))
total= a*230000 + b*140000
print("총 가격은 {0:8.2f}원 입니다.".format(total))

#패딩 스웨터-2

a_1= int(input("패딩의 가격을 정해주세요. : "))
b_1= int(input("스웨터의 가격을 정해주세요. : "))
c= int(input("할인율을 정해주세요. : "))
print()
print("손님이 왔습니다")
a_2= int(input("패딩을 몇 개 구매 하시겠습니까? : "))
b_2= int(input("스웨터를 몇 개 구매 하시겠습니까? : "))

total= ((a_1 * a_2)+(b_1 * b_2))*(1-(c/100))

print("총 가격은 {0:8.2f}원 입니다".format(total))



#야옹이가 하고싶은말

a=input("고양이가 하고 싶은 말은? ")
b=len(a)

print("        ","_"*b)
print("       ","<{0}>".format(a))
print("        ","-"*b)
print("        /")
print(" /\_/\ /")
print("( o.o )")
print(" > ^ <")
