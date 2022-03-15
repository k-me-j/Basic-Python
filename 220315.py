# list add / delete, modify ..
print("▶ list add, delete")
list_a = [1, "2", 4.2]
print(f"{list_a}, id :", id(list_a))
'''
[1, '2', 4.2], id : 2398720770688
'''

# id값 체크 : list는 mutable한 자료형
# 따라서 수정을 하더라도 새로운 객체를 생성하는 것이 아니라 동일한 주소값을 참조
list_a[1] = 4
print(f"{list_a}, id :", id(list_a))
print()
'''
[1, 4, 4.2], id : 2398720770688
'''


# list 더하기 연산
print("▶ list 더하기 연산")
list_a += [4, 5]
print(list_a)
print()
'''
[1, 4, 4.2, 4, 5]
'''


# 특정 인덱스 값을 삭제
print("▶ 특정 인덱스 값을 삭제")
list_b = [2, 5, 8, 9]
print(list_b)
del list_b[-1]
print(list_b)
print()
'''
[2, 5, 8, 9]
[2, 5, 8]
'''


# list append, sort 내장 함수
print("▶ list append, sort 내장 함수")
test_list = ['a', 'b', 'c', 1, 3, '핫', [9, 7]]
test_list.append([8, 5, 4, 7, 10])
test_list.append("String")
print(test_list)
print()
'''
['a', 'b', 'c', 1, 3, '핫', [9, 7], [8, 5, 4, 7, 10], 'String']
'''


# 추가한 리스트를 sort하기
print("▶ 추가한 리스트를 sort하기")
test_list[-2].sort()
print(test_list)
print()
'''
['a', 'b', 'c', 1, 3, '핫', [9, 7], [4, 5, 7, 8, 10], 'String']
'''


# reverse (sort하는게 아니라 단순히 뒤집기)
print("▶ reverse")
tmp_list = [1, 2, 3, 'd', 9]
tmp_list.reverse()
print(tmp_list, tmp_list.index('d'))
print()
'''
[9, 'd', 3, 2, 1] 1
'''


# list insert, remove 함수 사용
print("▶ list insert, remove 함수 사용")
print("tmp_list : ", tmp_list)
tmp_list.insert(2, ['a', 'pp', 'l', 'e'])  # tmp_list의 2번째 인덱스에 리스트 삽입
print(tmp_list)
tmp_list[2].remove('e')  # 리스트 안의 1을 삭제
print(tmp_list)
print()
'''
tmp_list :  [9, 'd', 3, 2, 1]
[9, 'd', ['a', 'pp', 'l', 'e'], 3, 2, 1]
[9, 'd', ['a', 'pp', 'l'], 3, 2, 1]
'''


# pop, count, extend
print("▶ pop, count, extend")
print("tmp_list : ", tmp_list)

print("▶▶ pop")
tmp_list.pop()  # () 안에 아무 것도 넣지 않으면 리스트의 가장 마지막 값을 pop
print(tmp_list)
tmp_list.pop(2)  # () 안에 인덱스 넣을 수 있음
print(tmp_list)

print("▶▶ count")
print(tmp_list.count('d'))

print("▶▶ extend는 더하기 연산과 동일 : list.extend(추가할 리스트)")
print()
'''
tmp_list :  [9, 'd', ['a', 'pp', 'l'], 3, 2, 1]
▶▶ pop
[9, 'd', ['a', 'pp', 'l'], 3, 2]
[9, 'd', 3, 2]
▶▶ count
1
▶▶ extend는 더하기 연산과 동일 : list.extend(추가할 리스트)
'''


