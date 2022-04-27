import math
def solution_1(shirt_size):
    shirt_size_list = ["XS", "S", "M", "L", "XL", "XXL"]
    result = [shirt_size.count(shirt_size_list[i]) for i in range(len(shirt_size_list))]

    return result

def solution_2(origin):
    length = len(origin)
    result = [origin[length-1-i] for i in range(length)]

    return result

def solution_3(n):
    result = 0
    for i in range(1, n+1):
        if i == 1: tmp = 1
        else: tmp += 3
        result += tmp

    return result


def solution_4(cnt_list):
    biggest = -math.inf
    smallest = math.inf

    for i in range(len(cnt_list)):
        tmp = cnt_list.count(cnt_list[i])
        if  tmp > biggest:
            biggest = tmp
        if tmp <= smallest:
            smallest = tmp

    result = biggest // smallest

    return result


if __name__ == "__main__":
    shirt_size = ["XS", "S", "M", "L", "XL", "XXL"]
    print(solution_1(shirt_size))

    original = [3,2,1,999]
    print(solution_2(original))

    n = 5
    print(solution_3(n))

    cnt_list = [1,1,1,1,1,2,2,5,999,5,5,5,5,5]
    print(solution_4(cnt_list))


