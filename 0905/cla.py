class Student:
    def __init__(self,name = "student"):
        self.name = name
    def hello(self):
        print("Hello", self.name)

# s1 = Student()
# 1.Create instance of Student
# 2.생성된 인스턴스가 자동으로 __init__함수를 호출한다.
s1 = Student() 
s1.hello()

class Box:
    def __init__(self):
        self.w = 10
        self.h = 20
    def area(self):
        return self.w * self.h
    
mybox = Box()
print('가로=%d, 세로=%d' % (mybox.w, mybox.h))
print(mybox.area())

# class Circle:
#     def __init__(self, r):
#         self.radius = r
#     def area(self):
#         return 3.14 * self.radius ** 2
#     def perimeter(self):
#         return 2*3.14*self.radius
#     def __str__(self):
#         return "r=%.2f area=%.2f perimeter=%.2f" % (self.radius, self.area(), self.perimeter())

# c1 = Circle(1.0)
# print(c1)  
# radius = float(input("반지름의 길이 입력 : "))
# c1 = Circle(radius)
# print("원의 넓이 = ", c1.area())
# print("원의 둘레길이 = ", c1.perimeter())


# class Circle:
#     def __init__(self, r):
#         self.radius = r
#     def setRadius(self, r):
#         self.__radius = r
#     def getRadius(self):
#         return self.__radius
#     def __str__(self):
#         return "Circle: radius=%f" % (self.radius)
    
# c1 = Circle(1.0)
# c2 = c1
# c2.setRadius(2.0)
# c1.setRadius(5.0)
# print(c1.getRadius())
# print(c1)
# print(c2)
# c1.__radius = 2.0 #ERROR
# c1.setRadius(2.0)
# #print(c1.__radius)
# print(c1.getRadius())


# class Circle:
#     def __init__(self, r):
#         self.radius = r
#     def setArea(self):
#         return 3.14 * self.radius**2
#     @staticmethod
#     def getInfo():
#         return "Circle"
#     @classmethod
#     def getCircle(cls, r):
#         return cls(r)
    
# print(Circle.getInfo())

# c1 = Circle(1.0)
# print(c1.setArea)
# c2 = Circle.getCircle(10)

class Shape:
    def __init__(self):
        self.name="shape"
    
class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.name = "circle"
        self.radius = 0


c1 = Circle()
print(c1.name)
print(isinstance(c1, Shape))
print(isinstance(c1, Circle))