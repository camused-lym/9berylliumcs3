class bankaccount:
  def __init__(self, account_number: int, balance: float):
    self.account_number = acc
    self.balance = bal
    
    @property
    def account_number(self): return self.__acc
    @account_number.setter
    def account_number(self, z): self.__acc = z
    @property
    def balance(self): return self.__bal
    @balance.setter
    def balance(self, z):
        if z < 0: print("The balance must not be a negative number.")
        else: self.__bal = float(z)
