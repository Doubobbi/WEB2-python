


#람다 함수

#myList = [lambda a, b: a+b, lambda a,b: a*b]

#print(myList[0](3,2))
#print(myList[1](3,4))

print()
#외장함수
#def 는 사용자 정의 함수
#number = input("숫자를 입력하세요: ")

#print(number)

print()
#프린트 함수

print("life","is","too short")
print()

for i in range(10):
    print(i, end=' ')
#쓰기모드
f = open("새파일.txt", 'w', encoding="UTF-8")
for j in range(1,11):
    data = "%d번째 줄입니다. \n" % j
    f.write(data)
f.close()    
print()

f = open("새파일.txt", 'r', encoding="UTF-8")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()

#f.readlines는 전부 읽어오는것
#f.readline은 한줄만 읽어 오는것
#f = open("새파일.txt",'a')하게되면 뒤에 더 추가하겠다이고
#f = open("새파일.txt",'r')을 하게되면 다 갈아엎고 새로하겠다이다
f = open("새파일.txt", 'a' , encoding="UTF-8")
for j in range(11,20):
    data = "%d번째 줄입니다. \n" % j
    f.write(data)
f.close()

with open("foo.txt", "w") as f:
    f.write("Life is too short, you need python")
