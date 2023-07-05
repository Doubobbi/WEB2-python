import sys
sys.path.append("C:\\WEB2\\SubFolder")
import mod1
print(mod1.add(3,4))

def positive(x):
    return x > 0


#필터 내장함수
a = list(filter(positive, [1, -3, 2, 0, -5, 6]))
print(a)

#맵

def two_times(y): return y*2
b = list(map(two_times, [1, 2, 3, 4]))
print(b)
#같은 맵 람다 함수
c = list(map(lambda c: c*2, [1, 2, 3, 4]))
print(c)

#zip내장함수
>>> list(zip([1, 2, 3], [4, 5, 6]))