class Student:

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def get_value(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")


rahim = Student(1011, 3.50)
rahim.get_value()

karim = Student(1012, 3.80)
karim.get_value()