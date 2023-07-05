# immutable
# 정수, 실수 문자열, 튜플 변하지않음
# ex) a = 1
# def vartest(a):
#def함수선언
#       a = a + 1
#vartest(a)
#print(a)


#mutable
#리스트,집합,딕셔너리
# ex) b = [1,2,3]
#def vartest2(b):
    # b= b.append(4)

#vartest2(b)
#print(b)

#클래스
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
        
cal1 = Calculator()
cal2 = Calculator()
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

print()

