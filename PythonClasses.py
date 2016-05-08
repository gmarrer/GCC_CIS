# PythonClasses

#start of the class
class CheckBook:
  
    # variables
    deposits = 0  # intialize deposits instance variable to 0
    checks = 0    # intialize checks instance variable to 0
    balance = 0   # intialize balance instance variable to 0
   
    # methods    
    def CurBal(self):
        self.balance = self.deposits - self.checks   # calculate balance from object instance variable
        # print deposits, checks and balance variables
        print "Deposits $", self.deposits, " Checks $",self.checks," Balance = $",self.balance
    
   
        
    # accessor - get and mutator - set methods
    def setDeposits(self, inVal):
        self.deposits = inVal
    def getDeposits(self):
        return self.deposits
    def setChecks(self, inVal):
        self.checks = inVal
    def getChecks(self):
        return self.checks
    def toString(self):
        print "Deposits $", self.deposits, " Checks $",self.checks," Balance = $",self.balance
# end of class

#start of program
#instantiate the object
cb = CheckBook()
#set the valud ot the deposits obj variable
cb.setDeposits(100)
print "Banking Summary"
#set new value for deposits
cb.setDeposits(100 +  cb.getDeposits())
#set value for checks variable
cb.setChecks(100)
#module to return current balance
cb.CurBal()


# eop
