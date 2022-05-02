# class 만들기 : class 이름
# 상속 받을 경우 class 이름(상속받을 클래스명)

class FourClac_setData:
    def setData(self, fir, sec):  # 생성자 : 객체를 생성할 때 Default로 무엇인가를 하고 싶을 때
        self.first = fir
        self.second = sec

    def add(self):
        return self.first + self.second

    def sub(self):
        return  self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        if self.second == 0:
            return 0
        return self.first / self.second

class FourClac:
    def __init__(self, fir, sec):  # 생성자 : 객체를 생성할 때 Default로 무엇인가를 하고 싶을 때
        self.first = fir
        self.second = sec

    def add(self):
        return self.first + self.second

    def sub(self):
        return  self.first - self.second

    def mul(self):
        return self.first * self.second

    def div(self):
        return self.first / self.second

# 상속받기
class MoreCalc(FourClac):
    def __init__(self, first, second, third=1):
        # super() : 부모클래스에 있는 메서드를 그대로 사용 가능
        super().__init__(first, second)
        self.third = third

    # 부모 클래스 FourClac의 메서드들 모두 사용 가능
    # 새로운 메서드 추가해보기
    def pow(self):
        return self.first ** self.second

    # overriding : 상속받은 클래스의 메서드 수정
    def add(self):
        return super().add() + self.third

    def div(self):
        if self.second == 0:
            return 0
        return super().div()



if __name__ == "__main__":
    cal0 = FourClac_setData()
    cal0.setData(5, 3)  # init이 없으면 이런 식으로 한 번 더 값을 넘겨줘야 하는 번거로움
    print("setData : ", cal0.div())

    cal1 = FourClac(5, 2)
    print("__init__ : ", cal1.div())

    cal2 = MoreCalc(1,0,7)
    print("상속 : ", cal2.div())

    print('\nif __name__ == "__main__" 문 안에 있으면 모듈 호출했을 때 이 코드는 실행 안됨.'
          '그래서 이 안에서 테스트 코드 진행함\n')

print('\nif __name__ == "__main__" 문 밖에 있으면 모듈 호출했을 때 이 코드 같이 실행된대\n')