#반복문(while)

나무찍기 = 0
while 나무찍기 < 10:
    나무찍기 = 나무찍기 + 1
    print("나무를 %d번 찍었습니다." % 나무찍기 )
    if 나무찍기 ==10:
        print("나무가 넘어갑니다.")

print()

커피 = 10
돈 = 10000
while 돈:
    print("돈을 받았으니 커피를 줍니다.")
    커피 = 커피 -1
    print("남은 커피의 양은 %d개입니다." % 커피)
    if not 커피:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
# 컨티뉴
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)

#무한루프 while = True: print("안녕하세요")

