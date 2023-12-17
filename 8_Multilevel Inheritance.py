class A:
    def display1(self):
        print("I am inside A class")

class B(A):
    # display1 () coming from Class a Due to the inheritance
    def display2(self):
        print("I am inside B class")

class C(B):
    # display1, display2 () and coming from Class a Due to the inheritance
    def display3(self):
        super().display1()
        super().display2()
        print("I am inside C class")

obj1 = C()
obj1.display3()
# obj1.display2()
# obj1.display3()