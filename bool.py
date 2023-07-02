a = [1,2,3,4]
while a:
    a.pop()
    print(a)

b = [1,2,3]
#슬라이싱해서 넣으면 아이디가 바뀜
c = b[:]

b[1] = 4
print(id(b))
print(id(c))
print()
print(b)
print(c)

#같은 방식으로 copy 도 가능
from copy import copy
d = [1,2,3]
e = copy(d)
d[1] = 4
print(d)
print(e)
print()
#변수 할당 방법
f, g = ('python', 'life')
print(f)
print(g)
print()
#이것도 같은 방법
(h, i) = '같은', '방법'

print(h)
print(i)
print()
#리스트로도 가능
[j, k] = ['이것도', '가능']
print(j)
print(k)
print()
#l값과 m값을 바꾸고싶을때
#일반적인ex) l = 3 , m = 5 
# l = 3
#m = 5
#tmp = m
#m = l
#l = tmp
#print(l)
#print(m)
#파이썬은
l = 3
m = 5
l,m = m,l
print(l)
print(m)



