########### 1. index error, zero division 발생하는 코드 ############
##################################################################
def proc_error():
    try:
        f = open("foo.txt", "r")
        a = [1, 2]
        print(a[3])
        b = 4 / 0  # 위에서 먼저 에러 발생하면 예외처리 하러 내려가기 때문에 여기까지는 코드 진행 안됨
        f.close()
    except (IndexError, ZeroDivisionError, FileNotFoundError) as e:
        print(e)


############################################
########### 2. 나이를 입력받는 함수 ########### # Django Framework, Flask가 됐든
############################################
# 나이 입력받는 함수에서 반환할 예외 클래스 생성 not 내장 예외 클래스
class AgeError(Exception):  # 예외 클래스를 생성할 땐 Exception을 상속받아야 함
    def __str__(self):
        return "0 이상 100세 미만으로 입력 가능합니다."

def input_age():
    while True:
        try:
            age = int(input("나이 입력하세요(숫자만 입력) : "))
            if (age < 0) or (age >= 100):
                raise AgeError  # raise로 에러 강제 발생  # 생성한 예외 클래스 호출
            break
        except ValueError:
            print("숫자만 입력 가능합니다.", end=" ")
        except AgeError as e:
            print(e, end=" ")
        finally:  # break보다 우선순위 높음, try가 break 되더라도 try문이 끝나는 순간이면 무조건 실행됨!
            print("다시 입력해주세요.")

    return age



#####################################################################################
########### 3. 별명 출력하는 함수 : "바보" 입력 시 내가 생성한 예외 클래스 호출하기 ###########
#####################################################################################
class NickError(Exception):
    def __str__(self):
        return "바보 아님!! 허용하지 않는 별명입니다."

def say_nick(nick):
    if nick == "바보":
        raise NickError
    print(nick)


################################################################################################
########### 4. 함수 입력 인자 (bool, list) 중 bool=True일 때 리스트 출력, 아니면 Error 발생 ###########
################################################################################################
class NotAccessList(Exception):
    def __str__(self):
        return "List에 접근 권한이 없습니다"

def list_access(in_bool, in_list):
    if in_bool:
        print(in_list[:])
    else:
        raise NotAccessList



if __name__ == "__main__":
    # proc_error()

    # age = input_age()
    # print(f"입력받은 나이는 {age} 살 입니다.")

    # try:
    #     say_nick("바보")
    # except NickError as e:
    #     print(e)

    try:
        list_access(1, [1,2,3,4])
        list_access(0, [4,3,2,1])
    except NotAccessList as e:
        print(e)
