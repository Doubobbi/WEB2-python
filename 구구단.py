#구구단

a = 10
for i in range(2,10):
    for j in range(1, 10):
        print(i * j, end=" ")
    print('')

print()
#list내포 이건 틀렸음 다시 공부 해야됨
result = [num * 3 for num in a if num % 2 == 0]


print()
result = []
for num in a:
    if num%2==0:
        result.append(num*3)