#ReceivingMainOrig.py
#import receiving class module for ReceivingLogic Class
from ReceivingClass import ReceivingLogic
	
#start of program
#instanitate the receiving object
myOrder = ReceivingLogic()

myOrder.setOrderNumber("0")
#Screen Interface

print "                              Receiving Main Screen"
print
while (myOrder.getOrderNumber() != "Q"):
	print
	myOrder.setOrderNumber (raw_input("Enter Order Number or Q to Quit >>  "))
	
	display = myOrder.lookUpOrder()
	if (display != "Order Number not Found" and myOrder.setOrderNumber != "Q") :
		print "ORDER NO. |  VENDOR                                 |  VEN. ID |  QTY  |  AMOUNT |"
		print display
		flag = 0
		while (flag != 1):
			dummyDisplay = raw_input("Enter P to Process or E to process Exception or Q to Quit  >>  ")
			if (dummyDisplay.upper() != "Q"):
				if (dummyDisplay.upper() == "P"):
					print "Order Processed"
					flag = 1
				elif (dummyDisplay.upper() == "E"):
					print "goto Exception Menu" 
					flag = 1
				else:
					print "invalid entry"
			else:
				flag = 1
				myOrder.setOrderNumber("Q")
	
	else:
		if myOrder.getOrderNumber() != "Q":
			print display
	
	
#end of program	
