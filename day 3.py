"""# 예제 3-3
sum = 0
for i in [1, 3, 5, 7, 9]:
    sum = sum + i

print(sum)    

sum = 1
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum * i

print(sum)    

sum = 1
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sum = 7 * i
    print("7 x", i, "=", sum)


sum = 1
for i in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
    sum = 7 * i
    print("7 x", i, "=", sum)"""

# 연습문제 3-4
def exp(x, y):
    rlt = 1
    for i in range(y):
        rlt = rlt * x
    return rlt

exp(2, 3)

def greef():
    num = eval(input("인사를 몇번 할까요?"))
    for i in range(num):
        print("반갑습니다")

greef()    
