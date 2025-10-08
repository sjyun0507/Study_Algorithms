class Person:
    # pass # 아무것도 없다는 의미
    def __init__(self, name_param):
        self.name = name_param
        print("hi I am Person",self, self.name)

    def talk(self):
        print("안녕하세요 저는",self.name,"입니다")

person_1 = Person("유재석")
person_1.talk()
person_2 = Person("박명수")
person_2.talk()