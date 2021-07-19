import random as r
a=0

while a<10:
    a=a+1
    com=r.randint(1,10)
    com_2=com%2
    print()
    user=input("홀 짝을 맞춰보세요: ")
    if user=="홀":
        user=int(1)
    else:
        user=int(0)
    if com_2==1 and user==1:
        print("홀수가 맞습니다~ 축하합니다")
    elif com_2==0 and user==0:
        print("짝수가 맞습니다~ 축하합니다")
    else:
        print("틀렸습니다 다시 시도하세요")
    print("컴퓨터의 숫자는 {0}입니다~".format(com))
print("총 {0}번 반복했습니다".format(a))