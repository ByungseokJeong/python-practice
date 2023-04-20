# 연습문제 2-1
def MH():
    print("1 + 2 + 3 + 4 + 5 =", 1 + 2 + 3 + 4 + 5)
    print("Simple is the best!")
    print("행복한 파이썬")

MH()   

# 연습문제 2-2

def zs(n1):
    print(n1)
    print(n1)
    print(n1)

zs(2)    

def bs(n1):
    print(n1 * -1)

bs(3)

def ding(n1, n2):
    print((n1 + n2) / 2)

ding(5, 7)    

# 연습문제 2-3
def fx(n1): # n1이라는 변수를 가진 함수 fx 정의
    d1 = n1 * -1  
    return d1 # 변수 d1을 입력한 곳에 반환

drx = fx(5) # 함수 fx에 5를 입력한 변수 drx 
print(drx)

def dopa(n1, n2): # n1, n2라는 변수를 지닌 함수 dopa 정의
    ex = (n1 + n2) / 2 # n1과 n2의 평균값을 지닌 변수 ex 설정 
    return ex # ex의 값을 입력한 곳에  반환함

rodic = dopa(2, 4) # 함수 dopa를 호출하는 하는 변수 rodic 
print(rodic) # rodic의 값 출력
    

def adder(n1, n2): # adder 함수의 정의
    return n1 + n2 

def main(): # 실행 흐름을 담은  main 함수의 정의
    print(adder(5, 7))
    print(adder(2,4))
    print(adder("abc", "def"))

main() # main 함수 호출
    
