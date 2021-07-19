#1. 당신은 ‘코딩’ 에 대해 조금은 이해했을거라 기대합니다. 그렇다면 ‘코딩’이 무슨 의미인지
#를 설명해 보세요. 단! 다음과 같은 절차를 거치도록 프로그램을 작성하세요.
print("문제 1번")
print()
    
a=input("이름 : ")
b=input("학과 : ")
c=input("학번 : ")
print("당신의 학과는",b,"입니다")
print("당신의 학번은",c,"입니다.")
print("당신의 이름은",a,"입니다.")
print("코딩에 대해 알려드리겠습니다.")
d=len(a+b+c)*2
print("="*d)
print("|",b,"|",c,"|",a,"|")
print("="*d)
print("코딩이란 험난한 탐험입니다. 내게 주어진 '언어'라는 '도구'를 가지고 "
      "'결과'라는 '목적'에 도달하기 때문이죠")
print("="*d)

#2. 1~100 사이의 숫자 열개로 이루어진 임의의 리스트를 한 개 만든 후(original) 리스트 원소
#값의 평균 이상인 원소들만을 골라 새로운 리스트(new_list)로 만든다. 새로 만들어진 리스트
#(new_list)를 화면에 출력하고 그 리스트 원소들의 최대값/최소값/평균을 출력하시오.

print()
print("문제 2번")
print()
import random as r

a = r.randint(1, 100)
b = r.randint(1, 100)
c = r.randint(1, 100)
d = r.randint(1, 100)
e = r.randint(1, 100)
f = r.randint(1, 100)
g = r.randint(1, 100)
h = r.randint(1, 100)
i = r.randint(1, 100)
j = r.randint(1, 100)
original = [a, b, c, d, e, f, g, h, i, j]
avg = (a + b + c + d + e + f + g + h + i + j) / 10
new_list = []
for i in original:
    if i >= avg:
        new_list.append(i)
print("new_list : ",new_list)
k = 0
for j in new_list:
    k = k + j
avg_new = k / len(new_list)

new_list.sort()

print("최대값 : ",new_list[-1])
print("최소값 : ",new_list[0])
print("평균 : ",avg_new)
