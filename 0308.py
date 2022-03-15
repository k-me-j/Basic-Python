# 정수 표현 : 특정 변수에 정수 값을 대입
print("▶ 정수 표현")
a = 123
b = -1234
print(a,b)
print(f'{a}를 16진수로 나타내기 : {a:0x}')
print(f'{a}를 소수로 나타내기 : {a:f}')
print()


# 실수 표현 : 특정 변수에 실수 값을 대입
print("▶ 실수 표현")
fa = 3.141532
fb = -0.33245
fexpA = 4.24E3  # E3 = 10^3
fexpB = 4.24E-3  # E-3 = 10^-3
print(fa, fb, fexpA, fexpB)
print()


# floating point example
print("▶ floating point example")
num = 0.0
for idx in range(0,100):
    num += 0.1
print(num)
print(f'{num:.18f}')  # 소수점 아래 18번째 자리까지 표현하기
# 0.1을 100번 더했는데도 9.99... 딱 10을 표현하는 게 아니라 10에 근접한 숫자를 나타내게 됨.
# 실수를 이진법으로 나누다보면 딱 떨어지지 않는 경우가 있기 때문 ex)0.3
print()


# 연산자
print("▶ 연산자")
num1, num2 = 7, 4
print(f"{num1}**{num2} = ", num1**num2)   # ** 연산자 : 제곱
print(f"{num1}//{num2} = ", num1//num2)   # // 연산자 : 나눗셈 후 몫 반환
print(f"{num1}%{num2} = ", num1%num2)     # % 연산자 : 나눗셈 후 나머지 반환
print()


# [실습] 구구단 만들기
print("▶ 구구단 만들기")
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} x {j} = ', i*j)
print()


# prime number 소수 구하기 : 약수가 1과 자기 자신 밖에 없는 수
print("▶ 소수 구하기 : 주어진 코드(오류 존재)")
# 주어진 코드 : 오류 있는 코드
testNum = 12
for i in range(2,testNum):
    if (testNum % i) == 0:
        print(f"{testNum} is not Prime Number")
        break
    print(f'{testNum} is Prime Number')
print()

# 알고리즘 적용하기
# 약수는 대칭적 -> 구하려는 숫자의 제곱근 이하까지만 체크하면 됨
# ex) 6 : 1 2 3 6 -> 6의 제곱근인 2.4494... 이하까지만 체크하면 됨
# print("▶ 소수 구하기 : 알고리즘 적용해보기")
# import math as m
#
# input_num = int(input("소수 여부를 확인할 정수를 입력하시오 "))
# if input_num > 1:
#     for i in range(2, int(m.sqrt(input_num))+1):  # 안의 수식은 변수로 빼주기. for문 돌때마다 실행하지 않아도 되는 부분이잖아.
#         if input_num % i == 0:
#             print("false")
#             break
#     else:
#         print("true")  # break 없이 for문 벗어난 경우에만 출력
# else:
#     print("false")
# print()

'''
# 참고하기
while(1):
    testnum = input()
    if (testnum.isdigit()):
        break
'''

# 조언 참고해서 다시 짠 코드
# while(1):
#     num = input("소수 여부 확인할 숫자 입력 ")
#     if num.isdigit() and int(num)>1:
#         num = int(num)
#         break
#     print("2이상의 숫자만 입력하시오")
#
# for i in range(2, int(m.sqrt(num))+1):
#     if num % i == 0:
#         print(f"False. cuz '{i}'")
#         break
# else:
#     print("True")
# print()


# 문자열 연산하기
print("▶ 문자열 연산하기")
str1 = "Hi everyone"
str2 = "My name is ..."
str3 = '*' * 20
print(f'{str3*3}\n{str1 + str2}, \n'
      f'This block is comment block\n'
      f'{str3*3}')
print()


# [실습] 문자열 슬라이싱하기
today = "20220308Sunny"
print(f"Today is {today[:8]} and it's {today[8:]}!")
