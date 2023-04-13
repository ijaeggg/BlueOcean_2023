# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 선언
# class 클래스명:
#     함수
#     함수
#     함수

# 예제1
class UserInfo: # 첫 글자는 무조건 대문자
    # 속성과 메소드
    def __init__(self, name,):
        self.name = name
    def user_info_p(self):
        print("Name: ", self.name)


user1 = UserInfo("JK")
user1.user_info_p()
user2 = UserInfo("KJ")
user2.user_info_p()

print()

print(id(user1))
print(id(user2))
print(user1.__dict__)
print(user2.__dict__)

# # 클래스, 인스턴스 차이 중요
# # 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# # 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성
# # 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용한다

# # 예제2
# # self의 이해
class SelfTest:
    def function1():
        print('function1_called')
    def function2(self):
        print(id(self))
        print('function2_called')
        
self_test = SelfTest() # self는 인스턴스 함수이고, self를 사용하지 않으면 클래스 자체의 메소드로써, 공용 함수로 쓰인다.
# self_test.function1()
SelfTest.function1()
self_test.function2()

print(id(self_test))
SelfTest.function2(self_test)

# 예제3
# 클래스 변수, 인스턴스 변수

class WarvHouse:
    # 클래스 변수
    # 예: 연봉인상율
    stock_num = 0.05
    def __init__(self, name):
        self.name = name
        WarvHouse.stock_num += 1 #공통 창고 하나당 재고 하나
    def __del__(self):
        WarvHouse.stock_num -= 1

user1 = WarvHouse('Kim')
user2 = WarvHouse('Park')
user3 = WarvHouse('Lee')

print('\n')
print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print('\n')
print(WarvHouse.__dict__)

print()
print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num)
# 자기의 네임스페이스에 없으며 클래스 공통으로 가서 찾는다.
print(user2.stock_num)
print(user3.stock_num)

del user1
print(user3.stock_num)


try:
    class WareHouse:
        # 클래스 변수
        # 예: 연봉인상율, 재고수
        stock_nub = 0
        def __init__(self, name):
            self.name = name
            WareHouse.stock_nub += 1 # 공통 창고 하나당 재고 하나
        def __del__(self):
            WareHouse.stock_nub -= 1
        def user_stock_nub(self):
            print("hello: ", WareHouse.stock_nub)
        def user_Info_mation(self):
            print('nasty boy: ', self.name)

    print('------------------------')
    print()
    user4 = WareHouse('Minister')
    user4.user_Info_mation()
    user5 = WareHouse('LustBoy')
    user5.user_Info_mation()
    user6 = WareHouse('CallMeFather')
    user6.user_Info_mation()
    user5.user_stock_nub()
    print(id(user4))
    print(user5.__dict__)
    print()
    print('------------------------')

except ValueError:
    print('You are Wrong!')
except SyntaxError:
    print('Your Syntax is Wrong anyway!')
except IndexError:
    print('fuck you anyway')
except Exception:
    print('Hi')
else:
    print('Hello Python!')
finally:
    print('Stayc girls, It\'s going down!')

print()
print('77777777777777777777777777777777777777777777777777777777')