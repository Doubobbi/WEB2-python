def sum(a, b):
    result = a + b
    return result
print(sum(1,2))
#입력값이 없는함수
print()
def say():
    return 'Hi'
print(say())
#결과값이 없는 함수
def sum(c, d):
    print("%d, %d의 합은 %d입니다." % (c, d, c+d))
sum(1,2)
print()
#여러개
# *args = 여러개 들어갈수있다( 다른글자를 써도됨)
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum +i
    return sum
print(sum_many(1,2,3,4))
print()
#다른버젼
def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if (k == "name"):
            print("당신의 이름은 :" + kwargs[k])
print(print_kwargs(name="int 조수"))
print()
#함수의 결과값은 언제나 하나이다
def sum_and_mul(a,b):
    return a+b, a*b, a-b

print(sum_and_mul(1,2))

def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살 입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")  
say_myself("이영일",20)
print()
#변수의 범의

a =1 
def vartest(a):
    a = a +1
    
vartest(a)
print(a)
print()

