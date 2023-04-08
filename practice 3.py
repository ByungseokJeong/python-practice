# 연습문제 1
x = input("첫번째 입력: ")
y = input("두번째 입력: ")
print("두 입력의합:", x + y)

# 연습문제 2
jack = eval(input("첫번째 입력: "))
kick = eval(input("두번째 입력: "))
print("두 입력의 합:", jack + kick)

# 연습문제 3
som = 1
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    som = som * i


print(som)


som = 0
for i in [1, 3, 5, 7, 9]:
    som = som + i
    

print(som)

for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("7 x", i, "=", 7 * i)
