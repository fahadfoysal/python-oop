class Phone:
    def __init__(self):
        print("I am in Phone class")

class Samsung(Phone):
    def __init__(self):
        super().__init__()  #calling super class init method
        print("I am in Samsung class")

s = Samsung()

