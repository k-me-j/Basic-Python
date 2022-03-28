# 1.
# 정수형, 실수형, 문자열 및 "리스트 내에 리스트" 등을 포함하여 자신을 소개하는 리스트를 만들고,
# 리스트 인덱싱과 슬라이싱 기법 등을 이용하여 자기 소개하는 것 표현해보기
iam = ["정", "경임", "03", [1992, "0524"]]
introduce = f'''안녕하세요. 저는 {iam[0]}{iam[1]}이라고 합니다. 
{iam[-1][0]}년에 태어났고, 생일은 {iam[-1][1][:2]}월 {iam[-1][1][2:]}일입니다.
ML실 AI-{iam[2]} 컴퓨터를 지정석으로 사용하고 있습니다.
'''
print(introduce)


# 2.
## 2-1. 문자열 변수에서 특정 인덱싱으로 접근 후 문자열을 변경할 수 있는가? 답변 및 가능한 방법 코드 작성 및 제출
## 답변 : 문자열 변수에 특정 인덱싱으로 접근 후 문자열 변경 가능합니다.
ai = "ML, DL"
ai = ai.replace("L", "-Learning")
ai = ai.replace("M", "Machine").replace("D", "Deep")
print(ai)

## 2-2. mutable, immutable 자료형 정리해보기
mutable = ["값이 변하는 것", "List", "Dictionary", "Set"]
immutable = ("값이 변하지 않는 것", "Tuple", "Integer", "Float", "String")


# 3.
## 3-1. List에서 append, insert, extend 차이점
week = ['mon', 'tue', 'thu']

week.append("fri")  # 리스트의 가장 마지막에 요소 추가
print(week)
week.insert(2, 'wed')  # insert(i,x) i 위치에 x 추가
print(week)
week.extend(['sat', 'sun'])  # 괄호에 iterable한 자료만 넣을 수 있음. 리스트 마지막에 요소들 추가
print(week)
week.extend([['주중', '주말']])  # 대괄호 2개 사용시 요소가 아닌 리스트로 입력됨
print(week)

## 3-2.  remove, pop
finger = ['엄지', '검지', '중지', '약지', '소지']
# remove : 삭제할 부분을 값으로 입력
print(finger.remove("검지")) # None
print(finger)

# pop : 삭제할 부분을 index로 입력, 따로 지정하지 않으면 가장 마지막 값을 반환 후 삭제
print(finger.pop(-2))
print(finger)


# 4.
# 기존 파싱 코드에서 자료형 list와 문자열 관련 함수 split()을 이용하여 동일한 결과 도출하기
str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250"

vehicle_list = str_txt.split(" ")

for i in range(len(vehicle_list)):
    if vehicle_list[i] == 'vehicle' and int(vehicle_list[i+3]) >= 100:
        vehicle_list[i] = 'Truck'

print(' '.join(vehicle_list))


# 5.
# 기존 파싱 코드에서 데이터를 어떻게 만들면 더욱 효율적으로 처리할 수 있는지
# - Data 형식 변경 및 추가, 코드 작성 결과 확인 (조건은 동일함, 크기가 100보다 크면 vehicle에서 truck으로)
import json
from collections import OrderedDict  # json 만들기 위한 라이브러리

# json 파일 생성하기
vehicle_dataset = []  # 딕셔너리로 바꾼 자동차들의 정보를 담아줄 리스트
vehicle_json = OrderedDict()

input_data = input("입력 : vehicle 0 0 50 50 vehicle 50 50 250 250\n").split(" ")

for i in range(0, len(input_data), 5):  # 자동차 한 대의 정보가 5개의 요소로 이루어져 있으므로 index 5번에 한 번씩 반복해주기
    vehicle = {}  # 자동차 한 대의 정보를 담을 딕셔너리

    vehicle["clf"] = input_data[i]
    vehicle["x"] = int(input_data[i + 1])
    vehicle["y"] = int(input_data[i + 2])
    vehicle["w"] = int(input_data[i + 3])
    vehicle["h"] = int(input_data[i + 4])

    vehicle_dataset.append(vehicle)

    vehicle_json["vehicle_list"] = vehicle_dataset

# 확인해보기
print(json.dumps(vehicle_json, indent='   '))  # 화면 출력시 dumps

# json 파일 생성하기
json_path = 'vehicle.json'
with open(json_path, 'w') as mkfile:
    json.dump(vehicle_json, mkfile, indent='   ')  # 저장할 땐  dump (s 없음)

# json 파일 dict로 가져오기|
with open(json_path, 'r', encoding='utf-8') as f:
    load_vehicle = json.load(f)
    # print(json.dumps(load_vehicle, indent='   '))  # json 파일 내용 확인하기

# 조건에 맞게 vehicle -> truck 변환하기
for one in load_vehicle['vehicle_list']:
    if one['w'] >= 100:
        one['clf'] = 'truck'

# 확인해보기
print(json.dumps(load_vehicle, indent='   '))

# 수정한 json 파일 생성하기
new_json_path = 'new_vehicle.json'
with open(new_json_path, 'w') as mkfile:
    json.dump(load_vehicle, mkfile, indent='   ')
