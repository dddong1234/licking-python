import random as r
num1=1
num2=0

while num1<8:
    data1=r.randint(1,9)
    data2=r.randint(1,9)
    print("{}) {}*{} 는 얼마인가요?".format(num1,data1,data2))
    dap=int(input("결과: "))
    num1=num1+1

    if dap==data1*data2:
        print("정답입니다.")
        num2=num2+1
    else:
        print("오답입니다")
print("정답을 맞춘 횟수:", num2)
