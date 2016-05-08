#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Gary
#
# Created:     11/04/2016
# Copyright:   (c) Gary 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Customer():
     #  Constructor it initialize private):
    def __init__(self, inName, inAddr, inDOB):
        self.__name__ = inName  # intialize private names instance variable to constructor value
        self.__address__ = inAddr    # intialize private adaress instance variable to constructor value
        self.__DOB__= inDOB   # intialize private DOB instance variable to constructor value

    # accessor - get and mutator - set methods
    def setName(self, inVal):
        if inVal =="" :
          print("name is required")
        else:
            self.__name__ = inVal

    def getName(self):
        return self.__Name__

    def setAddress(self, inVal):
        if inVal == "" :
            print("Address is required")
        else:
            self.__address__ = inVal
    def getAddress(self):
        return self.__address__

    def setDOB(self, inVal):
        if inVal == "" :
            print("DOB is required")
        else:
            self.__DOB__ = inVal
    def getDOB(self):
        return self.__DOB__

    def toString(self):
        return "name "+  self.__name__ + " Address " + self.__address__ + " DOB " + self.__DOB__

class BadDeposit(Exception):
    # Call the base class constructor with the parameters it needs
        pass

class CheckBook(Customer):

    #  Constructor it initialize private):
    def __init__(self, dep, check, bal, name, addr, DOB):
        Customer.__init__(self, name, addr, DOB)
        self.__deposits__ = dep  # intialize private deposits instance variable to 0
        self.__checks__ = check    # intialize private checks instance variable to 0
        self.__balance__= bal   # intialize private balance instance variable to 0

    # methods
    def CurBal(self):  #public instance method
        self.__balance__ = self.__deposits__ - self.__checks__   # calculate balance from object instance variable
        # print deposits, checks and balance variables
        print ("Deposits $", self.__deposits__, " Checks $",self.__checks__," Balance = $",self.__balance__)

    # accessor - get and mutator - set methods
    def setDeposits(self, inVal):
        if inVal < 0 :
           raise BadDeposit
        else:
            self.__deposits__ = inVal

    def getDeposits(self):
        return self.__deposits__
    def setChecks(self, inVal):
        if inVal < 0 :
            print("Invalid Data = > 0")
        else:
            self.__checks__ = inVal
    def getChecks(self):
        return self.__checks__

    def toString(self):
       return "name " +  self.__name__ + " Address " + self.__address__ + " DOB " + self.__DOB__ + "Deposits $" +  str(self.__deposits__) + " Checks $" +  str(self.__checks__) + " Balance = $" + str(self.__balance__)

# end of class
