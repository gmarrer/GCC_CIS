# PythonClasses

#person class (Parent)
class Person:
    # variables
    name = "" # intialize name
    dob = ""   # intialize dob
    
    # accessor - get and mutator - set methods
    def setName(self, inVal):
        self.name = inVal
    def getName(self):
        return self.name
    def setdob(self, inVal):
         self.dob = inVal
    def getdob(self):
        return self.dob
    #customary for class objects to represent object as string  
    def toString(self):
        print "Name ", name

#start of the class (Child)
class CheckBook(Person):
  
    #constructor with two parms for deposits and checks
    def __init__(self, inDep, inChk):
    	self.deposits =  inDep
    	self.checks = inChk
    	#print "Constructor Called"
    	#print "Deposits = ", self.deposits
    	#print "Checks = ", self.checks
 
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
#instantiate the object with call to constructor
cb = CheckBook(10, 5)
#name instance variable comes from parent
cb.setName("Gary")
#set the valud ot the deposits obj variable
cb.setDeposits(100 +  cb.getDeposits())
print "Banking Summary"
#set new value for deposits
cb.setDeposits(100 +  cb.getDeposits())
#set value for checks variable
cb.setChecks(100 +  cb.getChecks())
#module to return current balance
print cb.getName(), "'s balance is at:"
cb.CurBal()


# eop
