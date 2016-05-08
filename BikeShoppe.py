#class Exercise - Bike Shop
#BikeShoppe.py   
 
#import BikeClasses Class for ReceivingLogic Class 
from BikeClasses import BikeClass

#start of program 
bc = BikeClass()  #instance of BikeClass called bc
ownerName = raw_input("Enter Owners Name ")
bc.setName(ownerName)
modelName = raw_input("Enter Model Name ")
bc.setModel(modelName)
ticket = raw_input("Enter Ticket Number ")
bc.setTicketNumber(ticket)
cost = input("Enter Cost ")
bc.setCost(cost)
print
print
print "========================================================="
print "Thank You ", bc.getName()
print bc.getModel(), " model on ticket number ", bc.getTicketNumber()
print "will cost. ", int(bc.getCost())
print
print "========================================================="

