class A:
    def display(self):
        print("I am inside A class")

class B:
    def display(self):
        print("I am inside B class")

class C(A, B):
    # Class A-display , B-display () and coming from Class a Due to the inheritance
    # def display(self):
    #     print("I am inside C class")
    pass

obj1 = C()
obj1.display()
# obj1.display2()
# obj1.display3()