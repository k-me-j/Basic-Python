# 리스트 자료형
print("▶ list 생성해보기")
list1 = [1, 2, 0.1, "string"]
print(f'{list1}')
print(list1)
print()



# 평수, 방 개수, [방#1, 방#2, 방#3], 층수, 가격
house = [30, 3, ['study', 'bed', 'game'], "1층", "3억"]

str1 = f'My hose area is {house[0]}, ' \
    f'there are {len(house[-3])} rooms. ' \
    f'I like the {house[-3][2]} room.'

print(str1)
print()

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
# list4 = list1 * list2
list5 = list1 * 5
print(list3)
# print(list4)
print(list5)
print()



# 문자열 관련 함수
print("▶ 문자열 관련 함수")
a = """Spread out before him that April day was the largest flotilla Communist-ruled China
48 ships, dozens of fighters jets, more than 10,000 military personnel."""

cnt_a = a.count("ships")
print("● count('ships') : ", cnt_a)
print("● find, index : ", a.find("jets"), a.find('h'), a.index('h'), a.find('korea'))
print("● upper : ", a.upper())
print("● lower : ", a.lower())
print()

b = '12345'
print(",".join(b))  # 1,2,3,4,5
print()

c = "Life is too short."
print(c.replace("short", "long"))  # Life is too long.
print(c)  # Life is too short.

c = c.split()
print(c, type(c))  # ['Life', 'is', 'too', 'short.'] <class 'list'>

c = " ".join(c)
print(c, type(c))  # Life is too short. <class 'str'>
print()



# 과제 : 문자열 변환하기
'''
Vehicle x y w h 가 반복되는 데이터가 있을 경우,
해당 데이터에서 넓이가 100 이상인 vehicle인 경우에는 Vehicle->Truck으로 변경
(조건 : Vehicle만 있고, 두 개의 라벨링 데이터만 존재)
'''
## 1. split 사용
str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250"
print("변경 전 : ", str_txt)

vehicle_list = str_txt.split(" ")

for i in range(len(vehicle_list)):
    if vehicle_list[i] == 'vehicle' and int(vehicle_list[i+3]) >= 100:
        vehicle_list[i] = 'Truck'

print("변경 후 : ", ' '.join(vehicle_list))
print()

## 2. split 사용 ㄴㄴ
'''
' ' 나올때까지 컷?
'''
str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250"

'''
find로 
'''