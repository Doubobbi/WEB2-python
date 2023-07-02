
#if 문

money = 12000
if money >= 10000 :
    print("택시를 타고 가라")
else:
    print("걸어 가라")    

#if 문은 들여 쓰기가 중요하다 파이썬은 들여쓰기가 중요함
print()
#자료형 값이 아래와 같으면 거짓 참으로 나뉜다
#  "python" = true 
#  "" = false
#[1,2,3] = true 값이 써있으면 참
# []= false
#()=false
#{}=false
#1 =true
# 0 = flase
# none = false
# or 이 들어가면 둘중에 아무거나 참이어도 true
#and 는 둘다 참이여야 true

if 1 in [1,2,3]:
    print("있음")
else: print("없음")    
print()

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    pass
elif card:
    print("택시 타셈")
else:
    print("걸으셈")   
#조건부 표현식
print()
print()
score = 70
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)

#위구문을 수정하면
print()
print()
#다른 언어에서는 3항 연산자로 표현함
message = "success" if score >= 60 else "failure"
print(message)