a = {1: '파란하늘', 2: '노란 꽃잎', 3: '빨간 차'}

for k, v in a.items():
    print("키는: " + str(k))
    print("밸류는: " +v)
print()
print(a.get(4,'없음'))
print()
print(4 in a)
print()
s1 = set([1,2,3])

print(s1)
print()


l = [1,2,2,3,3]
newList = list(set(l))
print(newList)

s2 = set("hello")
print(s2)
print()
#교집합
s3 = set([1,2,3,4,5,6,])
s4 = set([4,5,6,7,8,9])
print(s3 & s4)
print()
print(s3.intersection(s4))

print()
#합집합
print(s3 | s4)
print()
print(s3.union(s4))

#차집합
print(s3 - s4)
print()
print(s4.difference(s3))
print()
#추가
s3.add(7)
print(s3)
print()
s3.update([7,8,9])
print(s3)