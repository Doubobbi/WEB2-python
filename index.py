#!python3

a = "hobby"
print(a.count('b'))
print(a.find('y'))

b= ",".join("abcd")
print(b)

c = 'hi'
print (c.upper())

d = "Life is too short"
print(d.replace("Life", "Your legs"))
print(d.split())

e = ["이영일","강예지","홍창기","켈리","문성주","문보경","염경엽","신민재"]
print(e[3])
print(e[1] + e[3])
print(e[0:3])
e[0] ="함덕주"
print(e)
e.append("김현수")
print(e)
print(e.count("김현수"))

t1 = (1,2,'a','b')

print (t1)

dic = {'이름': '영일', 'age': 12 , '포지션' : '투수', '투타' : '좌투좌타'}
print(dic['포지션'])

h = {'이름': '문보경', 'age': 24 , '포지션' : '내야수', '투타' : '우투좌타'}
h['Avg'] = "0.294"
print (h['Avg'])
print (h)