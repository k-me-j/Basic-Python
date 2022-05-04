import torch

def read_value(file_name):
    rtn_list = []  # return_list
    cnt = 0  # row 개수 파악

    try:
        f = open(file_name, "r")  # r=read, w=write, rw=r+w
        while True:
            line = f.readline()  # 한 줄씩 읽어오기
            if not line: break  # 더 이상 라인이 없다면 끝

            # new line(\n)을 제거하고, 탭(\t)으로 split()
            splits = line.rstrip("\n").split("\t")  # [73, 80, 75, 152] 이렇게 넣어주기 위한 단계
            element = list(map(float, splits))  # float형태로 리스트 만들어주기
            rtn_list.append(element)
            cnt += 1
        f.close()

    except FileNotFoundError as e:
        print(e)

    return rtn_list, cnt


if __name__ == "__main__":
    path = "D:/Kamie/dataset/DL_Math/score_mlr03.txt"
    rtn_list, cnt = read_value(path)
    print(rtn_list)
    print(cnt)

    print(torch.cuda.is_available())