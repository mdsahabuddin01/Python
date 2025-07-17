#Protected and Private methods
class BankAccount:
    MIN_BALANCE =  100 #by convention, CAPITALIZE CONSTANT

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance


    def deposit(self, amount):
        if(amount >= 0):
            self._balance += amount
            self.__log_transaction("deposit", amount)
            print(f"{self.owner}'s new balance: ${self._balance}")
        else:
            print("Deposit balance must be positive")
    
    #protected method
    def _is_valid_amount(self, amount):
        return amount > 0
    
    #private method
    def __log_transaction(self, transaction_type, amount):
        print(f"Logging {transaction_type} of ${amount}. \
              New balance: ${self._balance}")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5

account = BankAccount("Anj", 500)
account.deposit(500)

print(BankAccount.is_valid_interest_rate(3))
print(BankAccount.is_valid_interest_rate(10))
