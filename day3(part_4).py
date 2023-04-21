num = 10
num = float(num) # 정수형인 3을 실수형인 3.0으로 변환
print(type(num))

num = float("3.14") # 문자형 3.14를 실수형인 3.14로 변환
print(type(num))

height = float(input("키 정보입력: ")) # 문자형인 입력값값을 실수형으로 변환
print(height)

num = int(3.14) # 실수형인 3.14를 정수형인 3으로 변환
print(num)

# 연습문제 4-1
def int_div(n1, n2):
    print("몫: ", n1 // n2)
    print("나머지: ", n1 % n2)

int_div(5, 2)    
    
def bet_sum(n1, n2):
    sum = 0
    for i in range(n1 + 1, n2):
        sum = sum + i
    print(sum)

bet_sum(2, 5)    
