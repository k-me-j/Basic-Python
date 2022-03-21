import pandas as pd
import random as r

def score():
    return r.randint(0, 100)  # 0 ~ 100 이하의 랜덤한 정수

def df_ai_engr(nameList):
    len_student = len(nameList)
    ai_engr = pd.DataFrame()

    for i in range(1, len_student):
        ai_engr.loc[i, "Name"] = nameList[i]
        ai_engr.loc[i, "Id"] = f"2022_{i}"
        ai_engr.loc[i, "국어"] = score()
        ai_engr.loc[i, "수학"] = score()
        ai_engr.loc[i, "영어"] = score()

    return ai_engr

nameList = ['신주석', '김근형', '김동혁', '남현진', '노영하',
            '박수연', '심우석', '안원영', '오수은', '이근혁',
            '이시영', '이은정', '이은주', '장민규', '전세환',
            '정경임', '차민욱', '최민석', '최비결', '최윤정',
            '최지호', '표주혁', '허진행']

if __name__ == "__main__":
    print(df_ai_engr(nameList))
    print(df_ai_engr(nameList).info())

    # print(type(score()))

    df_ai_engr(nameList).to_csv("D:/Kamie/mon_ML/f220321.csv")

