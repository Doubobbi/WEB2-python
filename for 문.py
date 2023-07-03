
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#ex2
print()
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

print()
#ex3
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

#내가해보는 예시
print()

면접자 = [40, 50, 70, 80, 90]
면접자수 = 0
for 지원자 in 면접자:
    면접자수 = 면접자수 + 1
    if 지원자 >= 60:
        print("%d번 지원자는 합격 입니다." % 면접자수)
    else:
        print("%d번 지원자는 불합격 입니다." % 면접자수)

print()
#for문 과 continue
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60: continue
    print("%d번 학생 축하합니다. 합격입니다." % number) 

print()