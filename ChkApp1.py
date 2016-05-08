#-------------------------------------------------------------------------------
# Name:        chkApp1
# Purpose:
#
# Author:      Gary
#
# Created:     11/04/2016
# Copyright:   (c) Gary 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Name:        ChkApp
# Purpose:
#
# Author:      garuw82311
#
# Created:     28/10/2013
# Copyright:   (c) garuw82311 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#
#run with Python 3.x
#start of the class
from ChkClasses import *

#start of program
chkBook1 = CheckBook(0,0,0,"Fred","123 Main St", "2/15/1965")  #instanate Class with contructor
chkBook2 = CheckBook(100,50,0,"Gary","4 Pinte St", "12/15/1956")  #instanate Class with contructor

inDeposit = int(input("Enter an initial deposit >> "))
chkBook1.setDeposits(inDeposit)
# print(chkBook1.deposits)  this would be public access with I made invalid
cnt = 1

while  cnt < 5 :   #enter 4 checks
    inCheck = int(input("Enter  4 Checks  >>  "))
    chkBook1.setChecks(inCheck + chkBook1.getChecks())
    cnt = cnt + 1

print (chkBook1.toString())
chkBook1.CurBal()

print (chkBook2.toString())
chkBook2.CurBal()

#end of program
