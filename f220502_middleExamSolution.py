# split 함수 구현하기

def str_split(input_str):
    rtn_list = []
    # " " 문자를 카운팅하는 방법으로 문제 접근
    cnt = input_str.count(" ")

    for _ in range(cnt):
        # find : 해당되는 문자의 index 값을 반환. 가장 첫 번째 인덱스만 반환
        cmp_value = input_str[:input_str.find(" ")]

        if cmp_value and cmp_value != " ":
            rtn_list.append(cmp_value)

        input_str = input_str[input_str.find(" ")+1:]
        
    rtn_list.append(input_str)
    return rtn_list


# pop 함수 구현해보기
input_list = [1,2,3,5,6,9]
def impl_pop(index=-1):
    '''
    가장 마지막 값이 나오길 기대 
    만약 index가 주어진다면 그 위치의 값 반환
    '''
    global input_list

    if index >= len(input_list):
        return -1
    if index == -1:
        rtn_value = input_list[index]
        input_list = input_list[:-1]
    elif index == 0:
        rtn_value = input_list[index]
        input_list = input_list[index+1:]
    else:
        rtn_value = input_list[index]
        input_list = input_list[:index] + input_list[index+1:]


if __name__ == "__main__":
    s = "  dasd   asda asd   "
    a = str_split(s)
    print(a)