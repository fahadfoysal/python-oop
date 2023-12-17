class Student:
    roll = ""
    gpa = ""

    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def get_value(self):
        print(f"Roll: {self.roll}, GPA: {self.gpa}")


rahim = Student()
rahim.set_value(1011, 3.50)
rahim.get_value()

karim = Student()
karim.set_value(1012, 3.80)
karim.get_value()