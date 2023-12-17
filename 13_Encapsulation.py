class Bank:
    account_holder = "Rahim"
    _account_number = 1011
    __password = "@68bv"
    balance = 500

    def show_details(self):
        print(f"Account holder: {self.account_holder}, Account Number: {self._account_number}, Password: {self.__password}, Balance: {self.balance}")

user1 = Bank()
user1.show_details()
print(user1._account_holder)
# print(user1.__password) # __ indicate strongly private, which is not accessable from the outside of class